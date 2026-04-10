"""
AQR 공개 데이터로 Value and Momentum Everywhere 재현 실행.

사용법:
    python3 run_replication.py              # 전체 재현 (논문 기간: 1972-2011)
    python3 run_replication.py --extended    # 확장 기간 (2025년까지)
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import statsmodels.api as sm
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from load_aqr_data import load_all, PORTFOLIO_COL_MAP

OUTPUT_DIR = Path(__file__).parent / 'output'
OUTPUT_DIR.mkdir(exist_ok=True)

ANNUALIZE = 12

ASSET_CLASSES = list(PORTFOLIO_COL_MAP.keys())
STOCK_CLASSES = ['us_stocks', 'uk_stocks', 'eu_stocks', 'jp_stocks']
NONSTOCK_CLASSES = ['country_idx', 'currencies', 'fixed_income', 'commodities']

ASSET_LABELS = {
    'us_stocks': 'U.S. stocks',
    'uk_stocks': 'U.K. stocks',
    'eu_stocks': 'Europe stocks',
    'jp_stocks': 'Japan stocks',
    'country_idx': 'Country indices',
    'currencies': 'Currencies',
    'fixed_income': 'Fixed income',
    'commodities': 'Commodities',
}

# 논문 원본 기간
PAPER_END = '2011-07-31'


# ============================================================
# 통계 함수
# ============================================================
def return_stats(r):
    """월간 수익률 → 연율화 통계."""
    r = r.dropna()
    n = len(r)
    if n < 12:
        return {k: np.nan for k in ['mean', 't_stat', 'stdev', 'sharpe']}

    mean_m = r.mean()
    std_m = r.std(ddof=1)
    mean_ann = mean_m * ANNUALIZE
    std_ann = std_m * np.sqrt(ANNUALIZE)
    t_stat = mean_m / (std_m / np.sqrt(n))
    sharpe = mean_ann / std_ann if std_ann > 0 else np.nan

    return {'mean': mean_ann, 't_stat': t_stat, 'stdev': std_ann, 'sharpe': sharpe}


def compute_alpha(r, benchmark):
    """시장 벤치마크 대비 alpha (HAC t-stat)."""
    r = r.dropna()
    common = r.index.intersection(benchmark.dropna().index)
    if len(common) < 24:
        return np.nan, np.nan

    y = r[common]
    X = sm.add_constant(benchmark[common])
    reg = sm.OLS(y, X).fit(cov_type='HAC', cov_kwds={'maxlags': 6})
    alpha = reg.params.iloc[0] * ANNUALIZE
    alpha_t = reg.tvalues.iloc[0]
    return alpha, alpha_t


# ============================================================
# Table I: 수익률 통계
# ============================================================
def replicate_table_I(data, end_date=None):
    """Table I 재현."""
    print("\n" + "=" * 110)
    print("TABLE I: Performance of Value and Momentum Portfolios across Markets and Asset Classes")
    print("=" * 110)

    all_rows = []

    for ac in ASSET_CLASSES:
        if ac not in data['by_asset']:
            continue

        d = data['by_asset'][ac]
        val_p = d['val_ports']
        mom_p = d['mom_ports']
        val_f = d['val_factor']
        mom_f = d['mom_factor']

        if end_date:
            val_p = val_p[:end_date]
            mom_p = mom_p[:end_date]
            val_f = val_f[:end_date]
            mom_f = mom_f[:end_date]

        # P3-P1 spread
        val_spread = val_p['P3'] - val_p['P1']
        mom_spread = mom_p['P3'] - mom_p['P1']

        # 50/50 Combo
        combo_spread = 0.5 * val_spread + 0.5 * mom_spread
        combo_factor = 0.5 * val_f + 0.5 * mom_f

        # Corr(Val, Mom)
        common = val_f.dropna().index.intersection(mom_f.dropna().index)
        corr_vm = val_f[common].corr(mom_f[common])

        # Benchmark = 동일가중 평균 (P1+P2+P3)/3
        benchmark = (val_p['P1'] + val_p['P2'] + val_p['P3']) / 3

        # 통계 출력
        label = ASSET_LABELS.get(ac, ac)
        period_start = val_p.dropna(how='all').index[0].strftime('%m/%Y')
        period_end = val_p.dropna(how='all').index[-1].strftime('%m/%Y')

        print(f"\n{'─'*110}")
        print(f"  {label} ({period_start} to {period_end})")
        print(f"{'─'*110}")

        for strategy, ports, spread, factor, sname in [
            ('Value', val_p, val_spread, val_f, 'val'),
            ('Momentum', mom_p, mom_spread, mom_f, 'mom'),
        ]:
            stats_list = []
            for s in [ports['P1'], ports['P2'], ports['P3'], spread, factor]:
                st = return_stats(s)
                a, at = compute_alpha(s, benchmark)
                st['alpha'] = a
                st['alpha_tstat'] = at
                stats_list.append(st)

            print(f"\n  {strategy} Portfolios:")
            _print_stats_row('Mean', stats_list, 'mean', pct=True)
            _print_stats_row('(t-stat)', stats_list, 't_stat', fmt='({:5.2f})')
            _print_stats_row('Stdev', stats_list, 'stdev', pct=True)
            _print_stats_row('Sharpe', stats_list, 'sharpe', fmt='{:7.2f}')
            _print_stats_row('Alpha', stats_list, 'alpha', pct=True)
            _print_stats_row('(t-stat)', stats_list, 'alpha_tstat', fmt='({:5.2f})')

        # Combo
        combo_s_stats = return_stats(combo_spread)
        combo_f_stats = return_stats(combo_factor)
        print(f"\n  50/50 Combination:")
        print(f"  {'':20s} {'':>8s} {'':>8s} {'':>8s} {'P3-P1':>8s} {'Factor':>8s}")
        print(f"  {'Mean':20s} {'':>8s} {'':>8s} {'':>8s} {combo_s_stats['mean']:7.1%} {combo_f_stats['mean']:7.1%}")
        print(f"  {'Sharpe':20s} {'':>8s} {'':>8s} {'':>8s} {combo_s_stats['sharpe']:7.2f} {combo_f_stats['sharpe']:7.2f}")
        print(f"  Corr(Val, Mom) = {corr_vm:.2f}")

        all_rows.append({
            'asset_class': ac,
            'val_sharpe': return_stats(val_f)['sharpe'],
            'mom_sharpe': return_stats(mom_f)['sharpe'],
            'combo_sharpe': combo_f_stats['sharpe'],
            'corr_vm': corr_vm,
        })

    return pd.DataFrame(all_rows)


def _print_stats_row(label, stats_list, key, pct=False, fmt=None):
    """Table I 행 출력 헬퍼."""
    header = f"{'P1':>8s} {'P2':>8s} {'P3':>8s} {'P3-P1':>8s} {'Factor':>8s}"
    if label == 'Mean':
        print(f"  {'':20s} {header}")

    vals = [s.get(key, np.nan) for s in stats_list]
    print(f"  {label:20s}", end='')
    for v in vals:
        if np.isnan(v):
            print(f" {'N/A':>7s}", end='')
        elif pct:
            print(f" {v:7.1%}", end='')
        elif fmt:
            print(f" {fmt.format(v):>7s}", end='')
        else:
            print(f" {v:7.2f}", end='')
    print()


# ============================================================
# Table II: Comovement
# ============================================================
def replicate_table_II(data, end_date=None):
    """Table II 재현: 자산군 간 Value/Momentum 상관관계."""
    print("\n" + "=" * 80)
    print("TABLE II: Correlation of Value and Momentum across Asset Classes")
    print("=" * 80)

    # Panel A: 주식 평균 vs 비주식 평균
    stock_val = []
    stock_mom = []
    nonstock_val = []
    nonstock_mom = []

    for ac in ASSET_CLASSES:
        if ac not in data['by_asset']:
            continue
        d = data['by_asset'][ac]
        vf = d['val_factor'][:end_date] if end_date else d['val_factor']
        mf = d['mom_factor'][:end_date] if end_date else d['mom_factor']

        if ac in STOCK_CLASSES:
            stock_val.append(vf)
            stock_mom.append(mf)
        else:
            nonstock_val.append(vf)
            nonstock_mom.append(mf)

    panel_a_data = {
        'Stock Value': pd.concat(stock_val, axis=1).mean(axis=1),
        'Nonstock Value': pd.concat(nonstock_val, axis=1).mean(axis=1),
        'Stock Momentum': pd.concat(stock_mom, axis=1).mean(axis=1),
        'Nonstock Momentum': pd.concat(nonstock_mom, axis=1).mean(axis=1),
    }
    panel_a = pd.DataFrame(panel_a_data).corr()

    print("\nPanel A: Correlation of Average Return Series")
    print(panel_a.round(2).to_string())

    # Panel B: 개별 자산군 간
    all_series = {}
    for ac in ASSET_CLASSES:
        if ac not in data['by_asset']:
            continue
        d = data['by_asset'][ac]
        label = ASSET_LABELS[ac].split()[0]  # 짧은 이름
        vf = d['val_factor'][:end_date] if end_date else d['val_factor']
        mf = d['mom_factor'][:end_date] if end_date else d['mom_factor']
        all_series[f'{label} Val'] = vf
        all_series[f'{label} Mom'] = mf

    panel_b = pd.DataFrame(all_series).corr()

    # Value 간, Momentum 간, Value-Momentum 간 평균 상관계수 요약
    val_cols = [c for c in panel_b.columns if 'Val' in c]
    mom_cols = [c for c in panel_b.columns if 'Mom' in c]

    val_val_corrs = []
    mom_mom_corrs = []
    val_mom_corrs = []

    for i, c1 in enumerate(val_cols):
        for j, c2 in enumerate(val_cols):
            if i < j:
                val_val_corrs.append(panel_b.loc[c1, c2])
        for c2 in mom_cols:
            val_mom_corrs.append(panel_b.loc[c1, c2])

    for i, c1 in enumerate(mom_cols):
        for j, c2 in enumerate(mom_cols):
            if i < j:
                mom_mom_corrs.append(panel_b.loc[c1, c2])

    print(f"\n요약 상관관계:")
    print(f"  Value-Value 평균:    {np.mean(val_val_corrs):.3f}")
    print(f"  Mom-Mom 평균:        {np.mean(mom_mom_corrs):.3f}")
    print(f"  Value-Mom 평균:      {np.mean(val_mom_corrs):.3f}")

    return {'panel_a': panel_a, 'panel_b': panel_b}


# ============================================================
# Figure 1-2: 누적수익률
# ============================================================
def replicate_figures(data, end_date=None):
    """Figure 1 (자산군별) + Figure 2 (글로벌) 누적수익률."""

    # --- Figure 1: 자산군별 ---
    fig1, axes = plt.subplots(2, 4, figsize=(20, 10))
    fig1.suptitle('Figure 1: Cumulative Excess Returns — Value, Momentum, Combo',
                  fontsize=14, fontweight='bold')

    for idx, ac in enumerate(ASSET_CLASSES):
        if ac not in data['by_asset']:
            continue
        ax = axes[idx // 4, idx % 4]
        d = data['by_asset'][ac]

        vf = d['val_factor'][:end_date] if end_date else d['val_factor']
        mf = d['mom_factor'][:end_date] if end_date else d['mom_factor']
        cf = 0.5 * vf + 0.5 * mf

        for series, label, color, ls in [
            (vf, 'Value', '#1f77b4', '-'),
            (mf, 'Momentum', '#d62728', '-'),
            (cf, 'Combo', '#2ca02c', '--'),
        ]:
            s = series.dropna()
            cum = (1 + s).cumprod()
            ax.plot(cum.index, cum.values, label=label, color=color, linestyle=ls, linewidth=1.2)

        ax.set_title(ASSET_LABELS.get(ac, ac), fontsize=11)
        ax.set_yscale('log')
        ax.legend(fontsize=8, loc='upper left')
        ax.grid(True, alpha=0.3)
        ax.xaxis.set_major_locator(mdates.YearLocator(10))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    fig1.tight_layout()
    fig1.savefig(OUTPUT_DIR / 'figure1_cumulative_by_asset.png', dpi=150, bbox_inches='tight')
    print(f"[Figure 1] saved: {OUTPUT_DIR / 'figure1_cumulative_by_asset.png'}")

    # --- Figure 2: 글로벌 ---
    fig2, ax = plt.subplots(figsize=(14, 7))

    # 글로벌 팩터는 AQR이 이미 계산 (VAL, MOM columns)
    gf = data['global']
    gval = gf['everywhere_val'][:end_date] if end_date else gf['everywhere_val']
    gmom = gf['everywhere_mom'][:end_date] if end_date else gf['everywhere_mom']
    gcombo = 0.5 * gval + 0.5 * gmom

    for series, label, color, ls in [
        (gval, 'Global Value', '#1f77b4', '-'),
        (gmom, 'Global Momentum', '#d62728', '-'),
        (gcombo, 'Global Combo (50/50)', '#2ca02c', '--'),
    ]:
        s = series.dropna()
        cum = (1 + s).cumprod()
        ax.plot(cum.index, cum.values, label=label, color=color, linestyle=ls, linewidth=2)

    ax.set_yscale('log')
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.set_ylabel('Cumulative Excess Return ($1 invested)', fontsize=12)
    ax.set_title('Figure 2: Global Value, Momentum, and Combo — Cumulative Returns',
                 fontsize=14, fontweight='bold')
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    fig2.tight_layout()
    fig2.savefig(OUTPUT_DIR / 'figure2_cumulative_global.png', dpi=150, bbox_inches='tight')
    print(f"[Figure 2] saved: {OUTPUT_DIR / 'figure2_cumulative_global.png'}")

    plt.close('all')


# ============================================================
# Table V-VI: 3-Factor 가격결정 모델
# ============================================================
def replicate_table_V_VI(data, end_date=None):
    """3-Factor 모델로 48개 포트폴리오 가격결정."""
    print("\n" + "=" * 95)
    print("TABLE V-VI: Three-Factor Pricing Model (MKT + VAL + MOM)")
    print("=" * 95)

    gf = data['global']
    global_val = gf['everywhere_val'][:end_date] if end_date else gf['everywhere_val']
    global_mom = gf['everywhere_mom'][:end_date] if end_date else gf['everywhere_mom']

    # 시장 벤치마크: 각 자산군 포트폴리오 평균
    portfolios_df = data['portfolios_df'][:end_date] if end_date else data['portfolios_df']
    global_mkt = portfolios_df.mean(axis=1)  # 단순 평균 (근사)

    factors = pd.DataFrame({
        'MKT': global_mkt,
        'VAL': global_val,
        'MOM': global_mom,
    }).dropna()

    print(f"\nFactors period: {factors.index[0].strftime('%Y-%m')} ~ {factors.index[-1].strftime('%Y-%m')}")
    print(f"{'Portfolio':30s} {'Alpha':>8s} {'t(α)':>8s} {'β_MKT':>8s} {'β_VAL':>8s} {'β_MOM':>8s} {'R²':>8s}")
    print("─" * 95)

    alphas_list = []

    for ac in ASSET_CLASSES:
        if ac not in data['by_asset']:
            continue
        d = data['by_asset'][ac]
        label = ASSET_LABELS[ac]

        for strat, ports in [('Val', d['val_ports']), ('Mom', d['mom_ports'])]:
            ports_cut = ports[:end_date] if end_date else ports
            for p in ['P1', 'P2', 'P3']:
                port_ret = ports_cut[p].dropna()
                common = port_ret.index.intersection(factors.index)
                if len(common) < 24:
                    continue

                y = port_ret[common]
                X = sm.add_constant(factors.loc[common])
                reg = sm.OLS(y, X).fit(cov_type='HAC', cov_kwds={'maxlags': 6})

                name = f"{label} {strat} {p}"
                alpha_ann = reg.params['const'] * ANNUALIZE
                alpha_t = reg.tvalues['const']

                print(f"  {name:30s} {alpha_ann:7.1%} {alpha_t:8.2f} "
                      f"{reg.params['MKT']:8.2f} {reg.params['VAL']:8.2f} "
                      f"{reg.params['MOM']:8.2f} {reg.rsquared:8.3f}")

                alphas_list.append({
                    'name': name, 'alpha': alpha_ann, 'alpha_t': alpha_t,
                    'r_squared': reg.rsquared,
                })

    df_alphas = pd.DataFrame(alphas_list)
    if len(df_alphas) > 0:
        sig_count = (df_alphas['alpha_t'].abs() > 1.96).sum()
        print(f"\n  유의한 alpha 개수 (|t|>1.96): {sig_count} / {len(df_alphas)}")
        print(f"  평균 |alpha|: {df_alphas['alpha'].abs().mean():.1%}")
        print(f"  평균 R²: {df_alphas['r_squared'].mean():.3f}")

    return df_alphas


# ============================================================
# Table VII: 강건성 검증
# ============================================================
def replicate_table_VII(data, end_date=None):
    """하위기간, 1월 제외 등 강건성 검증."""
    print("\n" + "=" * 90)
    print("TABLE VII: Robustness — Sharpe Ratios across Subperiods")
    print("=" * 90)

    print(f"\n{'Asset Class':20s} {'Full':>8s} {'1st Half':>9s} {'2nd Half':>9s} {'Ex-Jan':>8s}")
    print("─" * 60)

    for ac in ASSET_CLASSES:
        if ac not in data['by_asset']:
            continue

        d = data['by_asset'][ac]
        label = ASSET_LABELS[ac]

        for strat, factor in [('Val', d['val_factor']), ('Mom', d['mom_factor'])]:
            f = factor[:end_date] if end_date else factor
            f = f.dropna()

            # Full
            full_sr = return_stats(f)['sharpe']

            # 1st/2nd half
            mid = f.index[len(f) // 2]
            first_sr = return_stats(f[:mid])['sharpe']
            second_sr = return_stats(f[mid:])['sharpe']

            # Excluding January
            no_jan = f[f.index.month != 1]
            exjan_sr = return_stats(no_jan)['sharpe']

            print(f"  {label + ' ' + strat:20s} {full_sr:8.2f} {first_sr:9.2f} {second_sr:9.2f} {exjan_sr:8.2f}")

        # Combo
        vf = d['val_factor'][:end_date] if end_date else d['val_factor']
        mf = d['mom_factor'][:end_date] if end_date else d['mom_factor']
        combo = (0.5 * vf + 0.5 * mf).dropna()
        combo_sr = return_stats(combo)['sharpe']
        print(f"  {label + ' Combo':20s} {combo_sr:8.2f}")


# ============================================================
# 추가: 논문 vs 확장 기간 비교
# ============================================================
def compare_periods(data):
    """논문 기간(~2011) vs 확장 기간(~2025) Sharpe 비교."""
    print("\n" + "=" * 80)
    print("BONUS: Paper Period (to 2011) vs Extended Period (to 2025)")
    print("=" * 80)

    print(f"\n{'Asset Class':20s} {'Val (Paper)':>12s} {'Val (Ext)':>10s} {'Mom (Paper)':>12s} {'Mom (Ext)':>10s}")
    print("─" * 70)

    for ac in ASSET_CLASSES:
        if ac not in data['by_asset']:
            continue
        d = data['by_asset'][ac]
        label = ASSET_LABELS[ac]

        vf_paper = return_stats(d['val_factor'][:PAPER_END])['sharpe']
        vf_ext = return_stats(d['val_factor'])['sharpe']
        mf_paper = return_stats(d['mom_factor'][:PAPER_END])['sharpe']
        mf_ext = return_stats(d['mom_factor'])['sharpe']

        print(f"  {label:20s} {vf_paper:12.2f} {vf_ext:10.2f} {mf_paper:12.2f} {mf_ext:10.2f}")


# ============================================================
# Main
# ============================================================
def main():
    extended = '--extended' in sys.argv

    print("=" * 60)
    print("  Value and Momentum Everywhere — AQR Data Replication")
    print("  Asness, Moskowitz, Pedersen (2013)")
    print("=" * 60)

    # 데이터 로딩
    data = load_all()

    end_date = None if extended else PAPER_END
    period_label = "Extended (to 2025)" if extended else f"Paper period (to {PAPER_END[:7]})"
    print(f"\n분석 기간: {period_label}")

    # Table I
    table_I = replicate_table_I(data, end_date)

    # Table II
    table_II = replicate_table_II(data, end_date)

    # Figure 1-2
    replicate_figures(data, end_date)

    # Table V-VI
    table_V_VI = replicate_table_V_VI(data, end_date)

    # Table VII
    replicate_table_VII(data, end_date)

    # 논문 vs 확장 비교
    if not extended:
        compare_periods(data)

    print("\n" + "=" * 60)
    print(f"  완료. 그래프: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == '__main__':
    main()
