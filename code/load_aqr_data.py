"""
AQR 공개 데이터 로더 — Value and Momentum Everywhere 재현용.

AQR에서 제공하는 3개 파일:
1. VME_Factors_Monthly.xlsx  — 팩터 수익률 (시그널 가중 long-short)
2. VME_Portfolios_Monthly.xlsx — 48개 tercile 포트폴리오 수익률
3. VME_Original_Paper_Data.xlsx — 논문 원본 데이터 (1972-2011)
"""

import pandas as pd
import numpy as np
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / 'data'

# 자산군 매핑: AQR 코드 → 우리 코드
ASSET_MAP = {
    'US': 'us_stocks',
    'UK': 'uk_stocks',
    'EU': 'eu_stocks',  # ROE in factors file
    'JP': 'jp_stocks',
    'EQ': 'country_idx',
    'FX': 'currencies',
    'FI': 'fixed_income',
    'COM': 'commodities',
}

# Factors 파일의 컬럼명 매핑
FACTOR_COL_MAP = {
    'us_stocks':    ('VALLS_VME_US90', 'MOMLS_VME_US90'),
    'uk_stocks':    ('VALLS_VME_UK90', 'MOMLS_VME_UK90'),
    'eu_stocks':    ('VALLS_VME_ROE90', 'MOMLS_VME_ROE90'),
    'jp_stocks':    ('VALLS_VME_JP90', 'MOMLS_VME_JP90'),
    'country_idx':  ('VALLS_VME_EQ', 'MOMLS_VME_EQ'),
    'currencies':   ('VALLS_VME_FX', 'MOMLS_VME_FX'),
    'fixed_income': ('VALLS_VME_FI', 'MOMLS_VME_FI'),
    'commodities':  ('VALLS_VME_COM', 'MOMLS_VME_COM'),
}

# Portfolios 파일의 컬럼명 매핑 (VAL1XX, VAL2XX, VAL3XX, MOM1XX, MOM2XX, MOM3XX)
PORTFOLIO_COL_MAP = {
    'us_stocks':    {'val': ['VAL1US', 'VAL2US', 'VAL3US'], 'mom': ['MOM1US', 'MOM2US', 'MOM3US']},
    'uk_stocks':    {'val': ['VAL1UK', 'VAL2UK', 'VAL3UK'], 'mom': ['MOM1UK', 'MOM2UK', 'MOM3UK']},
    'eu_stocks':    {'val': ['VAL1EU', 'VAL2EU', 'VAL3EU'], 'mom': ['MOM1EU', 'MOM2EU', 'MOM3EU']},
    'jp_stocks':    {'val': ['VAL1JP', 'VAL2JP', 'VAL3JP'], 'mom': ['MOM1JP', 'MOM2JP', 'MOM3JP']},
    'country_idx':  {'val': ['VAL1_VME_EQ', 'VAL2_VME_EQ', 'VAL3_VME_EQ'], 'mom': ['MOM1_VME_EQ', 'MOM2_VME_EQ', 'MOM3_VME_EQ']},
    'currencies':   {'val': ['VAL1_VME_FX', 'VAL2_VME_FX', 'VAL3_VME_FX'], 'mom': ['MOM1_VME_FX', 'MOM2_VME_FX', 'MOM3_VME_FX']},
    'fixed_income': {'val': ['VAL1_VME_FI', 'VAL2_VME_FI', 'VAL3_VME_FI'], 'mom': ['MOM1_VME_FI', 'MOM2_VME_FI', 'MOM3_VME_FI']},
    'commodities':  {'val': ['VAL1_VME_COM', 'VAL2_VME_COM', 'VAL3_VME_COM'], 'mom': ['MOM1_VME_COM', 'MOM2_VME_COM', 'MOM3_VME_COM']},
}


def load_factors(filepath=None):
    """
    AQR VME Factors 로딩.

    Returns:
        DataFrame: DATE index, columns = [VAL^XX, MOM^XX, ...] (월간 초과수익률)
    """
    if filepath is None:
        filepath = DATA_DIR / 'VME_Factors_Monthly.xlsx'

    df = pd.read_excel(filepath, sheet_name='VME Factors', header=None)

    # 헤더 행 찾기 (DATE가 포함된 행)
    header_row = None
    for i in range(30):
        val = str(df.iloc[i, 0]).strip().upper()
        if val == 'DATE':
            header_row = i
            break

    if header_row is None:
        raise ValueError("헤더 행(DATE)을 찾을 수 없습니다")

    # 데이터 파싱
    df.columns = df.iloc[header_row]
    df = df.iloc[header_row + 1:].reset_index(drop=True)
    df = df.rename(columns={df.columns[0]: 'DATE'})

    # 날짜 파싱
    df['DATE'] = pd.to_datetime(df['DATE'])
    df = df.set_index('DATE')

    # 숫자 변환
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # 빈 행 제거
    df = df.dropna(how='all')

    print(f"[Factors] {len(df)} months loaded ({df.index[0].strftime('%Y-%m')} ~ {df.index[-1].strftime('%Y-%m')})")
    print(f"  Columns: {list(df.columns)}")

    return df


def load_portfolios(filepath=None):
    """
    AQR VME Portfolios 로딩 (48개 tercile 포트폴리오).

    Returns:
        DataFrame: DATE index, columns = [VAL1US, VAL2US, ..., MOM3COM]
    """
    if filepath is None:
        filepath = DATA_DIR / 'VME_Portfolios_Monthly.xlsx'

    df = pd.read_excel(filepath, sheet_name='VME Portfolios', header=None)

    # 헤더 행 찾기
    header_row = None
    for i in range(30):
        val = str(df.iloc[i, 0]).strip().lower()
        if val == 'date':
            header_row = i
            break

    if header_row is None:
        raise ValueError("헤더 행(Date)을 찾을 수 없습니다")

    df.columns = df.iloc[header_row]
    df = df.iloc[header_row + 1:].reset_index(drop=True)
    df = df.rename(columns={df.columns[0]: 'DATE'})

    df['DATE'] = pd.to_datetime(df['DATE'])
    df = df.set_index('DATE')

    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.dropna(how='all')

    print(f"[Portfolios] {len(df)} months loaded ({df.index[0].strftime('%Y-%m')} ~ {df.index[-1].strftime('%Y-%m')})")
    print(f"  48 portfolios: {list(df.columns)}")

    return df


def get_factor_returns(factors_df, asset_class):
    """특정 자산군의 value/momentum 팩터 수익률 추출."""
    val_col, mom_col = FACTOR_COL_MAP[asset_class]
    val = factors_df[val_col].dropna()
    mom = factors_df[mom_col].dropna()
    return val, mom


def get_portfolio_returns(portfolios_df, asset_class):
    """
    특정 자산군의 tercile 포트폴리오 수익률 추출.

    Returns:
        val_ports: DataFrame with columns [P1, P2, P3]
        mom_ports: DataFrame with columns [P1, P2, P3]
    """
    mapping = PORTFOLIO_COL_MAP[asset_class]

    val_cols = mapping['val']
    mom_cols = mapping['mom']

    val_ports = portfolios_df[val_cols].copy()
    val_ports.columns = ['P1', 'P2', 'P3']

    mom_ports = portfolios_df[mom_cols].copy()
    mom_ports.columns = ['P1', 'P2', 'P3']

    return val_ports.dropna(how='all'), mom_ports.dropna(how='all')


def get_global_factors(factors_df):
    """글로벌 팩터 (EVERYWHERE, ALL EQUITIES, ALL OTHER)."""
    return {
        'everywhere_val': factors_df['VAL'],
        'everywhere_mom': factors_df['MOM'],
        'all_stocks_val': factors_df['VAL^SS'],
        'all_stocks_mom': factors_df['MOM^SS'],
        'all_other_val': factors_df['VAL^AA'],
        'all_other_mom': factors_df['MOM^AA'],
    }


def load_all():
    """
    전체 데이터 로딩 후 분석에 편리한 구조로 반환.

    Returns:
        dict with keys:
            'factors_df': raw factors DataFrame
            'portfolios_df': raw portfolios DataFrame
            'by_asset': dict[asset_class] -> {val_factor, mom_factor, val_ports, mom_ports}
            'global': dict of global factors
    """
    factors_df = load_factors()
    portfolios_df = load_portfolios()

    by_asset = {}
    for ac in PORTFOLIO_COL_MAP:
        try:
            val_f, mom_f = get_factor_returns(factors_df, ac)
            val_p, mom_p = get_portfolio_returns(portfolios_df, ac)

            by_asset[ac] = {
                'val_factor': val_f,
                'mom_factor': mom_f,
                'val_ports': val_p,
                'mom_ports': mom_p,
            }
            n_val = len(val_f.dropna())
            n_mom = len(mom_f.dropna())
            print(f"  {ac:15s}: val={n_val} months, mom={n_mom} months")
        except KeyError as e:
            print(f"  [WARN] {ac}: 컬럼 없음 — {e}")

    global_factors = get_global_factors(factors_df)

    return {
        'factors_df': factors_df,
        'portfolios_df': portfolios_df,
        'by_asset': by_asset,
        'global': global_factors,
    }


if __name__ == '__main__':
    import os
    os.chdir(DATA_DIR)
    data = load_all()

    print(f"\n총 {len(data['by_asset'])}개 자산군 로딩 완료")

    # 샘플: US stocks value factor
    if 'us_stocks' in data['by_asset']:
        us = data['by_asset']['us_stocks']
        print(f"\nUS stocks Value factor 샘플:")
        print(us['val_factor'].head(10))
        print(f"\nUS stocks Value portfolios 샘플:")
        print(us['val_ports'].head(10))
