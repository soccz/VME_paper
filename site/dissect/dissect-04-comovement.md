# 논문 해체: C. Comovement across Asset Classes (p.947~955)

> Section II의 마지막 파트다. 여기까지 논문은 "가치와 모멘텀이 각 자산군에서 돈을 번다"를 보여줬다. 이제 한 단계 더 나간다 — **서로 다른 자산군의 전략들이 함께 움직이는가?** 이것이 "공통 팩터"의 존재 여부를 결정하는 핵심 증거다. Table II, Figure 1, Figure 2를 모두 빠짐없이 뜯는다.

---

## 섹션 도입 (p.947 하단)

> *C. Comovement across Asset Classes*

### 뜯기

**Comovement** = 공동 움직임. 두 개 이상의 수익률 시리즈가 **같이 오르거나 같이 내리는** 경향. 통계적으로는 **상관(correlation)**으로 측정한다.

"across Asset Classes"가 중요하다. 같은 자산군 안에서(예: 미국 주식끼리) 함께 움직이는 건 놀랍지 않다 — 같은 경제 환경, 같은 투자자들이니까. 하지만 **미국 주식의 가치 전략**과 **원자재의 가치 전략**이 함께 움직인다? 이건 놀라운 일이다. 다른 투자자, 다른 정보, 다른 시장 구조인데 왜 같이 움직이는가?

---

## Table II 도입 문장 (p.947)

> "Table II reports the correlations of value and momentum returns across diverse asset classes to identify their common movements."

### 뜯기

- **"correlations"** = 상관계수. -1에서 +1 사이의 숫자. +1이면 완벽하게 같은 방향, -1이면 완벽하게 반대 방향, 0이면 관계 없음.
- **"to identify their common movements"** = 공통 움직임을 식별하기 위해. Table II의 목적이 명확하다: 전략들 사이에 공통 요인이 있는지 상관을 통해 확인하겠다.

> "The strength of comovement may support or challenge various theoretical explanations for value and momentum, and may ultimately point to underlying economic drivers for their returns."

### 뜯기

왜 상관을 보는가? 두 가지 이론적 함의 때문이다:

1. **공통 움직임이 강하면** → 전 세계적으로 작용하는 **하나의 원인**이 존재한다는 증거. 이것은 "글로벌 위험 팩터"를 지지한다.
2. **공통 움직임이 약하면** → 각 시장의 **개별적 원인**(로컬 행동 편향, 시장 미시구조 등)이 독립적으로 작용한다는 증거.

결과를 미리 말하면: 공통 움직임이 **매우 강하다**. 이것이 Section III에서 글로벌 3팩터 모형을 제안하는 근거가 된다.

---

## 상관 계산법 (p.949)

> "The correlations are computed from the returns of the signal-weighted zero-cost factor portfolios from equation (2), but results are similar using the top third minus bottom third P3-P1 portfolio returns."

### 뜯기

상관을 계산하는 데 사용한 수익률의 출처:

- **signal-weighted zero-cost factor portfolios** = 시그널 가중 무비용 팩터 포트폴리오. [dissect-02](dissect-02-data.md)에서 다룬 equation (2)의 방식. 각 자산의 시그널(BE/ME 또는 과거수익률)에 비례하여 가중치를 주고, 롱-숏으로 구성한 제로코스트 포트폴리오.
- **P3-P1** = 상위 1/3 매수 - 하위 1/3 매도. 더 단순한 방식이지만 결과가 비슷하다고 확인.

> "Panel A of Table II reports the correlations among value strategies and among momentum strategies globally across asset markets."

### 뜯기

Panel A의 구조: 주식 전체(4개국)를 한 그룹, 비주식(국가지수/통화/채권/원자재)을 한 그룹으로 묶어서 **그룹 간** 상관을 본다.

> "We first compute the average return series for value and momentum across all stock markets and across all nonstock asset classes separately."

### 뜯기

핵심 방법론: **개별 전략의 수익률을 먼저 평균 낸 뒤** 상관을 계산한다.

왜 이렇게 하는가? 개별 전략(예: 미국 가치)은 노이즈가 크다. 4개국 가치를 평균 내면 각 국가 고유의 노이즈가 상쇄되고, **공통 신호만 남는다**. 이것이 논문 전반에 걸쳐 반복되는 "평균 낸 뒤 상관 = 더 강한 통계적 발견" 원리다.

> "For example, we compute the volatility-weighted average of all the individual stock value strategies across the four equity markets — the United States, the United Kingdom, Europe, and Japan — and the weighted average of the value strategies across the nonequity asset classes — index futures, currencies, bonds, and commodities."

### 뜯기

구체적 절차:

1. 주식 가치: US value, UK value, Europe value, Japan value → **변동성 가중 평균** → "Stock Value" 시리즈 1개
2. 비주식 가치: Country index value, Currency value, FI value, Commodity value → **변동성 가중 평균** → "Nonstock Value" 시리즈 1개
3. 모멘텀도 동일하게 → "Stock Momentum", "Nonstock Momentum" 각 1개

이렇게 4개의 평균 수익률 시리즈를 만든 뒤, 이들 간의 상관 매트릭스를 계산한 것이 Panel A다.

> "We do the same for momentum. We then compute the correlation matrix between these average return series."

### 뜯기

4개 시리즈 간 4x4 상관 매트릭스. 대각선은 자기 자신과의 상관이 아니라 특별한 방식으로 계산된다 — 아래에서 설명.

> "The diagonal of the correlation matrix is computed as the average correlation between each individual market's return series and the average of all *other* return series in other markets."

### 뜯기

대각선이 1.0이 아니다! 보통 상관 매트릭스의 대각선은 자기 자신과의 상관이므로 1인데, 여기서는 다르다.

대각선의 의미: **같은 그룹 내 개별 전략들이 서로 얼마나 상관되는가**의 평균.

예를 들어 "Stock Value" 대각선(0.68):
- US value vs (UK+Europe+Japan) value의 평균 상관
- UK value vs (US+Europe+Japan) value의 평균 상관
- Europe value vs (US+UK+Japan) value의 평균 상관
- Japan value vs (US+UK+Europe) value의 평균 상관
- 이 4개의 평균 = **0.68**

> "For instance, the first entry in the covariance matrix is the average of the correlations between each equity market's value strategy and a portfolio of all other equity market value strategies: an average of the correlation of U.S. value with a diversified value strategy in all other individual equity markets (United Kingdom, Europe, and Japan); the correlation of U.K. value with a diversified value strategy in the United States, Europe, and Japan; the correlation of Europe value with a diversified value strategy in the United States, the United Kingdom, and Japan; and the correlation of Japan value with a diversified value strategy in the United States, United Kingdom, and Europe."

### 뜯기

위에서 설명한 것을 논문이 매우 상세하게 풀어쓰고 있다. 각 국가의 가치 전략과 **나머지 모든 국가의 가치 전략 포트폴리오** 간 상관을 각각 구하고, 그 평균을 취한다.

왜 이렇게 복잡하게? **자기 자신과의 상관(=1)을 제외**하면서도, **그룹 내 공통 변동의 강도**를 측정하기 위해서다. 0.68이라는 숫자는 "4개국 주식 가치 전략들이 서로 68% 정도 같이 움직인다"는 뜻이다.

> "We then take an equal weighted average of these four correlations to get the first element of the correlation matrix in Panel A of Table II."

### 뜯기

4개 상관의 단순 평균 = Panel A 첫 번째 요소 = **0.68***.

> "In general, we obtain more powerful statistical findings when looking at the correlations of the average return series rather than the average of individual correlations, since the former better diversifies away random noise from each market, a theme we emphasize throughout the paper."

### 뜯기

이 문장은 논문의 **방법론적 핵심 원칙**을 재확인한다:

- 방법 A: 개별 상관을 각각 구한 뒤 평균 → 노이즈 많음
- 방법 B: 수익률을 먼저 평균 낸 뒤 상관 구함 → 노이즈 적음 (논문이 택한 방법)

왜? 평균 내는 과정에서 각 시장의 **고유 노이즈가 상쇄**되기 때문이다. 8개 라디오로 같은 방송을 들으면 잡음은 줄고 신호는 선명해지는 원리와 같다.

> "Correlations are computed from quarterly returns to help mitigate any nonsynchronous trading issues across markets, due to illiquid assets that do not trade continuously or time zone differences."

### 뜯기

상관 계산에 **분기별(quarterly)** 수익률을 사용한다. 왜 월별이 아니라 분기별인가?

두 가지 문제를 해결하기 위해:

1. **비동시 거래(nonsynchronous trading)**: 일본 시장은 아시아 시간에, 미국은 뉴욕 시간에 닫는다. 같은 "월"이라도 실제 거래 시점이 다르므로, 월별 수익률로 상관을 구하면 **진짜 상관이 과소 측정**될 수 있다. 분기로 늘리면 이 시차의 영향이 줄어든다.

2. **비유동 자산**: 채권이나 일부 원자재는 매일 거래되지 않는다. 가격이 며칠 "정체"했다가 한꺼번에 움직일 수 있어서, 월별 수익률이 실제 가치 변동을 제대로 반영하지 못할 수 있다. 분기로 늘리면 이 문제가 완화된다.

> "An *F*-test on the joint significance of the correlations is also performed."

### 뜯기

**F-test** = 상관 매트릭스의 모든 비대각선 요소가 **동시에** 0인가를 검정하는 통계적 검정.

개별 상관 하나하나가 유의한지 보는 것보다, **전체가 동시에 0이다**라는 귀무가설을 기각하는 것이 더 강력한 증거다. "*" 표시가 그 결과를 나타낸다 — 5% 유의수준에서 유의하게 0과 다르다는 뜻.

---

### 각주 15 (p.949)

> <sup>15</sup> "In the Internet Appendix to the paper, we report the average of the individual correlations among the stock and nonstock value and momentum strategies, where we first compute the pairwise correlations of all individual strategies (e.g., U.S. value with Japan value) and then take the average for each group."

### 뜯기

Internet Appendix에는 **개별 쌍별(pairwise) 상관**의 평균도 보고한다. 본문의 방법(평균 수익률 간 상관)과는 다른 접근이다.

> "We exclude the correlation of each strategy with itself (removing the 1s) when averaging and also exclude the correlation of each strategy with all other strategies within the same market (i.e., exclude U.S. momentum when examining U.S. value's correlation with other momentum strategies)."

### 뜯기

두 가지를 제외한다:
1. **자기 자신과의 상관(1)** — 당연히 제외
2. **같은 시장 내 다른 전략과의 상관** — 예를 들어 US value와 US momentum의 상관은 제외. 왜? 같은 시장 안에서의 상관은 **시장 자체의 움직임**에 의해 기계적으로 발생할 수 있기 때문. **다른 시장의 전략**과의 상관만 봐야 진짜 "cross-asset comovement"을 측정할 수 있다.

> "While these individual correlations are consistently weaker than those obtained from taking averages first and then computing correlations, the average pairwise correlations also exhibit strong comovement among value and momentum across markets."

### 뜯기

개별 쌍별 상관은 평균 수익률 간 상관보다 **일관되게 약하다**. 이건 예상 가능한 결과다 — 개별 상관에는 노이즈가 더 많으니까. 하지만 약하더라도 **같은 패턴**(가치끼리 양, 모멘텀끼리 양, 가치-모멘텀 음)은 동일하게 나타난다. 결론의 강건성을 확인해 주는 것이다.

---

## Table II Panel A: 전략 그룹 간 상관 매트릭스 (p.948)

> **Table II**
> **Correlation of Value and Momentum Strategies across Markets and Asset Classes**

> *Panel A. Correlation of Average Return Series*

### 뜯기

Panel A는 **4x4 매트릭스**다. 행과 열은 동일하게:
1. Stock Value (주식 가치)
2. Nonstock Value (비주식 가치)
3. Stock Momentum (주식 모멘텀)
4. Nonstock Momentum (비주식 모멘텀)

매트릭스를 완전히 펼치면:

|  | Stock Value | Nonstock Value | Stock Momentum | Nonstock Momentum |
|--|-------------|----------------|----------------|-------------------|
| **Stock value** | **0.68*** | | | |
| **Nonstock value** | 0.15* | **0.07** | | |
| **Stock momentum** | -0.53* | -0.16* | **0.65*** | |
| **Nonstock momentum** | -0.26* | -0.13 | 0.37* | **0.21*** |

(하삼각 행렬 — 상삼각은 대칭이므로 생략)

그리고 마지막 2행:

|  | Stock Value | Nonstock Value | Stock Momentum | Nonstock Momentum |
|--|-------------|----------------|----------------|-------------------|
| **Global Stock value** | | | | |
| **Global Stock momentum** | | | | |

이 행들은 별도 계산으로, 글로벌 주식 팩터와 각 그룹의 상관을 보여준다:

| | Stock Value | Nonstock Value | Stock Momentum | Nonstock Momentum |
|--|-------------|----------------|----------------|-------------------|
| **Global Stock value** | 0.27* | | -0.19* | |
| **Global Stock momentum** | -0.28* | | 0.40* | |

이제 이 숫자들을 하나씩 뜯는다.

---

### 대각선: 같은 전략 그룹 내부의 상관

**Stock Value 대각선: 0.68***

4개국 주식 가치 전략들이 서로 68%의 상관을 보인다. 이건 **매우 높다**. 미국에서 가치가 잘 되는 분기에 일본에서도 가치가 잘 될 확률이 높다는 뜻이다.

왜 이렇게 높은가? 몇 가지 가능성:
1. **글로벌 경기 사이클** — 전 세계적으로 경기가 회복되면 저평가 종목이 함께 반등
2. **글로벌 위험 선호** — 투자자들의 위험 태도가 전 세계적으로 동시에 변함
3. **공통 팩터** — 가치 프리미엄을 만드는 근본 원인이 글로벌

**Stock Momentum 대각선: 0.65***

모멘텀도 비슷하게 높다. 4개국 모멘텀 전략들이 65% 상관. 한 나라에서 모멘텀이 잘 되면 다른 나라에서도 잘 된다.

**Nonstock Value 대각선: 0.07**

비주식 가치 전략들 간 상관은 **매우 낮다** — 7%밖에 안 된다. 그리고 "*"가 없다 = 통계적으로 유의하지 않다.

왜 이렇게 낮은가? 비주식 자산군(국가지수, 통화, 채권, 원자재)은 **서로 매우 이질적**이기 때문이다. 통화의 가치와 원자재의 가치는 전혀 다른 경제적 요인에 의해 결정된다. 주식은 "기업의 수익성"이라는 공통 축이 있지만, 비주식 자산군에는 그런 공통 축이 약하다.

**Nonstock Momentum 대각선: 0.21***

비주식 모멘텀은 21% — 가치(7%)보다는 높지만 주식(65%)보다는 낮다. 모멘텀 쪽이 자산군 간 공통성이 더 있다는 뜻.

> 📚 **더 깊이**: [ch05 상관과 공분산](../chapters/ch05-correlation.md) — 상관계수의 수학적 정의와 해석

---

### 비대각선: 서로 다른 그룹 간 상관

#### 가치끼리: 양의 상관

**Stock Value vs Nonstock Value: 0.15***

주식 가치 전략과 비주식 가치 전략이 함께 움직인다. 상관이 0.15로 높지는 않지만 **통계적으로 유의하다** ("*" 표시). 전혀 다른 자산군의 가치 전략들이 0이 아닌 양의 상관을 보인다는 것 자체가 의미 있는 발견이다.

#### 모멘텀끼리: 양의 상관

**Stock Momentum vs Nonstock Momentum: 0.37***

주식 모멘텀과 비주식 모멘텀의 상관은 0.37 — 가치끼리(0.15)보다 **훨씬 강하다**. 모멘텀이 자산군을 넘어 더 강하게 연결되어 있다.

왜 모멘텀이 가치보다 자산군 간 상관이 높은가? 모멘텀은 **가격 자체**의 추세를 따르는 전략이다. 글로벌 자금 흐름이나 위험 선호 변화가 모든 자산의 가격에 동시에 영향을 미치므로, 가격 추세도 동시에 나타날 수 있다. 반면 가치는 각 자산군마다 다른 "펀더멘털"을 비교하므로, 공통 움직임이 상대적으로 약하다.

#### 가치 vs 모멘텀 (같은 자산 범주 내): 음의 상관

**Stock Value vs Stock Momentum: -0.53***

주식에서 가치와 모멘텀은 **강하게 반대로 움직인다**. 가치가 잘 되는 분기에 모멘텀은 안 되고, 모멘텀이 잘 되는 분기에 가치는 안 된다.

이 -0.53은 Table I의 개별 시장 상관 (약 -0.60)보다 약간 약한데, 이는 **평균 수익률 간 상관**이기 때문이다. 4개국을 평균 내면 국가별 고유 변동이 상쇄되면서 전체 상관의 절대값이 약간 줄어든다.

**Nonstock Value vs Nonstock Momentum: -0.13**

비주식에서도 가치와 모멘텀은 음의 상관이지만, -0.13으로 약하고 **통계적으로 유의하지 않다** ("*" 없음). 비주식 자산군 내에서는 가치-모멘텀 음의 관계가 주식만큼 강하지 않다.

#### 가치 vs 모멘텀 (다른 자산 범주 간): 음의 상관

**Stock Value vs Nonstock Momentum: -0.26***

주식의 가치와 비주식의 모멘텀이 음의 상관. **자산군을 넘어서도** 가치-모멘텀의 음의 관계가 존재한다.

**Nonstock Value vs Stock Momentum: -0.16***

비주식 가치와 주식 모멘텀도 음의 상관. 역시 통계적으로 유의.

---

### 마지막 2행: 글로벌 주식 팩터와의 상관

| | Stock Value | Stock Momentum |
|--|-------------|----------------|
| **Global Stock value** | 0.27* | -0.19* |
| **Global Stock momentum** | -0.28* | 0.40* |

이 행들은 **Global Stock value/momentum** (4개국 주식을 통합한 글로벌 주식 팩터)와 **비주식 각 그룹**의 상관을 보여준다. (열 제목이 Panel B와 연결되는 요약 역할)

- Global Stock value는 Nonstock value와 양의 상관(0.27*), Nonstock momentum과 음의 상관(-0.19*)
- Global Stock momentum은 Nonstock value와 음의 상관(-0.28*), Nonstock momentum과 양의 상관(0.40*)

패턴이 완벽하게 일관적이다: **같은 전략 유형끼리 양, 다른 유형끼리 음**.

---

## Table II Panel B: 글로벌 주식 vs 개별 비주식 계열 (p.948)

> *Panel B. Correlation of Average Stock Series with Each Nonstock Series*

### 뜯기

Panel A는 비주식을 하나의 그룹으로 묶었다. Panel B는 이를 **풀어서** 각 비주식 자산군(국가지수, 통화, 채권, 원자재)과 글로벌 주식 팩터의 상관을 **개별적으로** 보여준다.

| | Country Index Value | Currency Value | FI Value | Commodity Value | Country Index Mom | Currency Mom | FI Mom | Commodity Mom |
|--|---------------------|----------------|----------|-----------------|-------------------|--------------|--------|---------------|
| **Global Stock value** | 0.27* | 0.13* | -0.03 | 0.01 | -0.28* | -0.20* | -0.01 | -0.17* |
| **Global Stock momentum** | -0.19* | -0.12* | -0.05 | -0.06 | 0.40* | 0.28* | 0.09 | 0.20* |

이 16개 숫자를 체계적으로 분석한다.

### Global Stock Value (글로벌 주식 가치) 행

**가치 전략들과의 상관 (같은 유형)**:
- Country Index Value: **0.27*** — 국가지수 가치와 강한 양의 상관. 국가지수는 "국가 단위의 주식"이므로 개별 주식 가치와 연결되는 것이 자연스럽다.
- Currency Value: **0.13*** — 통화 가치와도 양의 상관. 약하지만 유의.
- FI (Fixed Income) Value: **-0.03** — 채권 가치와는 상관 없음. 유의하지도 않음.
- Commodity Value: **0.01** — 원자재 가치와도 상관 없음.

패턴: 주식과 가까운 자산(국가지수 > 통화)은 상관이 있고, 먼 자산(채권, 원자재)은 상관이 없다. 이건 직관적으로 이해된다 — 국가지수는 결국 주식의 집합이고, 통화는 국가 경제와 연결되지만, 채권과 원자재는 다른 요인에 더 크게 좌우된다.

**모멘텀 전략들과의 상관 (다른 유형)**:
- Country Index Mom: **-0.28*** — 강한 음의 상관
- Currency Mom: **-0.20*** — 유의한 음의 상관
- FI Mom: **-0.01** — 상관 없음
- Commodity Mom: **-0.17*** — 유의한 음의 상관

패턴: 주식 가치는 다른 자산군의 모멘텀과 **음의 상관**. 채권만 예외. 가치-모멘텀의 음의 관계가 자산군을 넘어 존재한다는 강력한 증거.

### Global Stock Momentum (글로벌 주식 모멘텀) 행

**가치 전략들과의 상관 (다른 유형)**:
- Country Index Value: **-0.19*** — 음의 상관
- Currency Value: **-0.12*** — 음의 상관
- FI Value: **-0.05** — 상관 없음
- Commodity Value: **-0.06** — 상관 없음

**모멘텀 전략들과의 상관 (같은 유형)**:
- Country Index Mom: **0.40*** — 매우 강한 양의 상관
- Currency Mom: **0.28*** — 강한 양의 상관
- FI Mom: **0.09** — 유의하지 않음
- Commodity Mom: **0.20*** — 유의한 양의 상관

### Panel B의 핵심 패턴

16개 숫자를 관통하는 규칙:

| 비교 대상 | 부호 | 강도 |
|----------|------|------|
| 주식 가치 vs 비주식 가치 | **양(+)** | 국가지수 > 통화 > 채권/원자재 |
| 주식 모멘텀 vs 비주식 모멘텀 | **양(+)** | 국가지수 > 통화 > 원자재 > 채권 |
| 주식 가치 vs 비주식 모멘텀 | **음(-)** | 국가지수 > 통화 > 원자재 > 채권 |
| 주식 모멘텀 vs 비주식 가치 | **음(-)** | 국가지수 > 통화 > 채권/원자재 |

**채권(FI)만 일관되게 유의하지 않다.** 이건 Table I에서 채권의 가치/모멘텀 프리미엄이 약했던 것과 일관적이다. 채권은 이 논문의 프레임워크에서 가장 약한 고리다.

---

## 본문 해석: 4가지 상관 패턴 (p.949~950)

> "Panel A of Table II shows a consistent pattern, where value in one market or asset class is positively correlated with value elsewhere, momentum in one market or asset class is positively correlated with momentum elsewhere, and value and momentum are negatively correlated everywhere across markets and asset classes."

### 뜯기

논문이 Table II에서 읽어내는 **4가지 상관 패턴**을 명확히 정리한다:

| # | 패턴 | 예시 | 해석 |
|---|------|------|------|
| 1 | 가치 ↔ 가치: **양(+)** | US value가 좋으면 Japan value도 좋다 | 가치 프리미엄의 공통 원인 존재 |
| 2 | 모멘텀 ↔ 모멘텀: **양(+)** | US momentum이 좋으면 Currency momentum도 좋다 | 모멘텀 프리미엄의 공통 원인 존재 |
| 3 | 가치 ↔ 모멘텀 (같은 자산 내): **음(-)** | US value가 좋으면 US momentum은 나쁘다 | 가치와 모멘텀은 서로 반대 |
| 4 | 가치 ↔ 모멘텀 (다른 자산 간): **음(-)** | US value가 좋으면 Currency momentum도 나쁘다 | 이 반대 관계가 자산군을 넘어 존재 |

이 4가지가 **동시에** 성립한다는 것이 핵심이다. 하나하나는 이미 알려진 사실일 수 있지만, 8개 자산군에서 **모두 동시에** 성립한다는 것은 새로운 발견이다.

---

### 구체적 숫자 (p.950)

> "The average individual stock value strategy has a correlation of 0.68 with the average value strategy in other stock markets, and of 0.15 with the average nonstock value strategy."

### 뜯기

- 주식 가치 간: **0.68** — 같은 유형(주식) 내에서 매우 강한 연결
- 주식 가치 vs 비주식 가치: **0.15** — 다른 유형 간에도 연결이 있지만 약함

0.68과 0.15의 차이가 의미하는 것: 가치 전략의 공통 움직임은 **같은 자산 유형 내**에서 훨씬 강하고, **다른 자산 유형 간**에는 약하다. 하지만 0이 아니라는 것이 중요하다.

> "The average individual stock momentum strategy has a correlation of 0.65 with the average momentum strategy in other stock markets and a correlation of 0.37 with the average nonstock momentum strategy."

### 뜯기

- 주식 모멘텀 간: **0.65** — 가치(0.68)와 비슷하게 강함
- 주식 모멘텀 vs 비주식 모멘텀: **0.37** — 가치(0.15)보다 **훨씬 강함**

모멘텀이 자산군 간 경계를 더 잘 넘는다. 이건 모멘텀의 원천이 더 "글로벌"한 요인(위험 선호, 자금 흐름)에 있을 가능성을 시사한다.

> "The strong correlation structure among value and momentum strategies across such different assets is interesting since these asset classes have different types of investors, institutional and market structures, and information environments."

### 뜯기

논문이 이 발견의 의미를 강조한다. 자산군마다:
- **투자자가 다르다** — 주식 펀드매니저 vs 원자재 트레이더
- **시장 구조가 다르다** — 거래소 vs 장외(OTC)
- **정보 환경이 다르다** — 기업 실적 발표 vs 원자재 수급 데이터

그런데도 **같은 패턴**이 나타난다. 이것은 특정 시장의 미시구조나 특정 투자자 집단의 행동 편향으로는 설명할 수 없다. **보편적인 원인**이 있어야 한다.

---

### 가치-모멘텀 음의 상관 상세 (p.950)

> "Value and momentum are also negatively correlated across asset classes. The correlation between a value strategy in one stock market and a portfolio of momentum strategies in other stock markets is -0.53."

### 뜯기

주의: 이 -0.53은 Panel A의 Stock Value vs Stock Momentum과 같은 숫자다. 주식 가치와 **다른 주식 시장의** 모멘텀 간 상관이다.

> "In addition, value in one asset class is negatively correlated with momentum in another asset class."

### 뜯기

자산군을 넘어서도 음의 상관이 존재한다는 핵심 발견의 재확인.

> "For example, the correlation between the average stock value strategy and the average nonstock momentum strategy is -0.26, the correlation between nonstock value strategies and stock momentum strategies is -0.16, and the correlation between nonstock value and nonstock momentum in other asset classes is -0.13 on average."

### 뜯기

구체적 숫자 정리:

| 비교 | 상관 | 유의성 |
|------|------|--------|
| Stock Value vs Nonstock Momentum | **-0.26** | * |
| Nonstock Value vs Stock Momentum | **-0.16** | * |
| Nonstock Value vs Nonstock Momentum | **-0.13** | (유의하지 않음) |

패턴: 가치-모멘텀의 음의 상관은 **주식 쪽에 가까울수록 강하고**, 비주식끼리는 약하다. 하지만 **방향은 항상 음**이다.

---

### 패시브 노출로는 설명 불가 (p.950)

> "This correlation structure — value being positively correlated across assets, momentum being positively correlated across assets, and value and momentum being negatively correlated within and across asset classes — cannot be explained by the correlation of passive exposure to the asset classes themselves."

### 뜯기

이 문장은 **핵심 반론을 차단**한다.

반론: "가치 전략들이 같이 움직이는 건 그냥 **시장 자체**가 같이 움직이기 때문 아닌가? 미국 주식시장이 오르면 일본도 오르니까, 미국 롱-숏 포트폴리오와 일본 롱-숏 포트폴리오가 같이 움직일 수 있지 않나?"

답변: **아니다.** 이유:

> "The value and momentum strategies we examine are long-short and market neutral with respect to each asset class, and yet exhibit stronger correlation across asset classes than do passive exposures to these asset classes."

### 뜯기

두 가지 근거:

1. **롱-숏(long-short)**: 사는 것(롱)과 파는 것(숏)이 합쳐져 있으므로, 시장 전체가 오르내리는 것과는 무관해야 한다. 시장이 10% 올라도 롱 부분이 +10%, 숏 부분이 +10%면 전략 수익은 0이다.

2. **시장 중립(market neutral)**: 각 자산군 내에서 시장 노출이 제거되어 있다. 즉 전략의 수익률은 시장 수익률과 독립적이어야 한다.

그런데도 전략 간 상관이 시장 간 상관보다 **더 강하다**. 이것은 시장의 공통 움직임 위에 **추가적인 공통 요인**이 있다는 결정적 증거다.

비유: 두 학교의 시험 점수가 비슷한 건 "비슷한 교육과정" 때문일 수 있다. 하지만 **두 학교 내에서 "상위 학생 - 하위 학생" 차이**까지 비슷하게 움직인다면? 교육과정으로는 설명 안 된다. 학생들의 능력을 좌우하는 **더 깊은 공통 요인**이 있는 것이다.

---

## BE/ME 정의의 강건성 검정 (p.950~951)

> "For robustness, we also show that defining value differently produces similar negative correlation numbers between value and momentum strategies."

### 뜯기

하나의 반론이 더 있다: "가치와 모멘텀의 음의 상관은 **BE/ME의 정의** 때문에 기계적으로 발생하는 거 아닌가?"

왜 이런 의심이 생기는가? BE/ME에서 **ME(시장가치) = 주가 x 주식수**다. 주가가 최근에 많이 오른 주식은 ME가 커지므로 BE/ME가 낮아진다(=성장주로 분류). 동시에 최근 수익률이 높으니 모멘텀 측정치도 높다. 이렇게 **주가가 BE/ME와 모멘텀 모두에 영향**을 미치므로, 기계적으로 음의 상관이 발생할 수 있다.

> "Our value measure for equities, *BE/ME*, uses the most recent market value in the denominator, which yields a -0.53 correlation between value and momentum in Table II, Panel A."

### 뜯기

현재 방식: BE / (현재 ME) → 가치-모멘텀 상관 = **-0.53**

> "However, lagging prices by 1 year in the *BE/ME* measure (i.e., using *ME* from 1 year prior) so that the value measure uses price data that do not overlap with the momentum measure, still produces a negative correlation between value and momentum of -0.28, which is highlighted in the Internet Appendix."

### 뜯기

대안 1: BE / (1년 전 ME) → 가치-모멘텀 상관 = **-0.28**

왜 이렇게 하는가? 모멘텀은 "과거 2~12개월 수익률"로 측정한다. ME를 1년 전 값으로 쓰면, 가치 시그널과 모멘텀 시그널이 **겹치는 가격 정보가 없다**. 그래도 음의 상관이 유지된다(-0.28).

상관이 -0.53에서 -0.28로 줄어들긴 했다. 이건 **기계적 요인이 일부 기여**함을 보여준다(0.53 - 0.28 = 0.25 정도). 하지만 -0.28도 여전히 **유의미하게 음**이다.

> "While these correlations are smaller in magnitude, they are still significantly negative."

### 뜯기

핵심: 기계적 요인을 제거해도 음의 상관이 살아남는다. 기계적 효과가 전부는 아니다.

> "In addition, using the negative of the past 5-year return of a stock as a value measure for equities, which is what we use for the nonequity asset classes, also generates negative correlations between value and momentum of similar magnitude (-0.48 as highlighted in the Internet Appendix)."

### 뜯기

대안 2: "5년 수익률 반전(reversal)" = 과거 5년 수익률의 음수를 가치 측정치로 사용.

이 방식은:
- BE/ME를 **전혀 사용하지 않는다** — 장부가치 개념 자체가 없음
- 비주식 자산군의 가치 측정법과 동일한 원리 (과거 수익률의 반전)
- 가치-모멘텀 상관 = **-0.48**

-0.48은 원래의 -0.53과 거의 비슷하다. BE/ME라는 특정 측정치가 아니라, **가치(저가매수)라는 개념 자체**가 모멘텀과 음의 관계에 있다는 증거.

> "This provides more evidence that past 5-year returns capture similar effects as *BE/ME* (Gerakos and Linnainmaa (2012) reach a similar conclusion)."

### 뜯기

5년 수익률 반전과 BE/ME가 **같은 것을 측정**한다는 학술적 확인. Gerakos and Linnainmaa (2012)도 같은 결론.

> "Hence, simply using recent prices or using past 5-year returns as a value measure does not appear to be driving the negative correlation between value and momentum returns, which appears to be robust across different value measures."

### 뜯기

최종 결론: 가치-모멘텀의 음의 상관은:
- 동시 ME 사용 → **-0.53**
- 1년 래그 ME → **-0.28**
- 5년 수익률 반전 → **-0.48**

세 가지 다른 정의에서 모두 음의 상관이 유지된다. **측정 방법의 인위적 산물이 아니라 실제 현상**이라는 강건한 결론.

| 가치 측정법 | 가치-모멘텀 상관 | 기계적 겹침 | 해석 |
|-----------|--------------|----------|------|
| BE / 동시 ME | -0.53 | 있음 (가격이 양쪽에 영향) | 기계적 효과 + 진짜 효과 |
| BE / 1년전 ME | -0.28 | 없음 (가격 겹침 제거) | 진짜 효과만 |
| -5년 수익률 | -0.48 | 있음 (가격이 양쪽에 영향) | BE/ME 없이도 동일 |

---

## Panel B 본문 해석 (p.950)

> "Panel B of Table II breaks down the correlations of the average stock strategies with each of the nonstock strategies."

### 뜯기

Panel A에서 비주식을 하나로 묶었던 것을 Panel B에서 풀어놓는다.

> "Nearly all of the value strategies across asset classes are consistently positively correlated, all of the momentum strategies are consistently positively correlated, all of the correlations between value and momentum are consistently negatively correlated, and most of these correlations are statistically different from zero."

### 뜯기

Panel B의 16개 숫자를 한 문장으로 요약:
- 가치끼리: **거의 전부 양** (예외: FI Value -0.03, Commodity Value 0.01 — 약한 양 또는 0)
- 모멘텀끼리: **전부 양** (FI Mom 0.09만 유의하지 않음)
- 가치-모멘텀: **전부 음** (FI 관련만 유의하지 않음)
- **대부분 통계적으로 유의**

채권(Fixed Income)만 일관되게 패턴에서 벗어난다. 이것이 Section II.B에서 언급한 "채권은 가장 약한 결과"와 일치한다.

---

## Figure 1: PCA 분석 (p.951~952)

> "Figure 1 examines the first principal component of the covariance matrix of the value and momentum returns."

### 뜯기

**PCA (Principal Component Analysis, 주성분 분석)**는 여러 변수의 공통 변동을 요약하는 통계 기법이다.

비유: 교실에서 30명 학생의 10과목 성적이 있다. PCA는 "이 10개 성적을 관통하는 **가장 중요한 패턴**"을 찾아낸다. 첫 번째 주성분(PC1)이 가장 큰 패턴이다. 예를 들어 "전반적으로 공부를 잘하는 학생 vs 못하는 학생"이 PC1일 수 있다.

여기서는:
- 변수 = 각 자산군의 가치/모멘텀 전략 수익률
- PC1 = 이 전략들을 관통하는 **가장 큰 공통 패턴**

---

### Figure 1 상단: 4개국 개별주식 (p.952)

> "The top panel of the figure plots the eigenvector weights associated with the largest eigenvalue from the covariance matrix of the individual stock value and momentum strategies in each stock market."

### 뜯기

**상단 그래프** 구성:
- 8개 막대: US value, US momentum, UK value, UK momentum, Europe value, Europe momentum, Japan value, Japan momentum
- 각 막대의 높이 = **고유벡터(eigenvector) 가중치** = 해당 전략이 PC1에 기여하는 정도

그래프에서 관찰되는 패턴:
- **가치(파란색)**: 4개국 모두 **양(+)** 방향으로 약 +0.3~0.4 수준
- **모멘텀(노란색)**: 4개국 모두 **음(-)** 방향으로 약 -0.3~-0.5 수준

(일본만 약간 다름 — 일본은 모멘텀이 약해서 모멘텀 가중치의 절대값이 약간 작을 수 있다)

> "Percentage of covariance matrix explained = 53.6%"

PC1이 8개 전략 수익률 변동의 **53.6%**를 설명한다.

> "Both panels show that the first principal component loads in one direction on all value strategies and loads in exactly the opposite direction on all momentum strategies,"

### 뜯기

PC1의 의미: **"가치에 +, 모멘텀에 -"** (또는 반대 부호를 붙이면 "모멘텀에 +, 가치에 -").

이것은 PC1이 본질적으로 **"롱 모멘텀 + 숏 가치" 팩터** (또는 그 역인 "롱 가치 + 숏 모멘텀" 팩터)라는 뜻이다. 전 세계 주식 시장의 가치/모멘텀 전략들의 가장 큰 공통 변동 원천이 바로 이 **가치-모멘텀 축**이다.

> "highlighting the strong and ubiquitous negative correlation between value and momentum across asset classes as well as the positive correlation among value strategies and among momentum strategies across asset classes."

### 뜯기

PCA가 Table II의 상관 패턴을 **시각적으로** 확인해 준다:
- 가치 가중치가 모두 같은 부호 → 가치끼리 양의 상관
- 모멘텀 가중치가 모두 같은 부호 → 모멘텀끼리 양의 상관
- 가치와 모멘텀이 **반대 부호** → 가치-모멘텀 음의 상관

> "The first principal component, which is essentially long momentum and short value (or vice versa) in every asset class, accounts for 54% of the individual stock strategies' covariance matrix"

### 뜯기

본문에서는 **"54%"**로 반올림. PC1 하나가 8개 전략 변동의 절반 이상을 설명한다. 이건 매우 강력한 공통 구조다.

8개 전략이 완전히 독립적이라면 PC1은 1/8 = 12.5%만 설명해야 한다. 54%라는 것은 **독립적이지 않고 강하게 연결**되어 있다는 뜻이다.

---

### Figure 1 하단: 전 자산군 (p.952)

> "and 23% of the all-asset-class covariance matrix."

### 뜯기

**하단 그래프** 구성:
- 10개 막대: 5개 자산군(Stocks, Countries, Currencies, Bonds, Commodities) x 2개 전략(Value, Momentum)
- "Stocks"는 4개국 주식을 합친 글로벌 주식 팩터

> "Percentage of covariance matrix explained = 22.7%"

PC1이 10개 전략 수익률 변동의 **22.7%**를 설명한다.

본문에서는 **"23%"**로 반올림. 주식만 볼 때(54%)보다 낮지만, 10개 전략이 완전히 독립적이라면 1/10 = 10%만 설명해야 하므로 여전히 **2배 이상** 높다.

하단 그래프에서도 **동일한 패턴**:
- **가치(파란색)**: 5개 자산군 모두 **양(+)**
- **모멘텀(노란색)**: 5개 자산군 모두 **음(-)**

채권(Bonds)만 가중치의 절대값이 작다 — Table II에서 채권의 상관이 유의하지 않았던 것과 일치.

> "The commonality among value and momentum strategies across vastly different assets and markets with widely varying information, structures, and investors points to common global factor structure among these phenomena."

### 뜯기

논문의 핵심 결론 중 하나다:

**완전히 다른 자산, 시장, 정보 환경, 투자자 집단에서** 가치와 모멘텀이 같은 패턴으로 함께 움직인다 → **공통 글로벌 팩터 구조(common global factor structure)**가 존재한다.

이것은 초록의 문장 2("a strong common factor structure among their returns")의 **실증적 증거**다. 더 이상 "우연"이나 "데이터 마이닝"으로 치부하기 어렵다.

> 📚 **더 깊이**: [ch08 PCA와 팩터 구조](../chapters/ch08-pca-factors.md) — 주성분 분석의 수학과 직관, 고유벡터/고유값의 의미

---

### Internet Appendix: 조합 전략의 상관 (p.951)

> "The Internet Appendix also shows that correlations across markets and asset classes for the value/momentum combination strategies are lower than they are for value or momentum alone, indicating that the negative correlation between value and momentum offsets some of the common variation when combined together in a portfolio."

### 뜯기

**가치+모멘텀 조합** 전략의 자산군 간 상관은 **개별 전략보다 낮다**.

왜? 가치와 모멘텀이 반대로 움직이므로, 합치면 공통 변동의 일부가 **상쇄**된다.

비유: 여름에 아이스크림 매출은 오르고 핫초코 매출은 내린다. 각각의 자산군 간 상관은 높을 수 있지만, "아이스크림+핫초코" 조합 매장의 매출은 다른 조합 매장과 상관이 낮다 — 계절 효과가 상쇄되니까.

> "In other words, it appears that value and momentum load oppositely on some common sources of risk."

### 뜯기

핵심 통찰: 가치와 모멘텀은 **같은 위험 원천**에 **반대 방향으로** 노출되어 있다.

이것은 Section III의 이론적 설명으로 직결된다. 그 "같은 위험 원천"의 후보가 바로 **글로벌 펀딩 유동성 위험**이다.

---

## Figure 2: 누적수익률 그래프 (p.953~955)

> "Figure 2 illustrates succinctly the return and correlation evidence on value and momentum globally by plotting the cumulative returns to value, momentum, and their combination in each asset market and across all asset markets."

### 뜯기

Figure 2는 논문에서 **가장 시각적으로 강력한 증거**다. 11개의 개별 그래프가 있고, 각각이 하나의 시장 또는 시장 집합을 보여준다.

> "The consistent positive returns and strong correlation structure across assets, as well as the negative correlation between value and momentum in every market, is highlighted in the graphs."

### 뜯기

각 그래프에서 읽을 수 있는 것:
1. **가치(빨간/점선)**: 우상향 → 양의 수익
2. **모멘텀(파란/점선)**: 우상향 → 양의 수익
3. **조합(초록/실선)**: 가장 가파르게 우상향 → 더 높은 수익, 더 낮은 변동
4. **가치와 모멘텀이 반대로 움직이는 구간**이 눈에 보임

---

### 그래프의 구성

각 그래프에는:
- **y축**: 누적 로그 수익률 (연 10%로 스케일링)
- **x축**: 시간
- **3개의 선**: Value (가치), Momentum (모멘텀), Combo (50/50 조합)
- **표시 정보**: 샤프 비율 3개 + 가치-모멘텀 상관 1개

**연 10% 스케일링**: 모든 전략의 수익률을 연간 변동성이 10%가 되도록 조정한 것. 왜? 자산군마다 변동성이 다르기 때문에(예: 원자재는 주식보다 변동성이 큼) 동일한 스케일로 비교하기 위함.

---

### 11개 그래프의 전체 데이터

#### 개별 주식 시장 (4개)

**1. U.S. Stocks (미국 주식)**

| 항목 | 값 |
|------|-----|
| Value 샤프 | 0.26 |
| Momentum 샤프 | 0.45 |
| Combo 샤프 | 0.88 |
| Corr(val, mom) | -0.65 |

미국에서 모멘텀(0.45)이 가치(0.26)를 크게 앞선다. 조합(0.88)은 둘의 단순 합보다 훨씬 높다 — 음의 상관(-0.65) 덕분이다.

**2. U.K. Stocks (영국 주식)**

| 항목 | 값 |
|------|-----|
| Value 샤프 | 0.38 |
| Momentum 샤프 | 0.48 |
| Combo 샤프 | 1.07 |
| Corr(val, mom) | -0.64 |

영국도 패턴이 동일. 조합의 샤프가 **1.07**로 1을 넘긴다.

**3. Europe Stocks (유럽 주식)**

| 항목 | 값 |
|------|-----|
| Value 샤프 | 0.44 |
| Momentum 샤프 | 0.63 |
| Combo 샤프 | 1.20 |
| Corr(val, mom) | -0.52 |

유럽은 개별 전략의 샤프도 높고 조합도 **1.20**으로 매우 높다. 상관이 -0.52로 다른 시장보다 약간 약하지만 여전히 강한 음의 관계.

**4. Japan Stocks (일본 주식)**

| 항목 | 값 |
|------|-----|
| Value 샤프 | 0.77 |
| Momentum 샤프 | 0.13 |
| Combo 샤프 | 0.88 |
| Corr(val, mom) | -0.64 |

일본은 다른 시장과 **극적으로 다르다**:
- 가치가 **0.77**로 압도적 (다른 시장의 2~3배)
- 모멘텀이 **0.13**으로 거의 0에 가까움

이것이 왜 흥미로운가? 모멘텀이 안 되는 걸 행동재무학으로 설명하려면 "일본 투자자의 문화적 차이" 같은 이야기를 해야 하는데, 그러면 동시에 **가치가 왜 이렇게 잘 되는지**도 설명해야 한다. 가치-모멘텀 상관은 -0.64로 다른 시장과 같다. 즉 일본에서도 **둘은 여전히 서로의 적**이다.

#### 비주식 자산군 (4개)

**5. Country Indices (국가지수)**

| 항목 | 값 |
|------|-----|
| Value 샤프 | 0.60 |
| Momentum 샤프 | 0.63 |
| Combo 샤프 | 1.00 |
| Corr(val, mom) | -0.37 |

국가지수는 가치(0.60)와 모멘텀(0.63)이 거의 동등하고 조합(1.00)이 정확히 1. 상관은 -0.37로 주식보다 약하다.

**6. Currencies (통화)**

| 항목 | 값 |
|------|-----|
| Value 샤프 | 0.44 |
| Momentum 샤프 | 0.32 |
| Combo 샤프 | 0.69 |
| Corr(val, mom) | -0.43 |

통화에서는 가치(0.44)가 모멘텀(0.32)보다 우세.

**7. Fixed Income (채권)**

| 항목 | 값 |
|------|-----|
| Value 샤프 | 0.07 |
| Momentum 샤프 | 0.07 |
| Combo 샤프 | 0.20 |
| Corr(val, mom) | -0.35 |

채권은 모든 숫자가 **매우 낮다**. 가치도 모멘텀도 샤프 0.07. 논문이 "채권에서 결과가 가장 약하다"고 반복적으로 인정한 것과 일치. 그래도 음의 상관(-0.35)은 존재하고, 조합(0.20)은 개별(0.07)보다 높다.

**8. Commodities (원자재)**

| 항목 | 값 |
|------|-----|
| Value 샤프 | 0.31 |
| Momentum 샤프 | 0.55 |
| Combo 샤프 | 0.77 |
| Corr(val, mom) | -0.46 |

원자재에서 모멘텀(0.55)이 가치(0.31)를 크게 앞선다. 원자재 가격은 추세를 타는 경향이 강하기 때문(원유 가격이 오르기 시작하면 계속 오르는 경향).

#### 글로벌 집합 (3개)

**9. Global Stocks (글로벌 주식)**

| 항목 | 값 |
|------|-----|
| Value 샤프 | 0.51 |
| Momentum 샤프 | 0.59 |
| Combo 샤프 | 1.28 |
| Corr(val, mom) | -0.60 |

4개국 주식을 변동성 가중으로 합친 것. 개별 시장보다 샤프가 높다 — 분산 투자 효과. 조합 **1.28**은 매우 인상적.

**10. Global Other Assets (글로벌 비주식)**

| 항목 | 값 |
|------|-----|
| Value 샤프 | 0.55 |
| Momentum 샤프 | 0.62 |
| Combo 샤프 | 1.14 |
| Corr(val, mom) | -0.49 |

비주식 4개 자산군을 합친 것. 역시 개별보다 높은 샤프.

**11. Global All Assets (전 자산군 통합)**

| 항목 | 값 |
|------|-----|
| Value 샤프 | 0.72 |
| Momentum 샤프 | 0.74 |
| Combo 샤프 | **1.59** |
| Corr(val, mom) | -0.60 |

**이것이 논문의 클라이맥스 숫자다.** 전 세계 전 자산군의 가치+모멘텀 50/50 조합의 샤프 비율이 **1.59**.

> 📚 **더 깊이**: [ch09 샤프 비율의 의미](../chapters/ch09-sharpe-ratio.md) — 1.59가 왜 경이로운 숫자인지

---

### Figure 2 종합 분석

11개 그래프를 한 표로 정리:

| 시장 | V 샤프 | M 샤프 | C 샤프 | Corr | 특이사항 |
|------|--------|--------|--------|------|---------|
| US Stocks | 0.26 | 0.45 | 0.88 | -0.65 | 모멘텀 우위 |
| UK Stocks | 0.38 | 0.48 | 1.07 | -0.64 | 균형적 |
| Europe Stocks | 0.44 | 0.63 | 1.20 | -0.52 | 모멘텀 우위 |
| Japan Stocks | 0.77 | 0.13 | 0.88 | -0.64 | 가치 압도, 모멘텀 부진 |
| Country Indices | 0.60 | 0.63 | 1.00 | -0.37 | 균형적 |
| Currencies | 0.44 | 0.32 | 0.69 | -0.43 | 가치 우위 |
| Fixed Income | 0.07 | 0.07 | 0.20 | -0.35 | 전반적 약함 |
| Commodities | 0.31 | 0.55 | 0.77 | -0.46 | 모멘텀 우위 |
| Global Stocks | 0.51 | 0.59 | 1.28 | -0.60 | 분산 효과 |
| Global Other | 0.55 | 0.62 | 1.14 | -0.49 | 분산 효과 |
| **Global All** | **0.72** | **0.74** | **1.59** | **-0.60** | **최대 분산 효과** |

#### 읽히는 패턴들

1. **모든 시장에서 조합 > 개별**: 예외 없이 Combo 샤프 > Value 샤프, Combo 샤프 > Momentum 샤프. 이건 음의 상관 덕분이다.

2. **모든 시장에서 음의 상관**: -0.35(채권)에서 -0.65(미국 주식)까지. 예외 없음.

3. **분산이 효과적**: 개별 → 글로벌로 갈수록 샤프가 올라간다. US value(0.26) → Global Stock value(0.51) → Global All value(0.72). 다양화의 힘.

4. **일본이 독특**: 가치는 최고, 모멘텀은 최저. 하지만 음의 상관(-0.64)은 평균 수준 — 두 전략의 **반대 관계**는 일본에서도 건재.

5. **채권이 가장 약함**: 모든 숫자가 다른 자산군보다 현저히 낮다. 하지만 **방향은 동일** — 음의 상관, 조합 우위.

---

### 조합의 샤프 비율이 왜 이렇게 높은가?

두 전략의 50/50 조합 샤프 비율은 다음 공식으로 근사할 수 있다:

$$SR_{combo} \approx \sqrt{SR_V^2 + SR_M^2 - 2 \cdot \rho \cdot SR_V \cdot SR_M}$$

여기서 $\rho$는 상관계수. $\rho < 0$이면 루트 안의 값이 **커진다** — 즉 조합의 샤프가 **높아진다**.

Global All Assets의 경우:
- $SR_V = 0.72$, $SR_M = 0.74$, $\rho = -0.60$

$$SR_{combo} \approx \sqrt{0.72^2 + 0.74^2 - 2(-0.60)(0.72)(0.74)} = \sqrt{0.518 + 0.548 + 0.639} \approx \sqrt{1.705} \approx 1.31$$

실제(1.59)보다 약간 낮은 이유는 이 공식이 **단순 근사**이기 때문이다. 정확한 계산에서는 변동성 가중 방식과 리밸런싱 효과가 추가되어 더 높아진다.

핵심: **음의 상관이 마법의 열쇠**다. 같은 개별 샤프(0.72, 0.74)라도 상관이 +0.60이었다면 조합 샤프는 약 0.35에 불과했을 것이다. 음의 상관 덕분에 **4배 이상** 높아진다.

---

## Section III 전환: 각주 16 (p.951 하단)

> **III. Relation to Macroeconomic and Liquidity Risk**

> "In this section we investigate possible sources driving the common variation of value and momentum strategies across markets and asset classes."

### 뜯기

Section II에서 확인한 "공통 변동"의 **원인**을 찾는 단계로 넘어간다.

---

### 각주 16 (p.951)

> <sup>16</sup> "Chordia and Shivakumar (2002) claim that a conditional forecasting model of macroeconomic risks can explain momentum profits in U.S. stocks, but Griffin, Ji, and Martin (2003) show that neither an unconditional or conditional model of macroeconomic risks can explain momentum"

### 뜯기

이 각주는 **거시경제 위험과 모멘텀**에 관한 학술적 논쟁을 소개한다.

**Chordia and Shivakumar (2002)의 주장**:
- 거시경제 변수(GDP 성장률, 인플레이션 등)의 **조건부 예측 모형**으로 모멘텀 수익을 설명할 수 있다
- 즉 모멘텀은 거시경제 위험에 대한 합리적 보상이다

**조건부(conditional)** 모형이란? 시점에 따라 위험이 변한다는 것. 경기 확장기에는 모멘텀의 위험 노출이 다르고, 경기 침체기에는 다르다.

**Griffin, Ji, and Martin (2003)의 반박**:
- **무조건부(unconditional)** 모형도, **조건부(conditional)** 모형도 모멘텀을 설명할 수 없다
- Chordia and Shivakumar의 결과는 미국에만 국한되며, 국제 데이터에서는 재현되지 않는다

이 논쟁이 왜 이 논문에 중요한가? Section III에서 거시경제 변수와 가치/모멘텀의 관계를 직접 테스트하기 때문이다. 기존 논쟁의 맥락을 알아야 Section III의 결과를 제대로 이해할 수 있다.

---

## 이 섹션에서 배운 것

Section II.C는 논문의 **두 번째 핵심 발견**을 확립한다:

| # | 발견 | 증거 |
|---|------|------|
| 1 | 가치끼리 양의 상관 | Table II: Stock Val 내 0.68, Stock-Nonstock 0.15 |
| 2 | 모멘텀끼리 양의 상관 | Table II: Stock Mom 내 0.65, Stock-Nonstock 0.37 |
| 3 | 가치-모멘텀 음의 상관 (같은 자산 내) | Table II: Stock -0.53, Nonstock -0.13 |
| 4 | 가치-모멘텀 음의 상관 (다른 자산 간) | Table II: -0.26, -0.16 |
| 5 | 패시브 노출로 설명 불가 | 롱-숏, 시장중립인데도 상관 존재 |
| 6 | BE/ME 정의와 무관 | 1년 래그(-0.28), 5년 반전(-0.48)에서도 음의 상관 |
| 7 | PC1 = "가치 vs 모멘텀" 축 | Figure 1: 주식 54%, 전체 23% 설명 |
| 8 | 조합 전략의 압도적 성과 | Figure 2: Global All Combo 샤프 1.59 |

이 상관 구조가 Section III의 **글로벌 3팩터 모형**과 **유동성 위험 가설**의 출발점이 된다.

---

## 여기서 멈추고 생각하기

### 🤔 추론 연습

1. **주식 가치 간 상관(0.68)이 비주식 가치 간 상관(0.07)보다 훨씬 높다.** 왜? → 주식시장은 글로벌로 연결되어 있다(같은 애널리스트, 같은 펀드). 반면 원자재와 통화의 가치 전략은 서로 다른 세계. 0.07이어도 양수라는 것 자체가 놀라운 것.

2. **PC1이 "롱 모멘텀 + 숏 가치"라면**, 이걸 실제로 거래하면 어떻게 되는가? → 모멘텀을 사고 가치를 팔면 PC1에 노출된다. 하지만 이건 50/50 COMBO의 **정반대**다. COMBO는 "롱 가치 + 롱 모멘텀". PC1은 설명력이 높지만 투자 전략으로서는 한쪽에만 베팅하는 것.

3. **패시브 노출로 설명 불가** — 그렇다면 **무엇이** 이 상관을 만드는가? 세 가지 후보:
   - (a) 글로벌 유동성 사이클 (다음 섹션에서 검증)
   - (b) 동일한 투자자가 여러 시장에서 같은 전략을 운용 (AQR 같은 글로벌 퀀트 펀드)
   - (c) 아직 알려지지 않은 글로벌 위험 팩터

### ⚡ 비판적 사고

- Table II의 상관은 **분기별(quarterly)**로 계산되었다. 왜 월별이 아닌가? → 비동시 거래 문제. 하지만 분기별로 하면 **관측치 수가 1/3로 줄어**서 통계적 파워가 약해진다. 이건 트레이드오프.

- **0.07**이 유의한가? Nonstock Value 대각선이 0.07이고 별표가 없다(= 유의하지 않음). "비주식 가치끼리는 사실 상관이 없다"고 해석할 수도 있다. 하지만 0.15(Stock-Nonstock 교차)에는 별표가 있다. 미묘하다.

> **다음**: [dissect-05 거시경제와 유동성 위험](dissect-05-macro-liquidity.md) — Section III. 공통 변동의 원인을 추적한다.
