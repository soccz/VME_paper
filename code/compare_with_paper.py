"""
논문 Table I 수치 vs 재현 수치 정밀 비교.
"""
import pandas as pd
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from load_aqr_data import load_all

ANNUALIZE = 12
PAPER_END = '2011-07-31'


def return_stats(r):
    r = r.dropna()
    n = len(r)
    if n < 12:
        return {k: np.nan for k in ['mean', 't_stat', 'stdev', 'sharpe']}
    mean_m = r.mean()
    std_m = r.std(ddof=1)
    return {
        'mean': mean_m * ANNUALIZE,
        't_stat': mean_m / (std_m / np.sqrt(n)),
        'stdev': std_m * np.sqrt(ANNUALIZE),
        'sharpe': (mean_m * ANNUALIZE) / (std_m * np.sqrt(ANNUALIZE)),
    }


# ============================================================
# 논문 Table I에서 직접 읽은 수치 (p.940-943)
# ============================================================
PAPER = {
    'us_stocks': {
        'period': '01/1972-07/2011',
        'val_P1': {'mean': 9.5, 't': 3.31, 'std': 17.9, 'sr': 0.53},
        'val_P2': {'mean': 10.6, 't': 4.33, 'std': 15.4, 'sr': 0.69},
        'val_P3': {'mean': 13.2, 't': 5.19, 'std': 15.9, 'sr': 0.83},
        'val_P3-P1': {'mean': 3.7, 't': 1.83, 'std': 12.8, 'sr': 0.29},
        'val_factor': {'mean': 3.9, 't': 1.66, 'std': 14.8, 'sr': 0.26},
        'mom_P1': {'mean': 8.8, 't': 2.96, 'std': 18.6, 'sr': 0.47},
        'mom_P2': {'mean': 9.7, 't': 4.14, 'std': 14.8, 'sr': 0.66},
        'mom_P3': {'mean': 14.2, 't': 4.82, 'std': 18.5, 'sr': 0.77},
        'mom_P3-P1': {'mean': 5.4, 't': 2.08, 'std': 16.4, 'sr': 0.33},
        'mom_factor': {'mean': 7.7, 't': 2.84, 'std': 17.0, 'sr': 0.45},
        'corr': -0.65,
        'combo_P3-P1': {'mean': 4.6, 'sr': 0.63},
        'combo_factor': {'mean': 5.8, 'sr': 0.86},
    },
    'uk_stocks': {
        'period': '01/1972-07/2011',
        'val_P3-P1': {'mean': 4.5, 't': 1.83, 'std': 13.4, 'sr': 0.33},
        'val_factor': {'mean': 5.5, 't': 2.10, 'std': 14.4, 'sr': 0.38},
        'mom_P3-P1': {'mean': 6.0, 't': 2.37, 'std': 15.9, 'sr': 0.38},
        'mom_factor': {'mean': 7.2, 't': 3.00, 'std': 15.0, 'sr': 0.48},
        'corr': -0.62,
    },
    'eu_stocks': {
        'period': '01/1974-07/2011',
        'val_P3-P1': {'mean': 4.8, 't': 2.32, 'std': 11.5, 'sr': 0.42},
        'val_factor': {'mean': 5.2, 't': 2.95, 'std': 9.7, 'sr': 0.54},
        'mom_P3-P1': {'mean': 8.1, 't': 3.37, 'std': 14.7, 'sr': 0.55},
        'mom_factor': {'mean': 9.8, 't': 4.59, 'std': 13.1, 'sr': 0.75},
        'corr': -0.54,
    },
    'jp_stocks': {
        'period': '01/1974-07/2011',
        'val_P3-P1': {'mean': 12.0, 't': 4.31, 'std': 15.3, 'sr': 0.79},
        'val_factor': {'mean': 10.2, 't': 4.22, 'std': 13.2, 'sr': 0.77},
        'mom_P3-P1': {'mean': 1.7, 't': 0.57, 'std': 18.6, 'sr': 0.09},
        'mom_factor': {'mean': 2.2, 't': 0.81, 'std': 16.5, 'sr': 0.13},
        'corr': -0.64,
    },
    'country_idx': {
        'period': '01/1978-07/2011',
        'val_P3-P1': {'mean': 6.0, 't': 3.45, 'std': 9.8, 'sr': 0.61},
        'val_factor': {'mean': 5.7, 't': 3.40, 'std': 9.5, 'sr': 0.60},
        'mom_P3-P1': {'mean': 8.7, 't': 4.14, 'std': 11.9, 'sr': 0.73},
        'mom_factor': {'mean': 7.4, 't': 3.57, 'std': 11.8, 'sr': 0.63},
        'corr': -0.42,
    },
    'currencies': {
        'period': '01/1979-07/2011',
        'val_P3-P1': {'mean': 3.3, 't': 1.89, 'std': 9.7, 'sr': 0.34},
        'val_factor': {'mean': 3.9, 't': 2.47, 'std': 9.0, 'sr': 0.44},
        'mom_P3-P1': {'mean': 3.5, 't': 1.90, 'std': 10.3, 'sr': 0.34},
        'mom_factor': {'mean': 3.0, 't': 1.77, 'std': 9.6, 'sr': 0.32},
        'corr': -0.43,
    },
    'fixed_income': {
        'period': '01/1982-07/2011',
        'val_P3-P1': {'mean': 1.1, 't': 0.97, 'std': 6.3, 'sr': 0.18},
        'val_factor': {'mean': 0.5, 't': 0.39, 'std': 6.4, 'sr': 0.07},
        'mom_P3-P1': {'mean': 0.4, 't': 0.35, 'std': 6.0, 'sr': 0.06},
        'mom_factor': {'mean': 1.0, 't': 0.88, 'std': 5.8, 'sr': 0.17},
        'corr': -0.08,
    },
    'commodities': {
        'period': '01/1972-07/2011',
        'val_P3-P1': {'mean': 6.3, 't': 1.61, 'std': 24.2, 'sr': 0.26},
        'val_factor': {'mean': 7.3, 't': 1.92, 'std': 23.7, 'sr': 0.31},
        'mom_P3-P1': {'mean': 12.4, 't': 3.29, 'std': 23.4, 'sr': 0.53},
        'mom_factor': {'mean': 11.5, 't': 3.14, 'std': 22.8, 'sr': 0.51},
        'corr': -0.35,
    },
}


def main():
    import os
    os.chdir(Path(__file__).parent.parent / 'data')
    data = load_all()

    print("\n" + "=" * 100)
    print("논문 Table I vs AQR 데이터 재현 — 정밀 비교")
    print("=" * 100)
    print("\n주의: 논문은 Total Return, AQR 데이터는 Excess Return → P1/P2/P3 수준 차이는 정상")
    print("      P3-P1 (long-short)과 Factor (zero-cost)는 일치해야 함\n")

    for ac in PAPER:
        if ac not in data['by_asset']:
            continue

        d = data['by_asset'][ac]
        paper = PAPER[ac]

        print(f"\n{'━'*100}")
        print(f"  {ac} (논문 기간: {paper['period']})")
        print(f"{'━'*100}")

        # 논문 기간에 맞게 자르기
        val_f = d['val_factor'][:PAPER_END]
        mom_f = d['mom_factor'][:PAPER_END]
        val_p = d['val_ports'][:PAPER_END]
        mom_p = d['mom_ports'][:PAPER_END]

        # 실제 데이터 기간
        vf_start = val_f.dropna().index[0].strftime('%m/%Y')
        vf_end = val_f.dropna().index[-1].strftime('%m/%Y')
        print(f"  AQR 데이터 실제 기간: {vf_start} ~ {vf_end}")

        if paper['period'].split('-')[0] != vf_start:
            print(f"  ⚠ 기간 불일치! 논문: {paper['period'].split('-')[0]}, AQR: {vf_start}")

        # Value P3-P1
        val_spread = val_p['P3'] - val_p['P1']
        mom_spread = mom_p['P3'] - mom_p['P1']

        print(f"\n  {'':30s} {'논문':>10s} {'재현':>10s} {'차이':>10s} {'판정':>6s}")
        print(f"  {'─'*70}")

        comparisons = [
            ('Val P3-P1 Mean', paper.get('val_P3-P1', {}).get('mean'), return_stats(val_spread)['mean'] * 100),
            ('Val P3-P1 t-stat', paper.get('val_P3-P1', {}).get('t'), return_stats(val_spread)['t_stat']),
            ('Val P3-P1 Sharpe', paper.get('val_P3-P1', {}).get('sr'), return_stats(val_spread)['sharpe']),
            ('Val Factor Mean', paper.get('val_factor', {}).get('mean'), return_stats(val_f)['mean'] * 100),
            ('Val Factor t-stat', paper.get('val_factor', {}).get('t'), return_stats(val_f)['t_stat']),
            ('Val Factor Sharpe', paper.get('val_factor', {}).get('sr'), return_stats(val_f)['sharpe']),
            ('Mom P3-P1 Mean', paper.get('mom_P3-P1', {}).get('mean'), return_stats(mom_spread)['mean'] * 100),
            ('Mom P3-P1 t-stat', paper.get('mom_P3-P1', {}).get('t'), return_stats(mom_spread)['t_stat']),
            ('Mom P3-P1 Sharpe', paper.get('mom_P3-P1', {}).get('sr'), return_stats(mom_spread)['sharpe']),
            ('Mom Factor Mean', paper.get('mom_factor', {}).get('mean'), return_stats(mom_f)['mean'] * 100),
            ('Mom Factor t-stat', paper.get('mom_factor', {}).get('t'), return_stats(mom_f)['t_stat']),
            ('Mom Factor Sharpe', paper.get('mom_factor', {}).get('sr'), return_stats(mom_f)['sharpe']),
            ('Corr(Val,Mom)', paper.get('corr'), val_f.dropna().index.intersection(mom_f.dropna().index).shape[0] > 0 and val_f.corr(mom_f)),
        ]

        for name, paper_val, repl_val in comparisons:
            if paper_val is None:
                continue
            diff = repl_val - paper_val if not np.isnan(repl_val) else np.nan

            # 판정 기준
            if 'Sharpe' in name or 'Corr' in name:
                ok = abs(diff) < 0.10
            elif 'Mean' in name:
                ok = abs(diff) < 1.5  # 1.5%p 이내
            elif 't-stat' in name:
                ok = abs(diff) < 0.5
            else:
                ok = abs(diff) < 0.5

            verdict = "✓" if ok else "✗"

            if 'Mean' in name:
                print(f"  {name:30s} {paper_val:9.1f}% {repl_val:9.1f}% {diff:+9.1f}%p {verdict:>6s}")
            elif 'Sharpe' in name or 'Corr' in name:
                print(f"  {name:30s} {paper_val:10.2f} {repl_val:10.2f} {diff:+10.2f} {verdict:>6s}")
            else:
                print(f"  {name:30s} {paper_val:10.2f} {repl_val:10.2f} {diff:+10.2f} {verdict:>6s}")

    # 총평
    print(f"\n{'='*100}")
    print("총평")
    print(f"{'='*100}")
    print("""
1. P3-P1 (long-short spread): 대체로 근접하나 일부 자산군에서 차이 존재
2. Factor (signal-weighted): 논문과 유사하나 AQR 업데이트 데이터로 인한 소폭 차이
3. 기간 불일치: UK/EU/JP 주식 — 논문은 1972/1974 시작, AQR 업데이트 데이터는 1981 시작
   → 이것이 가장 큰 차이 원인
4. P1/P2/P3 수준: 논문은 Total Return, AQR는 Excess Return → 수준 차이는 정상
5. Corr(Val,Mom): 대부분 근접 (±0.05 이내)

★ 해결책: Original Paper Data (VME_Original_Paper_Data.xlsx)를 사용하면 더 정확할 수 있음
  (다만 수식이 포함되어 있어 openpyxl로 값 계산 필요)
""")


if __name__ == '__main__':
    main()
