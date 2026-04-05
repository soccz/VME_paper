# 논문 해체 5: 거시경제 리스크와 유동성 (Section III, p.955~964)

> 이 섹션은 논문의 **"왜?"** 파트다. Section II에서 "가치와 모멘텀은 어디서나 돈을 벌고, 서로 음의 상관을 보인다"는 사실을 확인했다. 이제 질문이 바뀐다: **그 공통 움직임의 원인은 무엇인가?** 거시경제 변수부터 시작해서, 유동성 리스크로 넘어간다.

---

## Section III 도입 (p.955~956)

> "we investigate possible sources driving the common variation of value and momentum strategies across markets and asset classes"

### 뜯기

Section II에서 발견한 핵심: 가치 전략들은 서로 같이 움직이고, 모멘텀 전략들도 서로 같이 움직인다. 그런데 가치↔모멘텀은 반대로 움직인다. 이 "공통 변동(common variation)"을 만드는 **원천(source)**이 뭔지 조사하겠다는 선언이다.

논문은 두 가지 후보를 순서대로 검증한다:

| 후보 | 섹션 | 결과 미리보기 |
|------|------|------------|
| **A. 거시경제 리스크** | p.956~958 | 약한 관계. 대부분 유의하지 않음 |
| **B. 유동성 리스크** | p.958~964 | 펀딩 유동성이 유의. 부분적 설명 |

---

## A. Macroeconomic Risk Exposure (p.956~958)

> "The first two columns of Table III report the time series regression coefficients of U.S. value and momentum returns on U.S. macroeconomic variables: long-run consumption growth, a recession indicator, GDP growth, as well as the U.S. stock market return in excess of the T-bill rate and the Fama and French (1993) bond market factor returns TERM and DEF."

### 뜯기

**방법론**: 시계열 회귀(time-series regression). 매 분기(또는 월) 가치/모멘텀 수익률을 종속변수로 놓고, 거시경제 변수 6개를 독립변수로 넣어 회귀분석을 돌린다.

"이 변수들이 움직이면 가치/모멘텀 수익률도 따라 움직이는가?" — 이것을 검증하는 것이다.

---

### 독립변수 6개: 하나씩 뜯기

#### 1. Long-run consumption growth (장기 소비 성장)

> "Consumption growth is the real per capita growth in nondurable and service consumption obtained quarterly and long-run consumption growth is the future 3-year growth rate in consumption, measured as the sum of log quarterly consumption growth 12 quarters ahead as in Parker and Julliard (2005) and Malloy, Moskowitz, and Vissing-Jorgensen (2009)."

**뜯기**:

"소비 성장"이란 사람들이 물건과 서비스를 얼마나 더 사게 되었는가를 측정한 것이다. 여기서 쓰는 것은 **실질 1인당 비내구재+서비스 소비**다.

왜 "비내구재+서비스"만? 자동차(내구재)는 한 번 사면 몇 년 쓴다. 올해 차를 샀다고 올해의 "소비"가 높은 것은 아니다. 반면 음식(비내구재)과 이발(서비스)은 산 분기에 소비한 것이므로 경제 상황을 더 정확히 반영한다.

**"장기" 소비 성장**은 특이하다 — 과거가 아니라 **미래 12분기(3년) 선행** 소비 성장의 합이다:

$$\text{Long-run consumption growth}_t = \sum_{k=1}^{12} \log(C_{t+k}/C_{t+k-1})$$

왜 미래를 보는가? Parker & Julliard (2005)의 아이디어: 자산의 위험은 그 자산이 **장기적으로** 소비와 얼마나 같이 움직이는지로 측정해야 한다. 한 분기의 소비 변동은 노이즈가 많지만, 3년치를 합하면 진짜 경제 충격이 드러난다.

Bansal & Yaron (2004)의 Long-run risks 모형도 같은 맥락: 자산 가격은 장기 소비 성장 기대에 의해 결정된다.

> 이 변수가 양(+)이면 "소비가 좋아질 때 이 전략도 좋다" → 위험한 자산 → 프리미엄이 정당화된다.
> 이 변수가 0이면 "소비와 무관하다" → 소비 기반 모형으로 설명 불가.

#### 2. Recession dummy (경기침체 더미)

> "The recession indicator is defined using ex post peak (=0) and trough dates (=1) from the NBER."

**뜯기**:

NBER(National Bureau of Economic Research)은 미국 경기순환의 공식 판정 기관이다. "경기 정점(peak)"부터 "경기 저점(trough)"까지가 침체 구간이다.

더미 변수: 침체 기간 = 1, 아닌 기간 = 0. 단순하다.

이 변수에 음(-)으로 로딩하면 "침체 때 손해를 본다" → 경기 민감한 전략 → 침체 리스크에 대한 보상으로 프리미엄을 받을 수 있다.

#### 3. GDP growth (GDP 성장)

> "GDP growth is real per capita growth in GDP."

**뜯기**:

실질 1인당 GDP. NIPA(National Income and Product Accounts, 국민소득생산계정)에서 가져온다. 소비 성장보다 넓은 개념 — 소비 + 투자 + 정부지출 + 순수출을 다 포함한다.

#### 4. Market return (시장 수익률)

> "the U.S. stock market return in excess of the T-bill rate"

**뜯기**:

MSCI World Index의 초과수익률 = MSCI World - T-bill 금리. 글로벌 주식시장 전체의 성과를 대표한다.

이 변수에 양(+)이면 "시장이 좋을 때 이 전략도 좋다" → 시장 베타가 있다. 음(-)이면 "시장이 나쁠 때 오히려 잘 된다" → 헤지 역할.

#### 5. TERM (기간 스프레드)

> Fama and French (1993) bond market factor returns TERM

**뜯기**:

TERM = 장기 국채 수익률 - 단기 국채 수익률. Fama & French (1993)가 정의한 채권 시장 팩터다.

이 스프레드가 크면 → 장기 경제 전망이 불확실하다 / 인플레이션 기대가 높다. 경기 확장기에 커지는 경향이 있다.

#### 6. DEF (부도 스프레드)

> Fama and French (1993) ... DEF

**뜯기**:

DEF = 회사채 수익률 - 국채 수익률. "디폴트 스프레드"라고도 한다.

이 스프레드가 크면 → 기업 부도 위험이 높다 → 경제가 불안하다. 경기 침체기에 급등한다 (2008년 리먼 때 폭등).

---

### 글로벌 변수 구성

> "Here, we use global long-run consumption growth, which is a GDP-weighted average of 12-quarter-ahead nondurable and service per capita consumption growth in the United States, the United Kingdom, Europe, and Japan. Global macroeconomic data are obtained from Economic Cycle Research Institute (ECRI), which covers production and consumption data as well as business cycle dates using the same methodology as the NBER for approximately 50 countries over time."

### 뜯기

미국만 보면 안 되니까, **글로벌 버전**도 만든다:

| 변수 | 글로벌 구성법 |
|------|-----------|
| 소비 성장 | 미국/영국/유럽/일본의 GDP 가중 평균 |
| 경기침체 더미 | ECRI 데이터 (~50개국), GDP 가중 평균 |
| GDP 성장 | 각국 GDP의 GDP 가중 평균 |
| 시장 수익률 | MSCI World Index (T-bill 차감) |
| TERM | **미국 것 그대로 사용** (국제 데이터 부재) |
| DEF | **미국 것 그대로 사용** (국제 데이터 부재) |

TERM과 DEF를 미국 것으로 쓰는 이유가 솔직하다: **"since we do not have data to construct TERM and DEF internationally, we use the U.S. versions."** 데이터가 없으니 어쩔 수 없다. 이건 한계점이다.

---

### Table III: Macroeconomic Risk Exposures (p.957)

> Reported are coefficient estimates, t-statistics (in parentheses), and R²s from time-series regressions of the value and momentum strategy returns in U.S. individual stocks, global individual stocks (across the United States, the United Kingdom, Europe, and Japan), nonstock asset classes, and all asset classes (stock and nonstock) on various measures of macroeconomic risks.

이 테이블은 4개 블록(U.S. Stocks, Global Stocks, Nonstock Assets, All Asset Classes) x 2개 종속변수(Value, Momentum)로 구성된다. 각 블록에서 6개 독립변수의 계수와 t-통계량을 보고한다.

#### 핵심 숫자 정리

| 독립변수 | U.S. Value | U.S. Mom | Global Value | Global Mom | Nonstock Value | Nonstock Mom | All Value | All Mom |
|---------|-----------|---------|-------------|-----------|---------------|-------------|----------|--------|
| **Long-run consumption** | 0.0004 (2.06) | 0.0001 (0.33) | 0.0001 (0.93) | 0.0001 (0.92) | 0.0001 (0.68) | 0.0001 (0.31) | 0.0001 (1.01) | 0.0001 (0.43) |
| **Recession dummy** | -0.0068 (-1.06) | -0.0056 (-0.73) | 0.0037 (-0.75) | -0.0044 (-0.75) | 0.0045 (1.48) | -0.0081 (-2.41) | 0.0043 (1.55) | -0.0072 (-2.26) |
| **GDP growth** | -0.0050 (-1.75) | 0.0019 (0.57) | -0.0011 (-0.39) | 0.0023 (0.80) | -0.0005 (-0.32) | -0.0034 (-2.08) | -0.0006 (-0.45) | 0.0020 (-1.29) |
| **Market** | -0.3435 (-1.46) | 0.0219 (0.40) | -0.0615 (-1.41) | -0.0709 (-1.55) | 0.0101 (0.44) | -0.0083 (-0.32) | -0.0068 (-0.32) | -0.0231 (-0.93) |
| **TERM** | 0.2038 (2.64) | -0.0234 (-0.27) | 0.0523 (1.04) | 0.0141 (0.27) | -0.0885 (-3.30) | 0.0370 (1.25) | -0.0551 (-2.22) | 0.0316 (1.11) |
| **DEF** | -0.3539 (-5.25) | -0.4733 (-5.57) | 0.2660 (0.26) | -0.3572 (-6.37) | 0.0310 (-3.03) | -0.0187 (-0.44) | 0.0240 (0.56) | -0.1480 (-2.94) |
| **R-squared** | **13.1%** | **5.9%** | **2.3%** | **6.4%** | **3.4%** | **2.9%** | **2.9%** | **4.7%** |

---

### 본문 해석: U.S. Stocks (p.956)

> "As Table III shows, U.S. stock value strategies are positively related to long-run consumption growth in U.S. data, consistent with the findings of Parker and Julliard (2005), Bansal and Yaron (2004), Malloy, Moskowitz, and Vissing-Jorgensen (2009), and Hansen, Heaton, and Li (2008)."

### 뜯기

**미국 가치 ← 장기 소비 성장: 양(+), t=2.06**

이것이 의미하는 바: 미래 소비가 잘 성장할 때 가치 전략도 수익이 좋다. 이건 소비 기반 자산가격결정 이론(CCAPM)과 **일치**하는 결과다.

왜 일치하는가? 가치주(value stock)는 대체로 경기에 민감한 기업들이다 — 철강, 은행, 자동차. 경제가 좋아지면(소비가 늘면) 이 기업들이 잘 된다. 경제가 나빠지면 크게 망한다. 이 "위험"에 대한 보상이 가치 프리미엄이라는 설명.

인용된 논문들의 맥락:
- **Parker & Julliard (2005)**: 장기 소비 베타로 가치 프리미엄 설명 시도
- **Bansal & Yaron (2004)**: Long-run risks 모형 — 장기 소비 성장의 불확실성이 자산 가격을 결정
- **Malloy, Moskowitz, Vissing-Jorgensen (2009)**: 부유층의 소비 성장이 자산 가격에 더 중요
- **Hansen, Heaton, Li (2008)**: 소비와 자산 수익률의 장기 관계

> "U.S. stock momentum strategy returns are not related to long-run consumption growth."

**미국 모멘텀 ← 장기 소비 성장: t=0.33, 무관**

모멘텀은 소비 성장과 아무 관계가 없다. 소비 기반 모형으로 모멘텀을 설명할 수 없다는 뜻.

> "Value and momentum are slightly negatively related to recessions and GDP growth, but none of these relationships are statistically significant."

경기침체와 GDP 성장에 대해서는 둘 다 약하게 음(-)이지만, 통계적으로 유의하지 않다. "경기가 나쁘면 둘 다 약간 손해"인데, 확실하지 않다.

> "TERM and DEF are positively related to value and the default spread is negatively related to momentum."

**TERM → 가치: 양(+)**, **DEF → 모멘텀: 음(-)**

TERM이 높을 때(장기 금리 > 단기 금리, 경기 확장 시그널) 가치가 좋다. DEF가 높을 때(부도 위험 ↑, 경기 악화 시그널) 모멘텀이 나쁘다.

DEF와 모멘텀의 관계가 특히 강하다: t=-5.57. 부도 스프레드가 벌어지면 모멘텀이 크게 손해본다.

---

### 본문 해석: 글로벌 (p.956~958)

> "the global macroeconomic variables are generally not significantly related to value and momentum returns, with a couple of exceptions."

### 뜯기

글로벌로 가면 **거의 다 유의하지 않다**. R-squared를 보라: 글로벌 주식 2.3%/6.4%, 비주식 3.4%/2.9%, 전체 2.9%/4.7%. 거시 변수 6개를 다 넣어도 수익률 변동의 **95% 이상을 설명하지 못한다**.

예외 두 가지:

> "Momentum is significantly negatively related to recessions, especially among nonstock asset classes."

**모멘텀과 경기침체: 비주식에서 유의하게 음(-)**

비주식 모멘텀의 침체 더미 계수: -0.0081 (t=-2.41). 전체 자산군: -0.0072 (t=-2.26). 경기침체가 오면 모멘텀이 크게 하락한다.

왜? 경기침체는 종종 갑작스럽게 온다. 모멘텀은 "오르던 것이 계속 오른다"에 베팅하는데, 침체가 오면 **추세가 급반전**된다. 오르던 자산이 갑자기 추락하고, 떨어지던 자산이 반등한다. 모멘텀에게는 최악의 시나리오.

> "DEF is consistently negatively related to momentum returns in all asset classes."

**DEF와 모멘텀: 전 자산군에서 일관되게 음(-)**

이건 중요한 패턴이다. 부도 스프레드가 벌어지면(금융 스트레스 ↑) 모멘텀이 손해본다. 미국뿐 아니라 **어디서나**. 유동성 섹션의 복선이다.

> "The default spread is positively related to global stock value, but is insignificantly negatively related to value returns in other asset classes."

DEF와 가치: 글로벌 주식에서만 양(+), 나머지는 무관. 부도 위험이 높을 때 가치주가 좋다? 직관과 맞다 — 부도 위험이 높은 시기에 "싸 보이는" 주식이 특히 싸게 거래되고, 나중에 회복하면 크게 오르니까.

---

### 거시경제 섹션의 결론

R-squared가 전부 한 자릿수다. 거시경제 변수 6개로는 가치와 모멘텀의 공통 변동을 **거의 설명하지 못한다**. 소비, GDP, 경기침체, 시장 수익률 — 전통적인 거시 리스크 팩터들이 무력하다.

이것이 의미하는 바: **"가치와 모멘텀이 위험 자산이라서 프리미엄을 받는다"**는 가장 기본적인 설명이 데이터에서 지지받지 못한다. 적어도 전통적 거시 변수로 측정한 "위험"으로는 안 된다.

그래서 논문은 다른 종류의 리스크 — **유동성 리스크** — 로 넘어간다.

---

## B. Liquidity Risk Exposure (p.958~963)

> "Table IV reports results from regressions that add various liquidity risk proxies to the macroeconomic variables above."

### 뜯기

거시경제 변수만으로는 부족했다. 이제 **유동성(liquidity)** 변수를 추가한다.

유동성이란 무엇인가? **"내가 원하는 때에, 원하는 가격에, 원하는 양을 거래할 수 있는 능력."** 유동성이 좋으면 거래가 쉽고, 나쁘면 팔고 싶어도 제값에 팔 수 없다.

논문은 유동성을 두 가지로 나눈다:
1. **펀딩 유동성(Funding liquidity)** — 돈을 빌릴 수 있는 능력
2. **시장 유동성(Market liquidity)** — 자산을 사고팔 수 있는 용이성

이 구분은 **Brunnermeier & Pedersen (2009)**의 이론에서 온다. 저자 중 한 명인 Pedersen이 바로 그 이론의 설계자다.

---

### B.1. Measuring Funding and Market Liquidity (p.958~959)

> "To measure liquidity risk exposure, we regress value and momentum returns on shocks to liquidity. We follow Moskowitz and Pedersen (2012) to define our liquidity shocks. We consider both funding liquidity shocks (e.g., Brunnermeier and Pedersen (2009)) and market liquidity shocks."

### 뜯기: 펀딩 유동성 변수 3개

#### 1. TED spread

> "The funding liquidity variables are the Treasury-Eurodollar (TED) spread (the average over the month of the daily local 3-month interbank LIBOR interest rate minus the local 3-month government rate)"

**TED 스프레드** = 3개월 LIBOR - 3개월 국채 금리

LIBOR는 은행끼리 돈을 빌려줄 때의 금리다. 국채 금리는 정부에 빌려주는 금리다. 정부는 절대 안 망하지만 은행은 망할 수 있다. 그 차이가 TED 스프레드다.

- TED가 높다 → 은행들이 서로를 신뢰하지 않는다 → 금융 스트레스 ↑ → 펀딩 유동성 ↓
- TED가 낮다 → 은행 간 신뢰 높다 → 돈 빌리기 쉽다 → 펀딩 유동성 ↑

2008년 9월 리먼 파산 때 TED 스프레드가 4.6%까지 치솟았다 (평소 0.2~0.5%).

#### 2. LIBOR - term repo spread

> "the LIBOR minus term repo spread (the spread between the local 3-month LIBOR rate and the local term repurchase rate)"

3개월 LIBOR - 3개월 RP(환매조건부채권) 금리.

RP(Repo)는 채권을 담보로 돈을 빌리는 거래다. 담보가 있으니 LIBOR(무담보)보다 싸다. 이 차이가 크면 → 담보 없이는 돈 빌리기 어렵다 → 펀딩 스트레스.

#### 3. Swap - T-bill spread

> "the spread between interest rate swaps and local short-term government rates (Swap-T-bill)"

금리스왑 금리 - 단기국채 금리.

금리스왑은 고정금리와 변동금리를 교환하는 계약이다. 이 스프레드가 크면 → 금융 시스템의 신용 리스크가 높다.

#### 4개 시장에서 측정

> "in each of the four markets"

미국, 영국, 일본, 유럽(독일 → 유로). 4개 시장 각각에서 이 3개 스프레드를 측정한다.

#### 부호 규칙

> "We sign every variable so that it represents liquidity. Hence, we take the negative of the TED spread and the other spreads so that they capture liquidity, since a wider spread represents worse liquidity."

스프레드가 크면 유동성이 **나쁜** 것인데, 변수를 **음수화**해서 "변수가 높으면 유동성이 좋다"로 통일한다. 즉:

- TED 변수 = -TED spread
- 나머지도 마찬가지

이렇게 하면 해석이 일관된다: **변수가 양(+)으로 움직이면 유동성 개선, 음(-)으로 움직이면 유동성 악화.**

#### Funding liquidity PC (펀딩 유동성 주성분)

> "we take the first principal component of the correlation matrix of all funding liquidity shocks"

3개 스프레드 x 4개 시장 = 12개 변수. 이걸 하나로 합치기 위해 **주성분 분석(PCA)**을 쓴다. 첫 번째 주성분(PC1)이 "글로벌 펀딩 유동성" 인덱스가 된다.

왜 **상관(correlation)** 행렬이고 **공분산(covariance)** 행렬이 아닌가? 변수들의 단위와 변동성이 다르기 때문이다. TED 스프레드와 Swap-T-bill 스프레드는 크기가 다르다. 공분산 행렬을 쓰면 변동성이 큰 변수가 PC를 지배해버린다. 상관 행렬은 모든 변수를 표준화한 뒤 추출하므로 공정하다.

---

### 뜯기: 시장 유동성 변수 3개

#### 1. On-the-run - off-the-run spread

> "The market liquidity variables are the on-the-run minus off-the-run 10-year government Treasury note spread (see Krishnamurthy (2002))"

**On-the-run** = 가장 최근에 발행된 국채. **Off-the-run** = 바로 직전에 발행된 국채.

둘 다 만기가 거의 같은 국채인데, 새로 발행된 것이 더 활발하게 거래된다. 그래서 on-the-run이 약간 더 비싸다(금리가 낮다). 이 차이가 크면 → 투자자들이 유동적인 자산에 프리미엄을 많이 지불한다 → 시장 유동성이 나쁘다.

Krishnamurthy (2002)가 이 측정법을 체계화했다.

#### 2. Pastor-Stambaugh (2003) 유동성 측도

> "the Pastor and Stambaugh (2003) liquidity measure (their factor, not their factor mimicking portfolio; specifically, their innovations obtained from CRSP)"

Pastor-Stambaugh는 주식시장에서 "거래량 충격이 가격에 미치는 영향"으로 유동성을 측정한다. 큰 거래가 가격을 많이 움직이면 → 유동성이 나쁘다.

**중요한 구분**: 그들의 "팩터(factor)" 자체를 쓰지, "팩터 모방 포트폴리오(FMP)"를 쓰지 않는다. FMP는 유동성에 민감한 주식들로 만든 포트폴리오인데, 이건 유동성의 간접 측정이다. 논문은 직접 측정을 쓴다.

#### 3. Acharya-Pedersen (2005) 비유동성 측도

> "the illiquidity measure of Acharya and Pedersen (2005), motivated by Amihud's (2002) measure"

Amihud (2002)의 비유동성 = |수익률| / 거래대금. 큰 거래대금에 비해 가격이 많이 움직이면 비유동적이다. Acharya-Pedersen (2005)이 이걸 자산가격결정 모형에 통합했다.

논문은 이 값의 **음수**를 사용한다: 높으면 유동성이 좋은 것.

#### 미국 외 시장 확장

> "We construct the Pastor and Stambaugh (2003) and Acharya and Pedersen (2005) measures in other countries by following their methodologies applied to stocks in those markets."

PS와 AP 측도는 원래 미국 주식만 대상이었는데, 논문이 **직접** 영국/유럽/일본에도 같은 방법론을 적용해서 만들었다. 이건 이 논문의 독자적 기여다.

---

### AR(2) 잔차로 쇼크 추정

> "We define shocks to these variables as the residuals from an AR(2) model, following Korajczyk and Sadka (2008) and Moskowitz and Pedersen (2012)."

왜 원시 수준(level)이 아니라 **쇼크(shock)**를 쓰는가?

유동성 수준 자체는 천천히 변한다. TED 스프레드가 높은 상태가 몇 달 지속될 수 있다. 하지만 자산 가격은 **예상치 못한 변화**에 반응한다. 그래서 AR(2) 모형으로 "예측 가능한 부분"을 제거하고, **잔차(residual) = 예상치 못한 변화 = 쇼크**만 추출한다.

AR(2)란: $X_t = a + b_1 X_{t-1} + b_2 X_{t-2} + \varepsilon_t$. 과거 2기의 값으로 현재를 예측하고, 예측 오차($\varepsilon_t$)가 쇼크.

> **각주 17**: "There is no special or theoretical reason to use an AR(2). An AR(3), AR(1), and first differences model yield similar results."

AR(2)를 쓴 데 특별한 이론적 근거는 없다. AR(1), AR(3), 단순 차분(first differences)도 비슷한 결과. **결과가 모형 선택에 민감하지 않다**는 뜻이므로 오히려 좋은 소식이다. 어떤 방법으로 쇼크를 정의하든 같은 패턴이 나온다.

---

### 각주 18: 제외된 변수들

> **각주 18**: A previous version of this paper also included the liquidity measures of Sadka (2006) and Adrian and Shin (2010) and found similar results. However, because the Sadka (2006) and Adrian and Shin (2009) measures require data not available in other equity markets, such as tick and trade data and balance sheet information from prime brokers, we cannot compute them internationally and hence omit them.

Sadka (2006)의 측도는 개별 거래(tick) 데이터가 필요하고, Adrian & Shin (2010)은 프라임 브로커의 대차대조표 정보가 필요하다. 미국에서는 구할 수 있지만, 영국/유럽/일본에서는 없다. "Everywhere"를 하려면 모든 시장에서 같은 변수를 써야 하므로, 이 둘은 제외했다.

---

### 기간과 최종 구성

> "The funding series are available for the common period January 1987 to July 2011."

1987년 1월 ~ 2011년 7월. 약 24.5년. 유동성 데이터의 가용 기간이 주식 데이터(1972~)보다 짧다.

**최종 유동성 지표 구성**:

| 지표 | 구성 |
|------|------|
| Funding liquidity PC | 3개 스프레드 x 4개 시장 → 12개 변수의 상관행렬 PC1 |
| Market liquidity PC | 3개 시장유동성 변수 x 4개 시장 → PC1 |
| All liquidity PC | Funding PC + Market PC + 개별 쇼크 전부 → 전체 PC1 |

---

## Figure 3: Time Series of Global Liquidity Shocks (p.961)

> "Figure 3 plots the time series of the index of all global liquidity shocks monthly from January 1987 to July 2011. The plot shows that our constructed global liquidity shocks capture a dozen of the largest known liquidity events in global markets over the last 25 years, including the 1987 stock market crash, decimalization, September 11, 2001, the quant meltdown of August 2007, Bear Stearns, and the Lehman Brothers bankruptcy."

### 뜯기

이 그래프는 논문이 구축한 "글로벌 유동성 쇼크 인덱스"가 **실제 위기를 잘 포착하는지** 보여주는 검증이다.

y축: 글로벌 유동성 쇼크 (AR(2) 잔차)
x축: 시간 (1987/07 ~ 2010/01)

그래프에 표시된 주요 이벤트들:

| 이벤트 | 시기 | 무슨 일이었나 | 유동성 영향 |
|--------|------|----------|---------|
| **1987 crash** | 1987.10 | 블랙 먼데이. 하루에 22% 폭락 | 급격한 유동성 고갈 (큰 음의 스파이크) |
| **Gulf War** | 1990~91 | 걸프전. 이라크의 쿠웨이트 침공 | 불확실성 → 유동성 악화 |
| **1/8 to 1/16 ticks** | ~1997 | 미국 주식시장 최소호가단위 변경 (12.5센트 → 6.25센트) | 거래비용 감소 → 유동성 개선 (양의 스파이크) |
| **Euro** | 1999.01 | 유로화 도입 | 유럽 금융시장 통합 → 유동성 개선 |
| **LTCM** | 1998.08~10 | 롱텀캐피탈매니지먼트 파산 | 글로벌 유동성 위기 (큰 음의 스파이크) |
| **Decimalization** | 2001 | 미국 주식 가격 소수점 표시 전환 | 스프레드 축소 → 유동성 개선 |
| **Sept. 11** | 2001.09 | 9/11 테러 | 시장 셧다운 → 유동성 고갈 |
| **Quant meltdown** | 2007.08 | 퀀트 헤지펀드 대량 손실 | 디레버리징 → 유동성 악화 |
| **Bear Stearns** | 2008.03 | 베어스턴스 붕괴/인수 | 투자은행 유동성 위기 |
| **FAS 157** | 2007.11 | 공정가치 회계 기준 도입 | 자산 평가 혼란 → 유동성 악화 |
| **Lehman Bros.** | 2008.09 | 리먼 브라더스 파산 | **역사상 최대 유동성 위기** (그래프 최저점, ~-0.30) |
| **Market recovery** | 2009~ | 양적완화 시작, 시장 회복 | 유동성 급격 개선 (큰 양의 스파이크) |

핵심: 이 인덱스는 "실험실에서 만든 숫자"가 아니라, **실제로 위기를 포착한다**. 리먼 파산 때 가장 큰 음의 쇼크, 시장 회복 때 가장 큰 양의 쇼크. 측정이 신뢰할 만하다는 시각적 증거.

---

## B.2. Value and Momentum Returns and Liquidity Risk (p.960~962)

> "Table IV reports regression results of value and momentum returns on the liquidity shocks, controlling for the macro variables in Table III. We only report the coefficient estimates on the liquidity shocks for brevity and because the coefficient estimates on the macro variables do not change much with the addition of the liquidity variables."

### 뜯기

핵심 방법론: Table III의 거시 변수 6개를 **통제한 상태에서**, 유동성 쇼크를 추가로 넣는다. 즉 "거시 변수로 설명되는 부분을 빼고도, 유동성이 추가적으로 설명하는 부분이 있는가?"를 검증한다.

거시 변수의 계수는 유동성을 추가해도 거의 안 변한다 → 유동성은 거시와 **다른 정보**를 담고 있다.

---

### Table IV Panel A: U.S. Liquidity Risk Measures (p.959)

4개 열: Value / Momentum / 50/50 Combination / Val-Mom (가치 - 모멘텀 차이)

#### 펀딩 유동성

| 변수 | Value | Momentum | 50/50 Combo | Val - Mom |
|------|-------|----------|-------------|-----------|
| **TED spread** | -0.0052 (-1.44) | 0.0129 **(3.07)** | 0.0061 **(2.13)** | -0.0180 **(-2.62)** |
| **LIBOR-repo** | -0.0137 **(-2.15)** | 0.0087 (1.11) | -0.0058 (-1.26) | -0.0223 (-1.71) |
| **Swap-T-bill** | -0.0002 (-0.05) | 0.0141 **(3.34)** | 0.0104 **(3.67)** | -0.0143 **(-2.04)** |
| **Funding PC** | -0.0111 **(-2.89)** | 0.0153 **(3.31)** | 0.0042 (1.49) | **-0.0264 (-3.41)** |

#### 시장 유동성

| 변수 | Value | Momentum | 50/50 Combo | Val - Mom |
|------|-------|----------|-------------|-----------|
| **On-off** | 0.0063 (0.53) | -0.0053 (-0.38) | -0.0043 (-0.50) | 0.0115 (0.49) |
| **Pastor-Stambaugh** | 0.0034 (0.32) | 0.0107 (0.89) | 0.0159 (1.93) | -0.0074 (-0.37) |
| **Acharya-Pedersen** | 0.0010 **(2.02)** | 0.0005 (1.44) | 0.0013 **(3.05)** | 0.0004 (0.70) |
| **Market PC** | -0.0080 (-0.44) | 0.0222 (0.94) | 0.0200 (1.06) | -0.0302 (-0.97) |

#### 전체 유동성

| 변수 | Value | Momentum | 50/50 Combo | Val - Mom |
|------|-------|----------|-------------|-----------|
| **All PC** | -0.0154 **(-2.84)** | 0.0195 **(2.96)** | 0.0043 (1.09) | **-0.0349 (-3.17)** |

---

### Table IV Panel B: Global Liquidity Risk Measures (p.960)

#### 펀딩 유동성

| 변수 | Value | Momentum | 50/50 Combo | Val - Mom |
|------|-------|----------|-------------|-----------|
| **TED spread** | -0.0067 (-1.69) | 0.0094 **(2.00)** | 0.0023 (0.74) | -0.0161 **(-2.05)** |
| **LIBOR-repo** | -0.0177 **(-2.87)** | 0.0139 (1.66) | -0.0005 (-0.08) | -0.0316 **(-2.36)** |
| **Swap-T-bill** | -0.0076 **(-2.15)** | 0.0055 (1.31) | -0.0012 (-0.46) | -0.0131 (-1.86) |
| **Funding PC** | **-0.0094 (-4.74)** | **0.0112 (3.58)** | 0.0013 (0.58) | **-0.0206 (-4.67)** |

#### 시장 유동성

| 변수 | Value | Momentum | 50/50 Combo | Val - Mom |
|------|-------|----------|-------------|-----------|
| **On-off** | 0.0108 (0.68) | -0.0001 (-0.01) | 0.0037 (0.32) | 0.0109 (0.34) |
| **Pastor-Stambaugh** | 0.0010 (0.39) | -0.0002 (-0.15) | 0.0003 (0.43) | 0.0011 (0.61) |
| **Acharya-Pedersen** | 0.0009 (1.06) | 0.0008 (0.28) | 0.0020 (1.30) | 0.0001 (0.02) |
| **Market PC** | -0.0009 (-0.74) | 0.0016 (1.00) | 0.0012 (1.21) | -0.0025 (-1.45) |

#### 전체 유동성

| 변수 | Value | Momentum | 50/50 Combo | Val - Mom |
|------|-------|----------|-------------|-----------|
| **All PC** | **-0.0079 (-3.25)** | **0.0093 (4.43)** | 0.0016 (0.82) | **-0.0172 (-4.63)** |

---

### 본문 해석: 펀딩 유동성 (p.960~961)

> "The first four rows of Panel A of Table IV show that funding liquidity risk is consistently negatively related to value returns and significantly positively related to momentum returns."

### 뜯기

**패턴이 명확하다**: 펀딩 유동성이 나빠지면(쇼크가 음이면):
- **가치: 올라간다** (계수가 음 = 유동성↓일 때 가치↑)
- **모멘텀: 내려간다** (계수가 양 = 유동성↓일 때 모멘텀↓)

글로벌 Funding PC 기준:
- Value: **-0.0094 (t=-4.74)** — 매우 유의
- Momentum: **+0.0112 (t=3.58)** — 매우 유의
- Val-Mom 차이: **-0.0206 (t=-4.67)** — 극도로 유의

**왜 반대 방향인가?**

> "Value performs poorly when funding liquidity rises, which occurs during times when borrowing is easier, while momentum performs well during these times."

직관적 설명:

**모멘텀** = 인기 있는 거래(crowded trade). 오르는 자산을 사고 떨어지는 자산을 파는 것. 돈 빌리기 쉬울 때 → 레버리지 늘림 → 모멘텀 거래에 더 많은 돈이 몰림 → 모멘텀 수익 ↑. 유동성 위기 때 → 디레버리징 → 가장 붐비는 거래(모멘텀)부터 매도 → 모멘텀 폭락.

**가치** = 역발상 거래(contrarian). 떨어진 자산을 사는 것. 유동성 위기 때 → 모두가 팔 때 → 가치주가 **더 싸지면서** 나중에 회복할 때 더 크게 오른다. 돈 빌리기 쉬울 때 → 모두가 인기 자산을 쫓아가서 → 가치주에 대한 관심 ↓.

Pedersen (2009)의 이론: 유동성 충격이 오면 → 투자자들이 현금 확보를 위해 투매(fire sale) → **붐비는 거래**(모멘텀)에 더 큰 가격 압력 → 한편 **인기 없는 거래**(가치)는 덜 영향받거나 오히려 기회가 됨.

---

### 각주 19: 대안 해석

> **각주 19**: "Another interpretation of these funding shocks is that they proxy for changes in risk aversion or risk premia in the economy... Under this alternative view, it would seem that both value and momentum returns would decline with rising spreads, whereas we find that value and momentum returns move in opposite directions with respect to these shocks."

### 뜯기

논문이 스스로 대안 해석을 제시하고 **반박**한다.

**대안 해석**: 펀딩 스프레드가 넓어지면 → 그건 단지 "위험 회피(risk aversion)"가 높아졌다는 신호 → 위험 프리미엄이 올라감.

**반박**: 만약 그렇다면, **가치와 모멘텀 모두** 스프레드가 넓어질 때 하락해야 한다 (둘 다 위험 자산이니까). 하지만 실제로는 **반대 방향**으로 움직인다. 이건 단순한 "위험 회피 변동" 설명과 맞지 않는다.

추가로, 회귀식에 시장 수익률과 거시 변수가 이미 포함되어 있어서 위험 회피/프리미엄 변동의 일부는 이미 통제되고 있다.

---

### 본문 해석: 시장 유동성 (p.961~962)

> "The next four rows examine market liquidity shocks in the U.S. market. Here, we find little relation between market liquidity shocks and value and momentum returns."

### 뜯기

시장 유동성은 **약하다**. 대부분 t-통계량이 2 미만.

유일한 예외: Acharya-Pedersen의 Value 계수 t=2.02, Combo t=3.05. 하지만 나머지는 전부 유의하지 않다.

> "Pastor and Stambaugh (2003) (and Sadka (2006)) find a positive and significant relation between U.S. equity momentum returns and their market liquidity shocks. We find the same sign as Pastor and Stambaugh (2003) for our global momentum returns across asset classes over our sample period, but do not detect a significant relation."

**핵심 대조**: Pastor-Stambaugh (2003)는 미국 주식에서 모멘텀과 시장 유동성의 유의한 관계를 발견했다. 이 논문도 같은 부호를 발견하지만, 글로벌로 확장하면 **유의하지 않다**.

왜? 두 가지 가능성:
1. PS의 결과가 미국 주식의 특수한 현상이었을 수 있다
2. 이 논문이 PS의 "팩터"를 쓰지 "팩터 모방 포트폴리오"는 안 쓰기 때문 — 논문은 팩터 자체가 더 직접적이고, FMP는 모멘텀과의 관계가 약하다고 지적

---

### 본문 해석: 글로벌 > 미국 (p.962)

> "Furthermore, the global measures, especially the funding liquidity index, seem to provide more statistical significance."

### 뜯기

글로벌 측정이 미국만의 측정보다 **더 유의하다**.

비교:
| 측정 범위 | Value Funding PC | Momentum Funding PC | Val-Mom All PC |
|----------|-----------------|--------------------|----|
| 미국만 | t=-2.89 | t=3.31 | t=-3.17 |
| 글로벌 | **t=-4.74** | **t=3.58** | **t=-4.63** |

글로벌 t-통계량이 훨씬 크다. 왜? 4개 시장의 데이터를 합치면 → **개별 시장의 노이즈가 상쇄**되고 → 진짜 신호가 더 선명하게 드러나기 때문. 이것이 "Everywhere"의 방법론적 위력.

---

### 핵심 발견: 반대 부호 로딩의 의미

> "The opposite signed loadings on liquidity risk for value and momentum may partially explain why the two strategies are negatively correlated."

### 뜯기

가치 = 유동성에 음(-) 로딩
모멘텀 = 유동성에 양(+) 로딩

같은 팩터에 반대 부호로 로딩하면, 당연히 둘은 **음의 상관**을 보인다. Section II에서 발견한 가치↔모멘텀의 음의 상관이 유동성 리스크에 대한 반대 노출로 **부분적으로** 설명된다.

---

### Deeper Puzzle: 왜 둘 다 양의 프리미엄? (p.962)

> "However, the opposite signed loadings on a single factor, such as liquidity risk, cannot explain why *both* value and momentum earn positive risk premia."

### 뜯기

이것이 이 섹션의 **가장 깊은 퍼즐**이다.

유동성 리스크가 양의 프리미엄을 가진다고 가정하자 (유동성이 나쁠 때 손해보는 자산은 보상받아야 하니까).

| 전략 | 유동성 로딩 | 유동성 프리미엄 | 결과 |
|------|---------|------------|------|
| **모멘텀** | **양(+)** | 양(+) | 양의 프리미엄 설명 OK |
| **가치** | **음(-)** | 양(+) | **음의 프리미엄이어야 함!** |

모멘텀은 유동성이 나빠질 때 손해본다 → 위험하다 → 프리미엄을 받는다. 논리 OK.

가치는 유동성이 나빠질 때 **오히려 이득**을 본다 → "보험" 역할 → **프리미엄을 내야** 한다 (보험에 돈을 주듯이). 그런데 실제로는 가치도 **양의** 프리미엄을 받는다. 왜?

> "On the other hand, value loads negatively on liquidity risk, which makes its positive return an even deeper puzzle."

유동성 리스크만으로는 가치 프리미엄을 **전혀 설명할 수 없다**. 오히려 퍼즐을 더 깊게 만든다.

---

### 50/50 조합의 면역성 (p.962)

> "Finally, as Table IV shows, because of the opposite signed exposure of value and momentum to funding liquidity shocks, the 50/50 equal combination of value and momentum is essentially immune to funding shocks, and yet, as we have shown, generates huge positive returns."

### 뜯기

Table IV에서 50/50 Combo의 Funding PC 계수를 보라:
- 미국: 0.0042 (t=1.49) — 유의하지 않음
- 글로벌: 0.0013 (t=0.58) — 유의하지 않음

가치의 음(-) 로딩과 모멘텀의 양(+) 로딩이 **거의 정확히 상쇄**된다. 50/50 조합은 유동성 리스크에 거의 노출되지 않는다.

그런데 이 조합은 **엄청난 수익을 낸다** (Section II에서 샤프 비율 1.59). 유동성 리스크로 설명할 수 없는 수익이다.

> "Thus, while exploring liquidity risk's relation to value and momentum more deeply may be interesting, liquidity risk by itself cannot explain why a combination of value and momentum is so profitable."

**결론**: 유동성 리스크는 가치와 모멘텀의 **음의 상관**을 부분적으로 설명하지만, 둘 다 **양의 수익**을 내는 이유는 설명하지 못한다. 특히 50/50 조합의 높은 수익은 완전한 미스터리로 남는다.

---

### 왜 모멘텀이 양으로, 가치가 음으로 로딩하는가? (p.962)

> "Why does momentum load positively and value load negatively on liquidity risk? One simple and intuitive story might be that momentum captures the most popular trades, being long the assets whose prices have recently appreciated as fickle investors flocked to these assets."

### 뜯기

**모멘텀 = 붐비는 거래(crowded trade)**

최근에 오른 자산 매수 → 변덕스러운 투자자들이 몰려든 자산. 유동성 위기가 오면 → "현금 확보"를 위한 투매 → 가장 붐비는 거래에 가격 압력이 집중 → 모멘텀 포트폴리오가 폭락.

> "Value, on the other hand, expresses a contrarian view, where assets have experienced price declines over several years. When a liquidity shock occurs, investor liquidations (from cash needs, redemptions, risk management, 'running for the exit' at the same time; see Pedersen (2009)) puts more price pressure on the more 'crowded' trades."

**가치 = 역발상 거래(contrarian)**

수년간 떨어진 자산 매수. 아무도 관심 없는 자산. 유동성 위기 때 투매 압력이 이 자산들에는 적게 작용한다 — 이미 아무도 안 가지고 있으니 팔 것도 없다. 오히려 위기 후 회복 때 더 크게 반등할 수 있다.

> "These liquidations may affect crowded high momentum securities more than the less popular contrarian/value securities."

Pedersen (2009)의 핵심: 유동성 충격 → 모두가 동시에 출구로 달려간다("running for the exit") → 붐비는 포지션(모멘텀)이 가장 큰 타격.

---

## B.3. The Power of Averaging Across Markets (p.963~964)

> "A key feature of the analysis in Tables III and IV is that we examine the average returns to value and momentum across a wide set of markets and asset classes simultaneously."

### 뜯기

이 하위 섹션은 논문의 **방법론적 핵심**을 정당화한다: 왜 "Everywhere"가 중요한가.

---

### Figure 4: Liquidity risk beta t-statistics (p.963)

> "Figure 4 depicts the t-statistics of the liquidity betas of each of our individual market and asset class value and momentum strategies."

### 뜯기

이 막대그래프는 논문의 가장 설득력 있는 시각화 중 하나다.

**구조**:
- x축: 8개 개별 시장/자산군 + Average + All asset classes
- y축: 유동성 리스크 베타의 t-통계량
- 파란 막대: Value, 주황 막대: Momentum

**개별 시장의 t-통계량**:

각 시장을 **따로** 보면:
- 가치의 유동성 베타 t-stat 평균: **-0.95** (유의하지 않음! |t| < 2)
- 모멘텀의 유동성 베타 t-stat 평균: **1.81** (거의 유의하지만 아슬아슬)

개별 시장별로 보면 "유동성 리스크와 가치/모멘텀의 관계? 별로 없는데?"라고 결론내릴 수 있다.

**평균 수익률 시리즈의 t-통계량**:

모든 시장의 수익률을 **평균**해서 하나의 시리즈로 만들면:
- 가치: **t = -3.25** (매우 유의!)
- 모멘텀: **t = 4.43** (극도로 유의!)

**같은 데이터**인데 분석 방법만 다르다. 개별로 보면 안 보이고, 합치면 선명하게 보인다.

> "The average liquidity beta among the individual strategies is not nearly as strong as the liquidity beta of the average."

### 뜯기

"개별 전략들의 유동성 베타의 평균"과 "평균 전략의 유동성 베타"는 **같지 않다**. 후자가 훨씬 강하다.

왜? **노이즈 감소** 때문이다.

각 시장의 가치/모멘텀 수익률에는:
- **신호(signal)**: 유동성 리스크에 대한 진짜 노출
- **노이즈(noise)**: 그 시장만의 고유한 잡음 (개별 기업 뉴스, 지역 정책 등)

개별 시장을 따로 분석하면 신호가 노이즈에 묻힌다. 하지만 8개 시장을 평균하면 → **노이즈는 상쇄**되고(서로 다른 방향이니까) → **신호는 누적**된다(같은 방향이니까).

라디오 비유: 8개 라디오에서 같은 방송을 들으면서 평균하면, 잡음은 사라지고 방송만 선명해진다.

> "Averaging across all markets and asset classes mitigates much of the noise not related to value or momentum, such as idiosyncratic regional or asset-specific noise, allowing for better identification of a common factor such as liquidity risk to emerge."

### 뜯기

"특이적(idiosyncratic) 지역 노이즈나 자산 고유 노이즈"가 사라진다. 남는 것은 가치와 모멘텀에 **공통적으로** 관련된 요인 — 유동성 리스크 같은 것.

> "When we restrict attention to one asset class at a time, or to one strategy within an asset class, the patterns above are difficult to detect."

한 번에 하나의 자산군만 보면, 또는 하나의 전략만 보면, 이 패턴은 **발견할 수 없다**. 기존 연구들이 "미국 주식에서 모멘텀만" 또는 "미국 주식에서 가치만" 봤던 것이 왜 유동성과의 관계를 놓쳤는지를 설명한다.

---

### 이 섹션의 핵심 문장 (p.964)

> "The scope and uniformity of studying value and momentum everywhere at once is what allows these patterns to be identified."

### 뜯기

이 한 문장이 Section III 전체의, 그리고 어쩌면 논문 전체의 방법론적 핵심이다.

"Everywhere"는 단순히 "여러 시장을 조사했다"가 아니다. **"여러 시장을 동시에 보는 것 자체가 발견을 가능하게 한다"**는 것이다.

- **scope(범위)**: 8개 시장/자산군
- **uniformity(통일성)**: 같은 측정법, 같은 기간, 같은 방법론
- **at once(동시에)**: 개별이 아니라 한꺼번에

이 세 가지가 합쳐져서 노이즈를 줄이고 신호를 증폭한다. "Everywhere"가 단순한 범위 확장이 아니라 **통계적 파워의 원천**이라는 것이 이 섹션의 최종 교훈이다.

---

## 이 섹션에서 배운 것

| # | 핵심 발견 | 근거 |
|---|---------|------|
| 1 | 전통적 거시 변수로는 가치/모멘텀의 공통 변동을 설명 못함 | Table III: R-squared 전부 한 자릿수 |
| 2 | **펀딩 유동성**은 유의한 설명력 보유 | Table IV: Funding PC t-stat -4.74 / +3.58 |
| 3 | 가치는 유동성에 **음(-)**, 모멘텀은 **양(+)** | 반대 부호 = 음의 상관 부분 설명 |
| 4 | 시장 유동성은 약하고 유의하지 않음 | Table IV: Market PC 전부 유의하지 않음 |
| 5 | 유동성 리스크는 모멘텀 프리미엄을 일부 설명하나 가치 프리미엄은 퍼즐을 심화 | 가치의 음(-) 로딩 → 보험 역할인데 양의 프리미엄? |
| 6 | 50/50 조합은 유동성에 면역이면서 높은 수익 → 유동성만으로 설명 불가 | Combo의 유동성 베타 t-stat ≈ 0 |
| 7 | 여러 시장 동시 분석이 통계적 파워의 핵심 원천 | Figure 4: 개별 t=-0.95 vs 전체 t=-3.25 |

---

## 여기서 멈추고 생각하기

### 🤔 추론 연습
1. **거시변수 실패 = 위험 보상 부정?** 거시변수로 설명이 안 된다면, 가치/모멘텀은 "거시경제 위험의 보상"이 아니라는 뜻인가? → 반드시 그렇지는 않다. 불완전한 거시 프록시일 수 있다. 소비성장 측정 자체가 노이즈가 많고, 분기별 GDP는 실시간 위험 인식을 반영하지 못한다.
2. **QE와 가치/모멘텀** 펀딩 유동성이 가치에 음(-), 모멘텀에 양(+)으로 작용한다. 만약 중앙은행이 유동성을 인위적으로 공급하면(QE), 모멘텀이 강해지고 가치가 약해질 것인가? → 2009~2020 QE 시대에 실제로 가치가 부진했다는 현실과 일치한다. 이 논문의 유동성 분석이 미래를 예측한 셈이다.
3. **"평균의 힘"의 범용성** Figure 4의 논리를 다른 연구에도 적용할 수 있는가? 예: 기후 변화 데이터도 개별 측정소는 노이즈가 크지만 전 지구 평균은 추세가 선명하다. "여러 시장을 동시에 보는 것 자체가 발견을 가능하게 한다"는 원리는 금융을 넘어 범용적이다.

### ⚡ 비판적 사고
1. **AR(2) 잔차 측정의 자의성** 유동성 쇼크를 AR(2) 잔차로 측정하는 것이 최선인가? AR(2) 선택에 "특별한 이유 없다"고 각주 17에서 저자 스스로 인정한다. AR(1)이나 AR(3)이면 결과가 달라질 수 있다.
2. **미국 중심 편향** 미국 TERM/DEF를 국제 시장에도 대체 사용한다 — 이건 "글로벌"을 표방하면서 거시변수는 미국 중심이라는 내적 모순 아닌가? 각국의 고유한 금리 구조와 신용 스프레드를 무시하는 셈이다.

> **다음**: [dissect-06 Comovement and Asset Pricing Tests 해체](dissect-06-pricing.md) — Section IV. 글로벌 3팩터 모형으로 48개 포트폴리오의 수익률을 설명한다.
