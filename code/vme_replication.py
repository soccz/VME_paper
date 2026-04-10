"""
Value and Momentum Everywhere (Asness, Moskowitz, Pedersen, 2013)
실험 재현 코드

논문의 핵심 실험을 Python으로 재현:
- Table I:  8개 자산군 Value/Momentum 포트폴리오 수익률 통계
- Table II: 자산군 간 상관관계 (Comovement)
- Fig 1-2: 누적수익률 시각화
- Table III-IV: 매크로/유동성 리스크 분석
- Table V-VI: 3-Factor 가격결정 모델
- Table VII: 강건성 검증
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy import stats
import statsmodels.api as sm
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# 0. 설정
# ============================================================
ASSET_CLASSES = [
    'us_stocks', 'uk_stocks', 'eu_stocks', 'jp_stocks',  # 개별주식 4개
    'country_idx', 'currencies', 'fixed_income', 'commodities'  # 비주식 4개
]

STOCK_CLASSES = ['us_stocks', 'uk_stocks', 'eu_stocks', 'jp_stocks']
NONSTOCK_CLASSES = ['country_idx', 'currencies', 'fixed_income', 'commodities']

SAMPLE_PERIODS = {
    'us_stocks':    ('1972-01', '2011-07'),
    'uk_stocks':    ('1972-01', '2011-07'),
    'eu_stocks':    ('1974-01', '2011-07'),
    'jp_stocks':    ('1974-01', '2011-07'),
    'country_idx':  ('1978-01', '2011-07'),
    'currencies':   ('1979-01', '2011-07'),
    'fixed_income': ('1982-01', '2011-07'),
    'commodities':  ('1972-01', '2011-07'),
}

ANNUALIZE = 12  # 월간 → 연간

OUTPUT_DIR = Path(__file__).parent / 'output'
OUTPUT_DIR.mkdir(exist_ok=True)


# ============================================================
# 1. 데이터 로딩
# ============================================================
def load_data(data_dir: str) -> dict:
    """
    데이터 로딩. 데이터 포맷에 맞게 수정 필요.

    기대하는 입력 형식 (자산군별):
    - returns: DataFrame (date × assets), 월간 초과수익률
    - signals_value: DataFrame (date × assets), value 시그널
    - signals_mom: DataFrame (date × assets), momentum 시그널
    - market_cap: DataFrame (date × assets), 시가총액 (주식만)
    - market_return: Series (date), 시장 벤치마크 수익률

    Returns:
        dict[asset_class] -> {returns, signals_value, signals_mom, market_cap, market_return}
    """
    data = {}
    data_path = Path(data_dir)

    for ac in ASSET_CLASSES:
        ac_path = data_path / ac
        if not ac_path.exists():
            print(f"[WARN] {ac} 데이터 없음, 건너뜀: {ac_path}")
            continue

        # TODO: 실제 데이터 포맷에 맞게 수정
        # 예시: CSV 파일 로딩
        try:
            returns = pd.read_csv(ac_path / 'returns.csv', index_col=0, parse_dates=True)
            sig_val = pd.read_csv(ac_path / 'signal_value.csv', index_col=0, parse_dates=True)
            sig_mom = pd.read_csv(ac_path / 'signal_mom.csv', index_col=0, parse_dates=True)

            mkt_ret = pd.read_csv(ac_path / 'market_return.csv', index_col=0, parse_dates=True).squeeze()

            mkt_cap = None
            if ac in STOCK_CLASSES:
                mkt_cap = pd.read_csv(ac_path / 'market_cap.csv', index_col=0, parse_dates=True)

            data[ac] = {
                'returns': returns,
                'signals_value': sig_val,
                'signals_mom': sig_mom,
                'market_cap': mkt_cap,
                'market_return': mkt_ret,
            }
            print(f"[OK] {ac}: {returns.shape[0]} months, {returns.shape[1]} assets")
        except Exception as e:
            print(f"[ERR] {ac} 로딩 실패: {e}")

    return data


# ============================================================
# 2. 시그널 구성 (데이터가 raw일 때 사용)
# ============================================================
def compute_value_signal(prices, book_values, asset_class):
    """
    Value 시그널 계산.

    - 개별주식: BE/ME (장부가치 6개월 래그 / 현재 시가총액)
    - 국가지수: MSCI BE/ME
    - 통화:     -1 × 5년 환율변화 + PPP 조정
    - 채권:     5년 금리 변화
    - 원자재:   -1 × 5년 현물가격 변화 (log)
    """
    if asset_class in STOCK_CLASSES:
        # BE/ME: 장부가치(6개월 래그) / 시장가치(현재)
        bv_lagged = book_values.shift(6)
        return bv_lagged / prices  # prices = market_cap

    elif asset_class == 'country_idx':
        # 해당 국가 MSCI 지수의 BE/ME
        return book_values  # 이미 BE/ME로 제공된다고 가정

    elif asset_class == 'commodities':
        # -log(P_t / P_{t-60}) ≈ log(P_{t-60}) - log(P_t)
        # 4.5~5.5년 전 평균 vs 현재
        log_p = np.log(prices)
        avg_past = log_p.rolling(12).mean().shift(54)  # 4.5~5.5년 전 12개월 평균
        return avg_past - log_p

    elif asset_class == 'currencies':
        # -1 × 5년 환율 수익률 (PPP 조정)
        log_fx = np.log(prices)
        return -(log_fx - log_fx.shift(60))  # 단순화: CPI 조정은 데이터 필요

    elif asset_class == 'fixed_income':
        # 5년 금리 변화 (yield change)
        return book_values - book_values.shift(60)  # book_values = yields

    return None


def compute_momentum_signal(returns):
    """
    Momentum 시그널: 과거 12개월 누적수익률, 최근 1개월 제외 (MOM2-12).
    모든 자산군에 동일하게 적용.
    """
    # 12개월 누적수익률 (2~12개월 전)
    cum_ret_12 = (1 + returns).rolling(12).apply(lambda x: x.prod(), raw=True) - 1
    # 1개월 스킵
    mom_signal = cum_ret_12.shift(1)
    return mom_signal


# ============================================================
# 3. 포트폴리오 구성
# ============================================================
def form_tercile_portfolios(returns, signal, market_cap=None, is_stock=False):
    """
    Tercile 정렬 포트폴리오 (P1=Low, P2=Mid, P3=High).

    - 주식: 시가총액 가중
    - 비주식: 동일 가중

    Args:
        returns: DataFrame (date × assets)
        signal: DataFrame (date × assets)
        market_cap: DataFrame (date × assets), 주식일 때만
        is_stock: bool

    Returns:
        DataFrame with columns ['P1', 'P2', 'P3'] (월간 수익률)
    """
    dates = returns.index.intersection(signal.index)
    result = pd.DataFrame(index=dates, columns=['P1', 'P2', 'P3'], dtype=float)

    for t in dates:
        ret_t = returns.loc[t].dropna()
        sig_t = signal.shift(1).loc[t].dropna()  # 시그널은 전월 기준

        common = ret_t.index.intersection(sig_t.index)
        if len(common) < 3:
            continue

        ret_t = ret_t[common]
        sig_t = sig_t[common]

        # Tercile 분류
        ranks = sig_t.rank(pct=True)
        low = ranks <= 1/3
        mid = (ranks > 1/3) & (ranks <= 2/3)
        high = ranks > 2/3

        if is_stock and market_cap is not None:
            # 시가총액 가중 (beginning-of-month)
            cap_t = market_cap.shift(1).loc[t][common].fillna(0)

            for label, mask in [('P1', low), ('P2', mid), ('P3', high)]:
                if mask.sum() == 0:
                    continue
                w = cap_t[mask]
                w = w / w.sum()
                result.loc[t, label] = (ret_t[mask] * w).sum()
        else:
            # 동일 가중
            for label, mask in [('P1', low), ('P2', mid), ('P3', high)]:
                if mask.sum() == 0:
                    continue
                result.loc[t, label] = ret_t[mask].mean()

    return result.astype(float)


def form_factor_portfolio(returns, signal):
    """
    시그널 가중 팩터 포트폴리오 (논문 Eq. 1-2).

    w_i = c * (rank(S_i) - mean(rank(S_i)))
    달러-중립, $1 long / $1 short으로 스케일링.
    """
    dates = returns.index.intersection(signal.index)
    factor_ret = pd.Series(index=dates, dtype=float)

    for t in dates:
        ret_t = returns.loc[t].dropna()
        sig_t = signal.shift(1).loc[t].dropna()

        common = ret_t.index.intersection(sig_t.index)
        if len(common) < 3:
            continue

        ret_t = ret_t[common]
        sig_t = sig_t[common]

        # 랭크 기반 가중치
        ranks = sig_t.rank()
        w = ranks - ranks.mean()

        # $1 long, $1 short으로 스케일링
        if w.abs().sum() == 0:
            continue
        c = 2.0 / w.abs().sum()
        w = w * c

        factor_ret.loc[t] = (ret_t * w).sum()

    return factor_ret


def form_combo_factor(val_factor, mom_factor):
    """50/50 Value + Momentum 조합 (Eq. 3)."""
    common = val_factor.index.intersection(mom_factor.index)
    return 0.5 * val_factor[common] + 0.5 * mom_factor[common]


# ============================================================
# 4. Table I: 수익률 통계
# ============================================================
def compute_return_stats(returns_series, market_return=None):
    """
    논문 Table I의 통계량 계산.

    Returns:
        dict: mean, t_stat, stdev, sharpe, alpha, alpha_tstat
    """
    r = returns_series.dropna()
    n = len(r)
    if n < 12:
        return {k: np.nan for k in ['mean', 't_stat', 'stdev', 'sharpe', 'alpha', 'alpha_tstat']}

    # 연율화 통계
    mean_m = r.mean()
    std_m = r.std(ddof=1)

    mean_ann = mean_m * ANNUALIZE
    std_ann = std_m * np.sqrt(ANNUALIZE)
    t_stat = mean_m / (std_m / np.sqrt(n))
    sharpe = mean_ann / std_ann if std_ann > 0 else np.nan

    # Alpha (시장 대비 회귀)
    alpha, alpha_tstat = np.nan, np.nan
    if market_return is not None:
        mkt = market_return.reindex(r.index).dropna()
        common = r.index.intersection(mkt.index)
        if len(common) > 12:
            y = r[common]
            X = sm.add_constant(mkt[common])
            reg = sm.OLS(y, X).fit(cov_type='HAC', cov_kwds={'maxlags': 6})
            alpha = reg.params.iloc[0] * ANNUALIZE
            alpha_tstat = reg.tvalues.iloc[0]

    return {
        'mean': mean_ann,
        't_stat': t_stat,
        'stdev': std_ann,
        'sharpe': sharpe,
        'alpha': alpha,
        'alpha_tstat': alpha_tstat,
    }


def replicate_table_I(data: dict) -> pd.DataFrame:
    """
    Table I 재현: 각 자산군별 Value/Momentum 포트폴리오 통계.

    Panel A: 개별주식 (US, UK, EU, JP + Global stocks)
    Panel B: 비주식 자산군 (Country idx, Currencies, Fixed income, Commodities)
    """
    all_results = []

    for ac in ASSET_CLASSES:
        if ac not in data:
            continue

        d = data[ac]
        is_stock = ac in STOCK_CLASSES
        mkt_ret = d['market_return']

        # Value 포트폴리오
        val_ports = form_tercile_portfolios(
            d['returns'], d['signals_value'], d['market_cap'], is_stock
        )
        val_factor = form_factor_portfolio(d['returns'], d['signals_value'])
        val_spread = val_ports['P3'] - val_ports['P1']

        # Momentum 포트폴리오
        mom_ports = form_tercile_portfolios(
            d['returns'], d['signals_mom'], d['market_cap'], is_stock
        )
        mom_factor = form_factor_portfolio(d['returns'], d['signals_mom'])
        mom_spread = mom_ports['P3'] - mom_ports['P1']

        # 50/50 Combo
        combo_spread = form_combo_factor(val_spread, mom_spread)
        combo_factor = form_combo_factor(val_factor, mom_factor)

        # Val-Mom 상관관계
        common = val_factor.dropna().index.intersection(mom_factor.dropna().index)
        corr_vm = val_factor[common].corr(mom_factor[common]) if len(common) > 12 else np.nan

        # 통계 계산
        row = {'asset_class': ac}

        for label, series in [
            ('val_P1', val_ports['P1']), ('val_P2', val_ports['P2']), ('val_P3', val_ports['P3']),
            ('val_P3-P1', val_spread), ('val_factor', val_factor),
            ('mom_P1', mom_ports['P1']), ('mom_P2', mom_ports['P2']), ('mom_P3', mom_ports['P3']),
            ('mom_P3-P1', mom_spread), ('mom_factor', mom_factor),
            ('combo_P3-P1', combo_spread), ('combo_factor', combo_factor),
        ]:
            s = compute_return_stats(series, mkt_ret)
            for k, v in s.items():
                row[f'{label}_{k}'] = v

        row['corr_val_mom'] = corr_vm
        all_results.append(row)

    return pd.DataFrame(all_results)


def print_table_I(df: pd.DataFrame):
    """Table I 결과를 논문 형식으로 출력."""
    print("\n" + "=" * 100)
    print("TABLE I: Performance of Value and Momentum Portfolios across Markets and Asset Classes")
    print("=" * 100)

    for _, row in df.iterrows():
        ac = row['asset_class']
        print(f"\n--- {ac} ---")
        print(f"{'':20s} {'P1':>8s} {'P2':>8s} {'P3':>8s} {'P3-P1':>8s} {'Factor':>8s}")

        for strategy in ['val', 'mom']:
            label = 'Value' if strategy == 'val' else 'Momentum'
            print(f"\n  {label} Portfolios:")
            print(f"  {'Mean':20s}", end='')
            for col in ['P1', 'P2', 'P3', 'P3-P1', 'factor']:
                v = row.get(f'{strategy}_{col}_mean', np.nan)
                print(f" {v:7.1%}" if not np.isnan(v) else f" {'N/A':>7s}", end='')
            print()

            print(f"  {'(t-stat)':20s}", end='')
            for col in ['P1', 'P2', 'P3', 'P3-P1', 'factor']:
                v = row.get(f'{strategy}_{col}_t_stat', np.nan)
                print(f" ({v:5.2f})" if not np.isnan(v) else f" {'N/A':>7s}", end='')
            print()

            print(f"  {'Stdev':20s}", end='')
            for col in ['P1', 'P2', 'P3', 'P3-P1', 'factor']:
                v = row.get(f'{strategy}_{col}_stdev', np.nan)
                print(f" {v:7.1%}" if not np.isnan(v) else f" {'N/A':>7s}", end='')
            print()

            print(f"  {'Sharpe':20s}", end='')
            for col in ['P1', 'P2', 'P3', 'P3-P1', 'factor']:
                v = row.get(f'{strategy}_{col}_sharpe', np.nan)
                print(f" {v:7.2f}" if not np.isnan(v) else f" {'N/A':>7s}", end='')
            print()

            print(f"  {'Alpha':20s}", end='')
            for col in ['P1', 'P2', 'P3', 'P3-P1', 'factor']:
                v = row.get(f'{strategy}_{col}_alpha', np.nan)
                print(f" {v:7.1%}" if not np.isnan(v) else f" {'N/A':>7s}", end='')
            print()

        # 50/50 Combo
        print(f"\n  50/50 Combination:")
        for stat_name, stat_key in [('Mean', 'mean'), ('Sharpe', 'sharpe')]:
            print(f"  {stat_name:20s}", end='')
            for col in ['P3-P1', 'factor']:
                v = row.get(f'combo_{col}_{stat_key}', np.nan)
                fmt = f" {v:7.1%}" if stat_key == 'mean' else f" {v:7.2f}"
                print(fmt if not np.isnan(v) else f" {'N/A':>7s}", end='')
            print()

        print(f"  Corr(Val, Mom) = {row.get('corr_val_mom', np.nan):.2f}")


# ============================================================
# 5. Table II: Comovement (상관관계 매트릭스)
# ============================================================
def replicate_table_II(data: dict) -> dict:
    """
    Table II 재현: 자산군 간 Value/Momentum 상관관계.

    Panel A: 평균 수익률 시계열 간 상관관계
    Panel B: 주식 vs 비주식 시계열 간 상관관계
    """
    # 각 자산군의 value/momentum 팩터 수익률 추출
    factors = {}
    for ac in ASSET_CLASSES:
        if ac not in data:
            continue
        d = data[ac]
        is_stock = ac in STOCK_CLASSES

        val_f = form_factor_portfolio(d['returns'], d['signals_value'])
        mom_f = form_factor_portfolio(d['returns'], d['signals_mom'])
        factors[ac] = {'value': val_f, 'momentum': mom_f}

    # --- Panel A: 그룹별 평균 후 상관관계 ---
    stock_val = _average_factors([factors[ac]['value'] for ac in STOCK_CLASSES if ac in factors])
    stock_mom = _average_factors([factors[ac]['momentum'] for ac in STOCK_CLASSES if ac in factors])
    nonstock_val = _average_factors([factors[ac]['value'] for ac in NONSTOCK_CLASSES if ac in factors])
    nonstock_mom = _average_factors([factors[ac]['momentum'] for ac in NONSTOCK_CLASSES if ac in factors])

    panel_a_series = {
        'Stock Value': stock_val,
        'Nonstock Value': nonstock_val,
        'Stock Momentum': stock_mom,
        'Nonstock Momentum': nonstock_mom,
    }

    panel_a = _compute_corr_matrix(panel_a_series)

    # --- Panel B: 개별 자산군 간 상관관계 ---
    panel_b_series = {}
    for ac in ASSET_CLASSES:
        if ac not in factors:
            continue
        ac_short = ac.replace('_stocks', '').replace('_', ' ').title()
        panel_b_series[f'{ac_short} Val'] = factors[ac]['value']
        panel_b_series[f'{ac_short} Mom'] = factors[ac]['momentum']

    panel_b = _compute_corr_matrix(panel_b_series)

    return {'panel_a': panel_a, 'panel_b': panel_b}


def _average_factors(factor_list):
    """여러 팩터의 평균 (공통 기간)."""
    if not factor_list:
        return pd.Series(dtype=float)
    df = pd.concat(factor_list, axis=1)
    return df.mean(axis=1)


def _compute_corr_matrix(series_dict):
    """시리즈 딕셔너리로부터 상관관계 매트릭스 계산."""
    df = pd.DataFrame(series_dict)
    return df.corr()


def print_table_II(result: dict):
    """Table II 결과 출력."""
    print("\n" + "=" * 80)
    print("TABLE II: Correlation of Value and Momentum across Asset Classes")
    print("=" * 80)

    print("\nPanel A: Correlation of Average Return Series")
    print(result['panel_a'].round(2).to_string())

    print("\nPanel B: Correlation of Average Stock Series with Each Nonstock Series")
    print(result['panel_b'].round(2).to_string())


# ============================================================
# 6. Figure 1-2: 누적수익률 시각화
# ============================================================
def replicate_figures_1_2(data: dict):
    """
    Figure 1: 각 자산군별 Value, Momentum, Combo 누적수익률
    Figure 2: Global (전체 자산군 결합) 누적수익률
    """
    fig1, axes = plt.subplots(2, 4, figsize=(20, 10))
    fig1.suptitle('Figure 1: Cumulative Returns of Value, Momentum, and Combo by Asset Class',
                  fontsize=14, fontweight='bold')

    global_val_factors = []
    global_mom_factors = []

    for idx, ac in enumerate(ASSET_CLASSES):
        if ac not in data:
            continue

        ax = axes[idx // 4, idx % 4]
        d = data[ac]

        val_f = form_factor_portfolio(d['returns'], d['signals_value'])
        mom_f = form_factor_portfolio(d['returns'], d['signals_mom'])
        combo_f = form_combo_factor(val_f, mom_f)

        global_val_factors.append(val_f)
        global_mom_factors.append(mom_f)

        # 누적수익률 ($1 투자)
        for series, label, color in [
            (val_f, 'Value', 'blue'),
            (mom_f, 'Momentum', 'red'),
            (combo_f, 'Combo', 'green'),
        ]:
            cum = (1 + series.dropna()).cumprod()
            ax.plot(cum.index, cum.values, label=label, color=color, linewidth=1)

        ax.set_title(ac.replace('_', ' ').title(), fontsize=11)
        ax.set_yscale('log')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    fig1.tight_layout()
    fig1.savefig(OUTPUT_DIR / 'figure1_cumulative_by_asset.png', dpi=150, bbox_inches='tight')
    print(f"[OK] Figure 1 saved: {OUTPUT_DIR / 'figure1_cumulative_by_asset.png'}")

    # --- Figure 2: Global ---
    fig2, ax = plt.subplots(figsize=(12, 6))
    fig2.suptitle('Figure 2: Cumulative Returns — Global Value, Momentum, and Combo',
                  fontsize=14, fontweight='bold')

    # 글로벌 팩터: 변동성 역수 가중 (논문 각주 11)
    global_val = _volatility_weighted_average(global_val_factors)
    global_mom = _volatility_weighted_average(global_mom_factors)
    global_combo = form_combo_factor(global_val, global_mom)

    for series, label, color in [
        (global_val, 'Global Value', 'blue'),
        (global_mom, 'Global Momentum', 'red'),
        (global_combo, 'Global Combo', 'green'),
    ]:
        cum = (1 + series.dropna()).cumprod()
        ax.plot(cum.index, cum.values, label=label, color=color, linewidth=1.5)

    ax.set_yscale('log')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_ylabel('Cumulative Return ($1 invested)')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    fig2.tight_layout()
    fig2.savefig(OUTPUT_DIR / 'figure2_cumulative_global.png', dpi=150, bbox_inches='tight')
    print(f"[OK] Figure 2 saved: {OUTPUT_DIR / 'figure2_cumulative_global.png'}")

    plt.close('all')
    return global_val, global_mom, global_combo


def _volatility_weighted_average(factor_list):
    """
    변동성 역수 가중 평균 (논문 각주 11).
    각 자산군이 동일한 변동성 기여를 하도록 가중.
    """
    if not factor_list:
        return pd.Series(dtype=float)

    df = pd.concat(factor_list, axis=1)
    # 각 자산군의 전체 표본 월간 변동성
    vols = df.std()
    inv_vols = 1.0 / vols
    weights = inv_vols / inv_vols.sum()

    return (df * weights.values).sum(axis=1)


# ============================================================
# 7. Table III-IV: 매크로/유동성 리스크 분석
# ============================================================
def replicate_table_III_IV(data: dict, macro_data: dict = None) -> dict:
    """
    Table III: 매크로 변수와 Value/Momentum 수익률의 관계
    Table IV: 유동성 리스크 (TED spread, Pastor-Stambaugh 등)

    macro_data 기대 형식:
    {
        'gdp_growth': Series,       # GDP 성장률
        'recession': Series,        # NBER 경기침체 더미
        'consumption_growth': Series,  # 소비 성장률
        'ted_spread': Series,       # TED spread (유동성 프록시)
        'liquidity_innovation': Series,  # Pastor-Stambaugh 유동성 혁신
        'funding_liquidity': Series,    # Brunnermeier-Pedersen 자금조달 유동성
    }
    """
    # 글로벌 팩터 구성
    val_factors = []
    mom_factors = []
    for ac in ASSET_CLASSES:
        if ac not in data:
            continue
        d = data[ac]
        val_factors.append(form_factor_portfolio(d['returns'], d['signals_value']))
        mom_factors.append(form_factor_portfolio(d['returns'], d['signals_mom']))

    global_val = _volatility_weighted_average(val_factors)
    global_mom = _volatility_weighted_average(mom_factors)
    global_combo = form_combo_factor(global_val, global_mom)

    if macro_data is None:
        print("[WARN] 매크로 데이터 없음. Table III-IV 건너뜀.")
        return {}

    results = {}

    # --- Table III: 매크로 변수 회귀 ---
    dep_vars = {
        'Global Value': global_val,
        'Global Momentum': global_mom,
        'Global Combo': global_combo,
    }

    for macro_name, macro_series in macro_data.items():
        reg_results = {}
        for dep_name, dep_series in dep_vars.items():
            common = dep_series.dropna().index.intersection(macro_series.dropna().index)
            if len(common) < 24:
                continue

            y = dep_series[common]
            X = sm.add_constant(macro_series[common])
            reg = sm.OLS(y, X).fit(cov_type='HAC', cov_kwds={'maxlags': 6})

            reg_results[dep_name] = {
                'beta': reg.params.iloc[1],
                't_stat': reg.tvalues.iloc[1],
                'r_squared': reg.rsquared,
            }

        results[macro_name] = reg_results

    return results


def print_table_III_IV(results: dict):
    """Table III-IV 결과 출력."""
    print("\n" + "=" * 80)
    print("TABLE III-IV: Macroeconomic and Liquidity Risk Exposures")
    print("=" * 80)

    if not results:
        print("(매크로 데이터 미제공)")
        return

    for macro_name, regs in results.items():
        print(f"\n  Macro variable: {macro_name}")
        print(f"  {'':25s} {'Beta':>10s} {'t-stat':>10s} {'R²':>10s}")
        for dep_name, stats in regs.items():
            print(f"  {dep_name:25s} {stats['beta']:10.4f} {stats['t_stat']:10.2f} {stats['r_squared']:10.3f}")


# ============================================================
# 8. Table V-VI: 3-Factor 가격결정 모델
# ============================================================
def replicate_table_V_VI(data: dict) -> dict:
    """
    Table V:  3-Factor 모델로 48개 포트폴리오의 수익률 설명
    Table VI: 3-Factor 모델로 Fama-French 포트폴리오 + 헤지펀드 지수 설명

    3-Factor 모델:
      r_i,t = alpha_i + beta_1 * MKT_t + beta_2 * VAL_t + beta_3 * MOM_t + e_i,t

    MKT = 글로벌 시장 포트폴리오
    VAL = 글로벌 value 팩터 (모든 자산군)
    MOM = 글로벌 momentum 팩터 (모든 자산군)
    """
    # 글로벌 팩터 구성
    val_factors = []
    mom_factors = []
    mkt_factors = []

    for ac in ASSET_CLASSES:
        if ac not in data:
            continue
        d = data[ac]
        val_factors.append(form_factor_portfolio(d['returns'], d['signals_value']))
        mom_factors.append(form_factor_portfolio(d['returns'], d['signals_mom']))
        if d['market_return'] is not None:
            mkt_factors.append(d['market_return'])

    global_val = _volatility_weighted_average(val_factors)
    global_mom = _volatility_weighted_average(mom_factors)
    global_mkt = _volatility_weighted_average(mkt_factors) if mkt_factors else pd.Series(dtype=float)

    # --- Table V: 48개 테스트 포트폴리오 pricing ---
    test_portfolios = {}
    for ac in ASSET_CLASSES:
        if ac not in data:
            continue
        d = data[ac]
        is_stock = ac in STOCK_CLASSES

        for signal_type, signal_data in [('val', d['signals_value']), ('mom', d['signals_mom'])]:
            ports = form_tercile_portfolios(d['returns'], signal_data, d['market_cap'], is_stock)
            for p in ['P1', 'P2', 'P3']:
                name = f"{ac}_{signal_type}_{p}"
                test_portfolios[name] = ports[p]

    # 시계열 회귀: GRS 테스트
    alphas = {}
    for name, port_ret in test_portfolios.items():
        port_ret = port_ret.dropna()
        common = port_ret.index
        for f in [global_mkt, global_val, global_mom]:
            common = common.intersection(f.dropna().index)

        if len(common) < 24:
            continue

        y = port_ret[common]
        X = pd.DataFrame({
            'MKT': global_mkt[common],
            'VAL': global_val[common],
            'MOM': global_mom[common],
        })
        X = sm.add_constant(X)

        reg = sm.OLS(y, X).fit(cov_type='HAC', cov_kwds={'maxlags': 6})

        alphas[name] = {
            'alpha': reg.params['const'] * ANNUALIZE,
            'alpha_tstat': reg.tvalues['const'],
            'beta_mkt': reg.params.get('MKT', np.nan),
            'beta_val': reg.params.get('VAL', np.nan),
            'beta_mom': reg.params.get('MOM', np.nan),
            'r_squared': reg.rsquared,
        }

    # GRS 테스트 (Gibbons, Ross, Shanken, 1989)
    grs_stat, grs_pval = _grs_test(test_portfolios, global_mkt, global_val, global_mom)

    return {
        'alphas': pd.DataFrame(alphas).T,
        'grs_stat': grs_stat,
        'grs_pval': grs_pval,
        'global_factors': {
            'MKT': global_mkt,
            'VAL': global_val,
            'MOM': global_mom,
        }
    }


def _grs_test(test_portfolios, *factors):
    """
    GRS test (Gibbons, Ross, Shanken, 1989).
    H0: 모든 alpha가 동시에 0.
    """
    # 공통 기간
    common_dates = None
    for name, ret in test_portfolios.items():
        idx = ret.dropna().index
        common_dates = idx if common_dates is None else common_dates.intersection(idx)
    for f in factors:
        common_dates = common_dates.intersection(f.dropna().index)

    if common_dates is None or len(common_dates) < 30:
        return np.nan, np.nan

    T = len(common_dates)
    N = len(test_portfolios)
    K = len(factors)

    # 회귀하여 alpha 벡터와 잔차 추출
    alpha_vec = []
    residuals = []

    F = pd.DataFrame({f'f{i}': f[common_dates] for i, f in enumerate(factors)})
    F_const = sm.add_constant(F)

    for name, ret in test_portfolios.items():
        y = ret[common_dates]
        reg = sm.OLS(y, F_const).fit()
        alpha_vec.append(reg.params['const'])
        residuals.append(reg.resid)

    alpha_vec = np.array(alpha_vec)
    residuals = np.column_stack(residuals)

    # Sigma (잔차 공분산), Omega (팩터 공분산)
    Sigma = np.cov(residuals.T, ddof=K+1)
    f_mean = F.mean().values
    Omega = np.cov(F.T, ddof=1)

    # GRS = (T/N) * ((T-N-K)/(T-K-1)) * (alpha' Sigma^-1 alpha) / (1 + mu_f' Omega^-1 mu_f)
    try:
        Sigma_inv = np.linalg.inv(Sigma)
        Omega_inv = np.linalg.inv(Omega)

        numerator = alpha_vec @ Sigma_inv @ alpha_vec
        denominator = 1 + f_mean @ Omega_inv @ f_mean

        grs = (T / N) * ((T - N - K) / (T - K - 1)) * (numerator / denominator)

        from scipy.stats import f as f_dist
        pval = 1 - f_dist.cdf(grs, N, T - N - K)

        return grs, pval
    except np.linalg.LinAlgError:
        return np.nan, np.nan


def print_table_V_VI(result: dict):
    """Table V-VI 결과 출력."""
    print("\n" + "=" * 80)
    print("TABLE V-VI: Three-Factor Pricing Model")
    print("=" * 80)

    if 'alphas' in result and len(result['alphas']) > 0:
        df = result['alphas']
        print(f"\nGRS test statistic: {result.get('grs_stat', np.nan):.2f}")
        print(f"GRS p-value: {result.get('grs_pval', np.nan):.4f}")

        print(f"\n{'Portfolio':30s} {'Alpha':>8s} {'t(α)':>8s} {'β_MKT':>8s} {'β_VAL':>8s} {'β_MOM':>8s} {'R²':>8s}")
        print("-" * 80)
        for name, row in df.iterrows():
            print(f"{name:30s} {row['alpha']:7.1%} {row['alpha_tstat']:8.2f} "
                  f"{row['beta_mkt']:8.2f} {row['beta_val']:8.2f} {row['beta_mom']:8.2f} "
                  f"{row['r_squared']:8.3f}")


# ============================================================
# 9. Table VII: 강건성 검증
# ============================================================
def replicate_table_VII(data: dict) -> dict:
    """
    Table VII: 강건성 검증.
    - 거래비용 고려
    - 하위 기간 분석 (전반/후반)
    - 1월 효과 제거
    - 극단적 시장 상황 제거
    """
    results = {}

    for ac in ASSET_CLASSES:
        if ac not in data:
            continue

        d = data[ac]
        is_stock = ac in STOCK_CLASSES

        val_f = form_factor_portfolio(d['returns'], d['signals_value'])
        mom_f = form_factor_portfolio(d['returns'], d['signals_mom'])
        combo_f = form_combo_factor(val_f, mom_f)

        ac_results = {}

        # 전체 기간
        ac_results['full'] = {
            'val': compute_return_stats(val_f)['sharpe'],
            'mom': compute_return_stats(mom_f)['sharpe'],
            'combo': compute_return_stats(combo_f)['sharpe'],
        }

        # 하위 기간: 전반/후반
        midpoint = val_f.dropna().index[len(val_f.dropna()) // 2]

        first_half_v = val_f[val_f.index <= midpoint]
        second_half_v = val_f[val_f.index > midpoint]
        first_half_m = mom_f[mom_f.index <= midpoint]
        second_half_m = mom_f[mom_f.index > midpoint]

        ac_results['first_half'] = {
            'val': compute_return_stats(first_half_v)['sharpe'],
            'mom': compute_return_stats(first_half_m)['sharpe'],
        }
        ac_results['second_half'] = {
            'val': compute_return_stats(second_half_v)['sharpe'],
            'mom': compute_return_stats(second_half_m)['sharpe'],
        }

        # 1월 제외
        no_jan_v = val_f[val_f.index.month != 1]
        no_jan_m = mom_f[mom_f.index.month != 1]
        ac_results['ex_january'] = {
            'val': compute_return_stats(no_jan_v)['sharpe'],
            'mom': compute_return_stats(no_jan_m)['sharpe'],
        }

        results[ac] = ac_results

    return results


def print_table_VII(results: dict):
    """Table VII 결과 출력."""
    print("\n" + "=" * 80)
    print("TABLE VII: Robustness Checks")
    print("=" * 80)

    print(f"\n{'Asset Class':20s} {'Full':>8s} {'1st Half':>8s} {'2nd Half':>8s} {'Ex-Jan':>8s}")
    print("-" * 60)

    for ac, res in results.items():
        for strategy in ['val', 'mom', 'combo']:
            label = f"{ac} {strategy.upper()}"
            full = res.get('full', {}).get(strategy, np.nan)
            first = res.get('first_half', {}).get(strategy, np.nan)
            second = res.get('second_half', {}).get(strategy, np.nan)
            exjan = res.get('ex_january', {}).get(strategy, np.nan)

            vals = [full, first, second, exjan]
            formatted = [f"{v:8.2f}" if not np.isnan(v) else f"{'N/A':>8s}" for v in vals]
            print(f"  {label:20s} {''.join(formatted)}")


# ============================================================
# 10. 메인 실행
# ============================================================
def run_all(data_dir: str, macro_data: dict = None):
    """전체 재현 파이프라인 실행."""
    print("=" * 60)
    print("  Value and Momentum Everywhere — Replication")
    print("  Asness, Moskowitz, Pedersen (2013)")
    print("=" * 60)

    # 1. 데이터 로딩
    print("\n[1/6] 데이터 로딩...")
    data = load_data(data_dir)

    if not data:
        print("[ERR] 데이터가 없습니다. data_dir을 확인하세요.")
        return

    # 2. Table I
    print("\n[2/6] Table I: 포트폴리오 수익률 통계...")
    table_I = replicate_table_I(data)
    print_table_I(table_I)
    table_I.to_csv(OUTPUT_DIR / 'table_I.csv', index=False)

    # 3. Table II
    print("\n[3/6] Table II: Comovement 상관관계...")
    table_II = replicate_table_II(data)
    print_table_II(table_II)
    table_II['panel_a'].to_csv(OUTPUT_DIR / 'table_II_panel_a.csv')
    table_II['panel_b'].to_csv(OUTPUT_DIR / 'table_II_panel_b.csv')

    # 4. Figure 1-2
    print("\n[4/6] Figure 1-2: 누적수익률 시각화...")
    global_val, global_mom, global_combo = replicate_figures_1_2(data)

    # 5. Table III-IV
    print("\n[5/6] Table III-IV: 매크로/유동성 리스크...")
    table_III_IV = replicate_table_III_IV(data, macro_data)
    print_table_III_IV(table_III_IV)

    # 6. Table V-VI
    print("\n[6/6] Table V-VI: 3-Factor 가격결정 모델...")
    table_V_VI = replicate_table_V_VI(data)
    print_table_V_VI(table_V_VI)

    # 7. Table VII
    print("\n[Bonus] Table VII: 강건성 검증...")
    table_VII = replicate_table_VII(data)
    print_table_VII(table_VII)

    print("\n" + "=" * 60)
    print("  재현 완료. 결과: " + str(OUTPUT_DIR))
    print("=" * 60)

    return {
        'table_I': table_I,
        'table_II': table_II,
        'table_V_VI': table_V_VI,
        'table_VII': table_VII,
        'global_factors': {'VAL': global_val, 'MOM': global_mom, 'COMBO': global_combo},
    }


# ============================================================
# 데모: 시뮬레이션 데이터로 테스트
# ============================================================
def generate_demo_data(n_months=480, n_assets=50, seed=42):
    """
    데모용 시뮬레이션 데이터 생성.
    실제 데이터 도착 전 코드 검증용.
    """
    np.random.seed(seed)
    dates = pd.date_range('1972-01-01', periods=n_months, freq='MS')
    assets = [f'asset_{i:03d}' for i in range(n_assets)]

    data = {}
    for ac in ASSET_CLASSES:
        # 랜덤 수익률 (value/momentum 프리미엄 내장)
        returns = pd.DataFrame(
            np.random.randn(n_months, n_assets) * 0.05,
            index=dates, columns=assets
        )

        # Value 시그널: 랜덤 + 약한 예측력
        sig_val = pd.DataFrame(
            np.random.randn(n_months, n_assets),
            index=dates, columns=assets
        )
        # 시그널에 따라 수익률에 약간의 예측력 부여
        returns += sig_val.shift(1) * 0.002

        # Momentum 시그널: 과거 12개월 수익률
        sig_mom = returns.rolling(12).sum().shift(1)
        # Momentum에도 약간의 예측력
        returns += sig_mom.shift(1).fillna(0) * 0.001

        # 시장 수익률
        mkt_ret = returns.mean(axis=1) + 0.005  # 양의 시장 프리미엄

        # 시가총액 (주식만)
        mkt_cap = None
        if ac in STOCK_CLASSES:
            mkt_cap = pd.DataFrame(
                np.random.lognormal(10, 2, (n_months, n_assets)),
                index=dates, columns=assets
            )

        data[ac] = {
            'returns': returns,
            'signals_value': sig_val,
            'signals_mom': sig_mom,
            'market_cap': mkt_cap,
            'market_return': mkt_ret,
        }

    return data


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        data_dir = sys.argv[1]
        run_all(data_dir)
    else:
        print("데이터 경로 미지정 — 시뮬레이션 데이터로 데모 실행\n")
        print("사용법: python vme_replication.py <data_dir>")
        print("       python vme_replication.py --demo\n")

        demo_data = generate_demo_data()

        # Table I만 빠르게 테스트
        print("[Demo] Table I 계산 중...")
        table_I = replicate_table_I(demo_data)
        print_table_I(table_I)

        print("\n[Demo] Table II 계산 중...")
        table_II = replicate_table_II(demo_data)
        print_table_II(table_II)

        print("\n[Demo] Figure 1-2 생성 중...")
        replicate_figures_1_2(demo_data)

        print("\n[Demo] Table V-VI 계산 중...")
        table_V_VI = replicate_table_V_VI(demo_data)
        print_table_V_VI(table_V_VI)

        print("\n[Demo] Table VII 계산 중...")
        table_VII = replicate_table_VII(demo_data)
        print_table_VII(table_VII)

        print("\n✓ 데모 완료. 실제 데이터가 오면 load_data()를 수정하세요.")
