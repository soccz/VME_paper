# 논문 해체 6: 공변동과 자산가격결정 검정 (Section IV, p.964~975)

> Section II에서 발견한 강력한 공통 팩터 구조, Section III에서 확인한 유동성 리스크와의 연결 -- 이 두 가지가 합쳐져서 자연스럽게 다음 질문으로 이어진다. **"그래서, 이걸 하나의 자산가격결정 모형으로 정리할 수 있는가?"** Section IV는 그 질문에 답한다. 총 12페이지, 수식 2개, 그림 2개(각각 다중 패널), 표 2개. 이 논문의 실증적 하이라이트다.

---

## Section IV 도입 (p.964)

> "The strong common factor structure evidenced in Section II and the link to liquidity risk in Section III suggest that we formally examine asset pricing tests to assess the economic significance of these patterns and how much of the return premia to value and momentum can be captured by this common variation."

### 뜯기

이 한 문장이 Section IV 전체의 로드맵이다. 단어별로 보자.

- **"strong common factor structure evidenced in Section II"** -- Section II에서 발견한 것: 가치 전략끼리 같이 움직이고, 모멘텀 전략끼리 같이 움직인다. 자산군이 달라도. 이건 "공통 팩터"가 있다는 증거다.

- **"link to liquidity risk in Section III"** -- Section III에서 발견한 것: 이 공변동의 원인 중 하나가 유동성 리스크, 특히 펀딩 유동성이다.

- **"formally examine asset pricing tests"** -- 지금까지는 "상관이 있다", "같이 움직인다" 수준이었다. 이제 **공식적인 자산가격결정 검정**을 한다. "공식적"이란 뭔가? 학계에서 인정하는 통계적 검정 프레임워크(GRS 검정, Fama-MacBeth 회귀 등)를 쓴다는 뜻이다.

- **"economic significance"** -- 통계적 유의성(p-value가 작다)과 경제적 유의성(돈으로 얼마나 되나)은 다르다. 여기서는 둘 다 본다.

- **"how much of the return premia... can be captured"** -- 가치/모멘텀 프리미엄의 몇 %를 모형이 설명할 수 있는가? 100%면 완벽한 모형, 0%면 쓸모없는 모형이다.

**왜 이게 필요한가?** Section II-III는 "현상 기술"이었다. "이런 패턴이 있고, 유동성과 관련 있다." 하지만 자산가격결정론에서는 한 단계 더 나아가야 한다 -- **하나의 모형으로 48개 포트폴리오의 기대수익률을 동시에 설명**할 수 있는가? 이것이 "자산가격결정 검정"이다.

> 📚 **더 깊이**: [ch09 자산가격결정 모형](../chapters/ch09-asset-pricing-models.md) -- CAPM에서 다팩터 모형까지 | [ch10 GRS 검정과 Fama-MacBeth](../chapters/ch10-grs-fama-macbeth.md)

---

## A. 한 시장의 가치/모멘텀을 다른 시장의 가치/모멘텀으로 설명하기 (p.964~966)

> "We first examine how well value and momentum in one market or asset class are explained by value and momentum returns in other asset classes. This test is not a formal asset pricing test, but a test of comovement across markets and asset classes. In the next subsection, we examine formal asset pricing tests. Specifically, we run the regression"

### 뜯기

저자들이 스스로 인정한다: 이건 **공식적인 자산가격결정 검정이 아니다**. 그냥 "공변동 검정"이다. 왜 먼저 이걸 하는가? 공식 검정(subsection B)으로 가기 전에 직관적으로 보여주기 위해서다. "다른 시장의 가치/모멘텀이 이 시장의 가치/모멘텀을 설명할 수 있는가?"

---

### 수식 (4): 다른 시장 팩터로 회귀

#### 말로 먼저

> "각 시장의 가치/모멘텀 포트폴리오 수익률을 **글로벌 시장 수익률** + **다른 모든 시장의 가치 팩터** + **다른 모든 시장의 모멘텀 팩터**로 회귀분석한다."

핵심은 "다른 모든 시장"이다. 미국 주식의 가치 포트폴리오를 설명할 때, 영국/유럽/일본 주식 + 선물 + 통화 + 채권 + 원자재의 가치/모멘텀 팩터를 쓴다. **미국 자체의 팩터는 쓰지 않는다.**

#### KaTeX 수식

$$R_{i,t}^{p} - r_{f,t} = \alpha_i^{p} + \beta_i^{p} \, MKT_t + v_i^{p} \sum_{j \neq i} w_j \, VAL_{j,t} + m_i^{p} \sum_{j \neq i} w_j \, MOM_{j,t} + \varepsilon_{i,t}^{p} \tag{4}$$

#### 기호 해설

| 기호 | 의미 | 구체적으로 |
|------|------|---------|
| $R_{i,t}^{p}$ | 시장 $i$의 포트폴리오 $p$의 $t$월 수익률 | 예: 미국 주식의 가치 High 포트폴리오의 2005년 3월 수익률 |
| $r_{f,t}$ | 무위험 이자율 | 미국 1개월 T-bill 금리 |
| $R_{i,t}^{p} - r_{f,t}$ | **초과수익률** | 무위험 이자를 뺀 순수한 "위험에 대한 보상" 부분 |
| $\alpha_i^{p}$ | **알파** (절편) | 모형이 설명하지 못하는 잔여 수익. 0이면 모형이 완벽 |
| $\beta_i^{p}$ | 시장 베타 | 글로벌 시장(MSCI World) 움직임에 대한 민감도 |
| $MKT_t$ | 글로벌 시장 포트폴리오 초과수익률 | MSCI World Index - T-bill |
| $v_i^{p}$ | 가치 팩터 로딩 | "다른 시장의 가치 팩터"에 대한 민감도 |
| $\sum_{j \neq i} w_j \, VAL_{j,t}$ | **다른 시장들의 가치 팩터 가중합** | $j \neq i$: 시장 $i$를 **제외한** 나머지 시장들만 |
| $w_j$ | 동일 변동성 가중치 | 각 자산군의 변동성이 같아지도록 조정하는 가중치 |
| $m_i^{p}$ | 모멘텀 팩터 로딩 | "다른 시장의 모멘텀 팩터"에 대한 민감도 |
| $\sum_{j \neq i} w_j \, MOM_{j,t}$ | **다른 시장들의 모멘텀 팩터 가중합** | 역시 시장 $i$ 제외 |
| $\varepsilon_{i,t}^{p}$ | 오차항 | 모형이 설명 못 하는 나머지 |

#### "$j \neq i$"의 의미: 왜 자기 시장을 빼는가?

이것이 이 수식의 핵심 설계다. 미국 주식의 가치 포트폴리오를 설명할 때 **미국 주식의 가치 팩터를 쓰면 안 된다**. 왜?

1. **기계적 상관**: 테스트 자산(좌변)과 팩터(우변)가 같은 증권으로 구성되면, 진짜 경제적 관계가 아니라 그냥 "같은 주식이 양쪽에 들어 있어서" 상관이 높게 나온다. 이건 사기다.

2. **독립적 검증**: $j \neq i$ 조건은 "증권의 겹침이 전혀 없음"을 보장한다. 미국 주식 포트폴리오에 들어 있는 애플, 구글은 영국/일본/통화/채권/원자재 팩터 어디에도 포함되지 않는다.

비유: 시험 문제를 만든 교수가 그 시험을 보고 100점 맞으면 아무 의미 없다. **다른 교수가 만든 시험으로 실력을 검증해야** 의미가 있다. $j \neq i$가 바로 "다른 교수의 시험"이다.

#### 48개 테스트 자산

8개 시장 × 6개 포트폴리오 = **48개**:

| 시장 | 가치 (H/M/L) | 모멘텀 (H/M/L) |
|------|-------------|--------------|
| 미국 주식 | Val_US^H, Val_US^M, Val_US^L | Mom_US^H, Mom_US^M, Mom_US^L |
| 영국 주식 | Val_UK^H, Val_UK^M, Val_UK^L | Mom_UK^H, Mom_UK^M, Mom_UK^L |
| 유럽 주식 | Val_EU^H, ... | Mom_EU^H, ... |
| 일본 주식 | Val_JP^H, ... | Mom_JP^H, ... |
| 주가지수 선물 | Val_EQ^H, ... | Mom_EQ^H, ... |
| 통화 | Val_FX^H, ... | Mom_FX^H, ... |
| 국채 | Val_FI^H, ... | Mom_FI^H, ... |
| 원자재 | Val_CM^H, ... | Mom_CM^H, ... |

H = High (상위), M = Middle (중위), L = Low (하위). 가치의 경우 H = BE/ME가 높은 (싼) 포트폴리오, L = BE/ME가 낮은 (비싼) 포트폴리오.

#### 숫자 예시

미국 주식의 가치 High 포트폴리오를 생각하자:

$$R_{\text{US},t}^{\text{Val}^H} - r_f = \alpha + \beta \cdot MKT_t + v \cdot \bigl(w_{\text{UK}} \cdot VAL_{\text{UK}} + w_{\text{EU}} \cdot VAL_{\text{EU}} + w_{\text{JP}} \cdot VAL_{\text{JP}} + \cdots\bigr) + m \cdot \bigl(w_{\text{UK}} \cdot MOM_{\text{UK}} + \cdots\bigr) + \varepsilon$$

우변의 가치/모멘텀 팩터에 미국(US)은 **없다**. 영국, 유럽, 일본, 선물, 통화, 채권, 원자재만 있다.

만약 $v$가 유의하게 양수로 나오면? → "미국 주식의 가치 포트폴리오가 좋을 때, **다른 나라의 가치 포트폴리오도** 좋다" → 글로벌 공통 가치 팩터가 존재한다는 증거.

> 📚 **더 깊이**: [ch11 시계열 회귀와 횡단면 회귀](../chapters/ch11-ts-xs-regression.md) -- 수식 (4)는 시계열 회귀(time-series regression)

---

### Figure 5: AMP 3-Factor Model (다른 시장 팩터만 사용) (p.965)

> "Figure 5 plots the actual average return of each of the test assets against the predicted expected return from the regression. The plot shows how much of the average returns to value and momentum portfolios in one market or asset class can be explained by value and momentum returns from other markets and asset classes. A 45° line passing through the origin is also plotted to highlight both the cross-sectional fit and the magnitude of the pricing errors across test assets."

#### 뜯기

Figure 5는 **산점도(scatter plot)** 하나다.

- **x축**: 수식 (4)의 회귀에서 나온 **예측 기대수익률**(predicted expected return). 모형이 "이 포트폴리오의 월평균 수익률은 이 정도일 것이다"라고 말하는 값.
- **y축**: 실제 **관측된 월평균 수익률**(actual average return). 데이터에서 직접 계산한 값.
- **각 점**: 48개 포트폴리오 중 하나. 라벨이 붙어 있다 -- `Val_US^H`, `Mom_JP^L` 같은 형태.

#### 45도선의 의미

모형이 완벽하면 예측값 = 실제값이므로 모든 점이 **45도 대각선** 위에 놓인다. 점이 대각선에서 멀수록 모형의 오류가 크다.

- 점이 대각선 **위**에 있으면: 실제 수익 > 예측 수익 → 모형이 설명 못 하는 **양의 알파**
- 점이 대각선 **아래**에 있으면: 실제 수익 < 예측 수익 → **음의 알파**

#### 핵심 통계

| 통계량 | 값 | 의미 |
|--------|---|------|
| $R^2$ | **0.55** | 48개 포트폴리오 평균수익률의 횡단면 변동 중 55%를 설명 |
| Average $\|\alpha\|$ | **0.00226** (22.6bp/월) | 평균적으로 각 포트폴리오가 월 22.6bp의 미설명 수익 |
| GRS 검정 | **불가** | 아래 설명 |

**22.6bp는 큰 건가 작은 건가?** 연환산하면 약 2.7%/년이다. 이건 작지 않다. 하지만 이건 "다른 시장의 팩터만으로" 설명한 것이다. **같은 시장의 증권을 전혀 안 썼는데** 55%를 설명한다는 것 자체가 놀라운 것이다.

#### GRS 검정이 불가능한 이유

> "A formal statistical test of the joint significance of the pricing errors is not possible since the independent variables change across test assets for each market and asset class (which is why this is not a formal asset pricing test)."

**GRS 검정**(Gibbons, Ross, and Shanken, 1989)은 "모든 포트폴리오의 알파가 동시에 0인가?"를 검정하는 것이다. 이 검정이 작동하려면 **모든 포트폴리오에 동일한 팩터(독립변수)를 써야** 한다.

그런데 수식 (4)에서는 시장마다 독립변수가 다르다:
- 미국 포트폴리오의 독립변수: 영국+유럽+일본+... 의 가치/모멘텀
- 영국 포트폴리오의 독립변수: 미국+유럽+일본+... 의 가치/모멘텀

"나를 제외한 나머지"가 시장마다 다르니까, 표준 GRS를 적용할 수 없다. 이것이 subsection B에서 "글로벌 3팩터 모형"을 따로 만드는 이유다 -- 모든 포트폴리오에 **같은** 팩터를 적용하기 위해.

#### 본문의 핵심 주장

> "The results indicate that value and momentum returns in one market are strongly related to value and momentum returns in other markets and asset classes. Unlike many asset pricing tests conducted in a single market, here there is no overlap of securities between the test assets used as the dependent variable and the factors used as regressors. The dependent variable contains securities from a completely separate market or asset class from those used to construct the factors on the right-hand side of the regression."

### 뜯기

이 단락이 Figure 5의 결과를 해석하는 핵심이다.

1. **"strongly related"**: 한 시장의 가치/모멘텀이 다른 시장의 가치/모멘텀과 강하게 관련된다. 이건 Section II의 상관 분석을 넘어서, 회귀 분석으로 확인한 것이다.

2. **"no overlap of securities"**: 이것이 이 검정의 최대 강점이다. Fama-French 3팩터 모형을 미국 주식에 적용할 때, HML 팩터도 미국 주식으로 만들고 테스트 자산도 미국 주식이다. 같은 주식이 양쪽에 들어간다. 여기서는 그런 문제가 **전혀 없다**.

3. **"completely separate market or asset class"**: 미국 주식 포트폴리오를 설명하는 팩터는 통화, 채권, 원자재 등 **완전히 다른 자산군**에서 왔다. 그런데도 설명력이 있다 → 진짜 공통 팩터가 존재한다.

> "Hence, the evidence in Figure 5 makes a compelling case for common global factor structure in value and momentum returns and suggests that this common variation is economically meaningful since it captures a significant fraction of the cross section of average returns."

**번역**: Figure 5의 증거는 가치/모멘텀 수익률에 공통 글로벌 팩터 구조가 있다는 강력한 증거이며, 평균수익률 횡단면의 상당 부분을 포착하므로 경제적으로도 의미 있다.

---

## B. 글로벌 3팩터 모형 (p.966~969)

> "To conduct a more formal asset pricing test, and to compare across various asset pricing models, we construct a three-factor model similar to equation (4), but where the regressors are the same for every asset. This three-factor model is similar in spirit to those of Fama and French (1993) and Carhart (1997), but applied globally to all markets and asset classes we study."

### 뜯기

수식 (4)의 한계: 시장마다 독립변수가 달라서 GRS 검정 불가.

해결책: **모든 포트폴리오에 동일한 팩터를 적용**하는 모형을 만든다. 이것이 "글로벌 3팩터 모형"이다.

- **Fama and French (1993)**: 미국 주식의 3팩터 (RMRF + SMB + HML). 시장 + 규모 + 가치.
- **Carhart (1997)**: FF 3팩터에 모멘텀(UMD)을 추가한 4팩터.
- **이 논문의 AMP 3팩터**: 글로벌 시장 + 글로벌 가치 everywhere + 글로벌 모멘텀 everywhere.

핵심 차이: FF/Carhart는 **미국 주식만**, AMP는 **전 세계 전 자산군**.

---

### 수식 (5): 글로벌 3팩터 모형

#### 말로 먼저

> "각 포트폴리오의 초과수익률을 **글로벌 시장** + **전 자산군 통합 가치 팩터** + **전 자산군 통합 모멘텀 팩터**, 이 세 개로 설명한다. 모든 48개 포트폴리오에 똑같은 세 팩터를 적용한다."

#### KaTeX 수식

$$R_{i,t}^{p} - r_{f,t} = \alpha_i^{p} + \beta_i^{p} \, MKT_t + v_i^{p} \, VAL_t^{\text{everywhere}} + m_i^{p} \, MOM_t^{\text{everywhere}} + \varepsilon_{i,t}^{p} \tag{5}$$

#### 기호 해설

| 기호 | 의미 | 수식 (4)와의 차이 |
|------|------|---------------|
| $VAL_t^{\text{everywhere}}$ | **전 자산군 동일 변동성 가중 가치 팩터** | (4)에서는 $\sum_{j \neq i} w_j VAL_{j,t}$ — 시장마다 달랐음. (5)에서는 **모든 시장 포함**, 모든 포트폴리오에 동일 |
| $MOM_t^{\text{everywhere}}$ | **전 자산군 동일 변동성 가중 모멘텀 팩터** | 마찬가지로 모든 시장 포함, 모든 포트폴리오에 동일 |

#### 수식 (4)와 (5)의 핵심 차이

| | 수식 (4) | 수식 (5) |
|---|---------|---------|
| 팩터가 시장마다 다른가? | **예** ($j \neq i$) | **아니오** (everywhere) |
| 테스트 자산과 팩터에 증권 겹침? | **없음** | **있음** (자기 시장도 팩터에 포함) |
| GRS 검정 가능? | **불가** | **가능** |
| 공식 자산가격결정 검정? | 아님 (공변동 검정) | **맞음** |

수식 (5)에서는 미국 주식 포트폴리오를 설명할 때 VAL_everywhere에 미국 가치 팩터도 포함된다. 증권 겹침이 있다. 하지만 이건 Fama-French 모형도 마찬가지다 -- HML은 미국 주식으로 만들고 테스트 자산도 미국 주식이다. 공식 자산가격결정 검정에서는 이것이 허용된다. 대신 GRS 검정으로 알파의 유의성을 엄밀하게 검정한다.

> "equation (5) also allows for a formal joint test of the significance of the alphas, since the explanatory variables are the same for each test asset. Hence, we report the Gibbons, Ross, and Shanken (GRS, 1989) F-statistic and p-value for a joint test of the pricing errors."

---

### Figure 6, Panel A: 48개 글로벌 가치/모멘텀 포트폴리오 (p.967)

> "The first graph in Panel A of Figure 6 plots the actual sample average returns of the 48 test assets versus their predicted expected returns from equation (5) along with a 45° line through the origin to highlight the magnitude of the pricing errors. The cross-sectional R² is 0.71 and the average absolute value of the alpha is 18 basis points, indicating slightly better fit than equation (4), which is not surprising, since, unlike equation (4), equation (5) contains some of the same securities on the left- and right-hand side of the regression."

#### 뜯기

Panel A에는 **4개의 산점도**가 있다. 각각 다른 자산가격결정 모형을 적용한 결과다. 48개 포트폴리오(8시장 × 3가치 + 8시장 × 3모멘텀)가 점으로 찍혀 있다.

#### 4개 모형 비교표

| # | 모형 | avg $\|\alpha\|$ | GRS F | p-value | $R^2$ | 평가 |
|---|------|-----------------|-------|---------|-------|------|
| 1 | **AMP 3-Factor** (MKT + VAL_everywhere + MOM_everywhere) | **0.00182 (18bp)** | **2.66** | 0 | **0.707** | **최고** |
| 2 | CAPM (MKT만) | 0.00399 (39bp) | 6.586 | 0 | 0.449 | 최하 |
| 3 | Fama-French 4-Factor (RMRF+SMB+HML+UMD) | 0.00352 (35bp) | 6.702 | 0 | 0.554 | 중하 |
| 4 | Fama-French 6-Factor (+DEF+TERM) | 0.00349 (35bp) | 7.113 | 0 | 0.601 | 중 |

#### 각 모형이 뭔가?

**1. AMP 3-Factor** -- 이 논문이 제안하는 모형:
- MKT: MSCI World Index (글로벌 시장)
- VAL_everywhere: 8개 자산군의 동일 변동성 가중 가치 팩터
- MOM_everywhere: 8개 자산군의 동일 변동성 가중 모멘텀 팩터

**2. CAPM** -- 가장 기본적인 모형:
- MKT만. "시장이 오르면 다 오른다"는 모형. 글로벌 포트폴리오 설명에 완전히 부적합.

**3. Fama-French 4-Factor**:

> "a four-factor model inspired by Carhart (1997), which is the Fama-French three-factor model consisting of the U.S. stock market RMRF, the U.S. size factor SMB, and the U.S. value factor HML augmented with the U.S. stock momentum factor UMD"

- RMRF: 미국 주식시장 초과수익률 (시장 팩터)
- SMB: Small Minus Big (소형주 - 대형주, 규모 팩터)
- HML: High Minus Low (가치주 - 성장주, 가치 팩터)
- UMD: Up Minus Down (승자 - 패자, 모멘텀 팩터)

핵심: **전부 미국 주식**으로 만든 팩터다. 이걸로 일본 주식, 통화, 원자재를 설명하려는 것이다. 당연히 한계가 있다.

**4. Fama-French 6-Factor**:

> "a six-factor model that adds the Fama and French (1993) bond return factors DEF and TERM"

4-Factor에 두 개 추가:
- DEF: Default spread (회사채 수익률 - 국채 수익률). 부도 위험 프리미엄.
- TERM: Term spread (장기 국채 - 단기 국채). 만기 프리미엄.

채권 팩터를 추가해서 비주식 자산도 설명하려는 시도. 하지만 여전히 미국 팩터.

#### 결과 해석

**AMP 3팩터가 압도적으로 우수하다.**

- **알파 크기**: AMP 18bp vs CAPM 39bp vs FF4 35bp vs FF6 35bp. AMP가 절반 이하.
- **$R^2$**: AMP 0.71 vs CAPM 0.45 vs FF4 0.55 vs FF6 0.60. AMP가 가장 높다.
- **GRS F-stat**: AMP 2.66 vs 나머지 6.5~7.1. 작을수록 좋다(알파가 0에 가까우면 F가 작다). AMP가 유일하게 3 이하.

그런데 **모든 모형의 p-value가 0**이다. 이건 뭘 의미하는가? GRS 검정의 귀무가설은 "모든 알파가 동시에 0이다". p=0이면 귀무가설 기각 → **어떤 모형도 완벽하지 않다**. AMP도 마찬가지. 하지만 AMP가 "가장 덜 나쁘다".

> "The Fama-French four- and six-factor specifications explain the returns a little better than the CAPM, but not nearly as well as the global three-factor model. The Fama-French factors generate twice the absolute magnitude of pricing errors as the three-factor global model and have much lower R²s."

**번역**: FF 4/6팩터는 CAPM보다 약간 낫지만, 글로벌 3팩터에는 한참 못 미친다. FF 팩터의 가격결정 오류는 글로벌 3팩터의 **2배**, $R^2$는 훨씬 낮다.

**왜 미국 팩터가 글로벌 포트폴리오를 설명 못 하는가?** 미국 주식의 HML은 "미국에서 싼 주식 사고 비싼 주식 파는 전략"이다. 이것이 일본 엔화의 가치/모멘텀과 무슨 관계가 있겠는가? 미국 주식 내부의 규모/가치 효과가 통화나 채권의 가치/모멘텀 효과와 동일한 경제적 원인을 가질 이유가 없다. 하지만 VAL_everywhere는 **전 자산군의 가치 효과를 통합**한 것이므로, 글로벌 공통 요인을 직접 포착한다.

---

### Figure 6, Panel B: Fama-French 25 Size-Value + 25 Size-Momentum (미국 주식) (p.968)

> "Panel B of Figure 6 repeats the same plots for test assets derived only from U.S. stocks. Here, we use the Fama-French 25 size-value and 25 size-momentum portfolios from Ken French's website... as test assets. These are, respectively, 5×5 double-sorted portfolios of U.S. stocks based on size and BE/ME and 5×5 portfolios sorted on size and past 2- to 12-month returns."

#### 뜯기

Panel B는 "반대 방향"의 검정이다.

- Panel A: **글로벌 포트폴리오**에 미국 팩터 vs 글로벌 팩터 → 글로벌 팩터 승
- Panel B: **미국 포트폴리오**에 미국 팩터 vs 글로벌 팩터 → 누가 이기는가?

테스트 자산: 50개 포트폴리오 (25 size-value + 25 size-momentum). Fama-French가 자신의 웹사이트에서 제공하는 표준 벤치마크다. 미국 주식만으로 구성.

#### 4개 모형 비교표 (Panel B)

| # | 모형 | avg $\|\alpha\|$ | GRS F | p-value | $R^2$ | 평가 |
|---|------|-----------------|-------|---------|-------|------|
| 1 | **AMP 3-Factor** | **0.00181 (18bp)** | **3.298** | 0 | **0.642** | 선전 |
| 2 | CAPM | 0.00319 (32bp) | 4.245 | 0 | 0.316 | 최하 |
| 3 | FF 4-Factor (RMRF+SMB+HML+UMD) | **0.00113 (11bp)** | **3.28** | 0 | **0.772** | **최고** |
| 4 | FF 6-Factor (+DEF+TERM) | 0.00113 (11bp) | 3.35 | 0 | 0.786 | 최고 |

**FF 3-Factor** (RMRF+SMB+HML만, UMD 없음)도 별도로 보고된다:
- GRS = 3.81, $R^2$ = 0.30 (Figure 6 Panel B 좌하단 그래프)

#### 결과 해석

미국 포트폴리오에서는 **FF 4/6팩터가 승리**한다. 놀랍지 않다:
- FF 팩터는 **미국 주식으로 만든** 팩터이고, 테스트 자산도 **미국 주식**이다
- 특히 SMB(규모 팩터)가 포함되어 있고, 테스트 자산이 규모로 정렬되어 있다

하지만 **AMP도 놀라울 정도로 선전**한다:
- AMP의 알파 18bp vs FF4의 11bp -- 차이가 7bp(월 0.07%)밖에 안 된다
- AMP의 $R^2$ 0.64 vs FF4의 0.77 -- 글로벌 팩터가 미국 주식의 64%를 설명

이건 대단한 결과다. AMP의 팩터에는 통화, 채권, 원자재의 가치/모멘텀이 섞여 있다. 그런 "잡다한" 팩터가 미국 주식의 규모/가치/모멘텀 포트폴리오를 64%나 설명한다? 이건 글로벌 공통 팩터의 힘이다.

---

### 사이즈 팩터 부재 논의 (p.969)

> "In addition, our three-factor model does not contain a size factor, which is important for pricing the Fama-French U.S. stock portfolios. If we exclude the two smallest quintiles of stocks from the Fama-French portfolios, then our three-factor model does as well as the Fama-French model in pricing the remaining Fama-French U.S. portfolios."

### 뜯기

AMP 3팩터에는 **규모(size) 팩터가 없다**. MKT + VAL + MOM, 세 개뿐.

FF 포트폴리오는 규모로 5분위 정렬이다. 가장 작은 주식(1분위, 2분위)은 "소형주 프리미엄"이 강하게 작용한다. AMP에 규모 팩터가 없으니 이 부분을 설명 못 한다.

**하지만**: 가장 작은 2개 분위를 빼면 AMP가 FF와 동등해진다. 이건 두 가지를 뜻한다:
1. AMP의 열세는 **오직 소형주** 때문이다
2. 중대형주의 가치/모멘텀은 글로벌 팩터로 충분히 설명된다

왜 AMP에 규모 팩터를 안 넣었는가? 규모 효과는 주로 주식에서 나타난다. 통화, 채권, 원자재에는 "규모"라는 개념이 적용되기 어렵다. 8개 자산군에 걸쳐 일관되게 적용할 수 있는 팩터만 넣은 것이다.

---

### Section B 종합 결론 (p.969)

> "Taken together, Panel A of Figure 6 shows that our global three-factor model can explain the returns to value and momentum across markets and asset classes much better than local U.S. factors can and Panel B shows that our global factors can explain the local returns to value and momentum in U.S. stocks almost as well as the U.S. factors can."

### 뜯기

이 한 문장이 Section B의 결론이다. 두 방향의 비대칭:

| 방향 | 글로벌 팩터 | 미국 팩터 | 승자 |
|------|---------|--------|-----|
| 글로벌 포트폴리오 설명 | 잘함 (18bp, R²=0.71) | 못함 (35bp, R²=0.55) | **글로벌** |
| 미국 포트폴리오 설명 | 꽤 잘함 (18bp, R²=0.64) | 잘함 (11bp, R²=0.77) | 미국 (근소) |

글로벌 팩터는 양방향 모두 잘 작동하지만, 미국 팩터는 미국에서만 잘 작동한다. 이건 글로벌 팩터가 더 "범용적"이라는 뜻이다.

> "These results suggest that global value and momentum portfolios across markets and asset classes are closer to the efficient frontier than U.S. stock-only value and momentum portfolios, and therefore provide a more robust set of asset pricing factors that can be used more broadly."

**효율적 프론티어(efficient frontier)**에 더 가깝다 = 같은 위험에서 더 높은 수익을 준다 = 더 나은 팩터다. 글로벌 팩터가 미국 팩터보다 효율적 프론티어에 가깝다.

---

## C. 추가 가격결정 검정과 경제적 크기 (p.969~975)

> "To further investigate the economic importance of the commonality among value and momentum strategies across asset markets, we examine their relation to macroeconomic and liquidity risks through cross-sectional and time-series asset pricing tests."

### 뜯기

Section A-B에서는 "가치/모멘텀 팩터로 가치/모멘텀 포트폴리오를 설명"했다. 일종의 순환이다.

Section C에서는 **경제적 변수**(유동성, GDP, 소비 등)가 가치/모멘텀 프리미엄을 얼마나 설명하는지 본다. "왜 이 프리미엄이 존재하는가?"에 대한 답을 찾는 것이다.

두 가지 방법:
1. **횡단면 검정** (C.1): Fama-MacBeth 회귀 -- "유동성 베타가 높은 포트폴리오가 수익도 높은가?"
2. **시계열 검정** (C.2): 팩터 모방 포트폴리오(FMP)를 독립변수로 쓰는 시계열 회귀

---

### C.1. 횡단면 가격결정 검정: Fama-MacBeth (p.969~971)

> "Table V reports Fama-MacBeth cross-sectional regressions of returns of the 48 value and momentum test portfolios on their betas with respect to funding liquidity risk, GDP growth, long-run consumption growth, TERM, and DEF. Regressions are run in the style of Fama and MacBeth (1973), where the cross section of monthly returns are regressed on the betas (estimated univariately using rolling windows of the past 60 months of returns) each month, and the time-series mean and t-statistic of the cross-sectional regression coefficients are reported in Table V."

#### Fama-MacBeth 회귀란?

**2단계 회귀** 방법이다:

**1단계 (시계열 회귀)**: 각 포트폴리오의 수익률을 여러 리스크 팩터에 회귀해서 **베타(민감도)**를 추정한다.
- 예: "포트폴리오 A의 유동성 베타 = 1.5" → "유동성이 1% 나빠지면 이 포트폴리오 수익이 1.5% 떨어진다"
- 롤링 윈도우 60개월(5년) 사용

**2단계 (횡단면 회귀)**: 매달, 48개 포트폴리오의 **그 달 수익률**을 **1단계에서 추정한 베타들**에 회귀한다.
- $R_i = \gamma_0 + \gamma_1 \hat\beta_{i,\text{Liq}} + \gamma_2 \hat\beta_{i,\text{GDP}} + \cdots + \eta_i$
- 이걸 매달 반복하면 $\gamma_1$이 매달 하나씩 나온다
- $\gamma_1$의 시계열 평균과 t-통계량을 보고

**$\gamma_1$의 의미**: "유동성 리스크에 1단위 더 노출되면 월 수익률이 $\gamma_1$만큼 높다/낮다". 이것이 **유동성 리스크 프리미엄**이다.

#### Dimson correction

> 본문에서 시장 베타에는 **Dimson correction**을 적용한다고 언급한다.

비동시 거래(nonsynchronous trading) 문제를 해결하기 위한 것이다. 시장이 다른 시간대에 거래되면(미국 장 마감 시각 ≠ 일본 장 마감 시각), 단순 동시점 회귀로는 베타가 과소추정된다.

Dimson(1979) 방법: 시장 수익률의 **동시점 + 1개월 래그 + 2개월 래그**를 모두 독립변수에 넣고, 세 계수의 합을 베타로 쓴다.

#### FMP(Factor Mimicking Portfolio)란?

> "the time series of the coefficient estimates represents the return series to a minimum variance portfolio with a unit exposure to that factor... Hence, the time series of monthly coefficient estimates represents a factor mimicking portfolio for liquidity risk, which we call FP_liq risk."

Fama-MacBeth 2단계의 **계수 시계열**은 그 자체가 투자 전략의 수익률이다. 유동성 베타의 계수 $\gamma_{1,t}$를 모으면, "유동성 리스크에 단위 노출을 가진 최소분산 포트폴리오"의 수익률 시계열이 된다. 이것을 **팩터 모방 포트폴리오(Factor Mimicking Portfolio, FMP)**라고 부른다. $FP_{\text{liq risk}}$라고 표기.

이 FMP는 Section C.2의 시계열 검정에서 독립변수로 쓰인다.

---

### Table V: Fama-MacBeth 횡단면 회귀 결과 (p.970)

48개 가치/모멘텀 포트폴리오의 횡단면 수익률을 각종 베타에 회귀한 결과. **10개 행**, 각 행은 서로 다른 변수 조합이다.

#### 전체 결과표

| 행 | $\beta_{\text{Liq}}$ | $\beta_{\text{GDP}}$ | $\beta_{\text{LRC}}$ | $\beta_{\text{TERM}}$ | $\beta_{\text{DEF}}$ | $\beta_{\text{MKT}}$ | $\beta_{\text{Value}}$ | $\beta_{\text{Mom}}$ |
|---|---|---|---|---|---|---|---|---|
| 1 | **0.0024** (**3.05**) | | | | | | | |
| 2 | | 0.0003 (0.43) | 0.0005 (0.42) | **0.0021** (**2.19**) | **0.0023** (**2.18**) | | | |
| 3 | **0.0023** (**2.29**) | -0.0001 (-0.13) | 0.0012 (1.01) | 0.0014 (1.59) | 0.0001 (0.11) | | | |
| 4 | 0.0005 (0.56) | | | 0.0015 (1.75) | **0.0020** (**2.22**) | | **0.0029** (**2.58**) | |
| 5 | 0.0016 (1.38) | **0.0018** (**2.87**) | -0.0001 (-0.03) | **0.0033** (**2.87**) | 0.0014 (1.12) | -0.0006 (-0.38) | **0.0031** (**3.96**) | **0.0030** (**3.53**) |
| | **Funding liquidity만** | | | | | | | |
| 6 | **0.0022** (**2.06**) | -0.0002 (-0.30) | 0.0019 (1.45) | 0.0011 (1.05) | 0.0015 (1.30) | | | |
| 7 | 0.0012 (1.80) | **0.0019** (**3.28**) | 0.0003 (0.17) | **0.0027** (**2.19**) | 0.0011 (0.84) | 0.0008 (0.58) | **0.0034** (**4.40**) | **0.0031** (**3.50**) |
| | **Market liquidity만** | | | | | | | |
| 8 | 0.0001 (0.07) | 0.0003 (0.48) | 0.0005 (0.44) | **0.0021** (**2.67**) | **0.0022** (**2.63**) | | | |
| 9 | -0.0013 (-0.88) | **0.0019** (**3.19**) | -0.0010 (-0.77) | **0.0045** (**5.05**) | **0.0030** (**2.73**) | 0.0004 (0.31) | **0.0038** (**5.94**) | **0.0040** (**5.82**) |

*괄호 안 = t-통계량. 굵은 글씨 = |t| > 2 (약 5% 유의수준에서 유의)*

#### 변수 설명

| 변수 | 의미 |
|------|------|
| $\beta_{\text{Liq}}$ (행1-5) | "All" 유동성 리스크 베타 -- funding + market의 주성분 가중 평균 |
| $\beta_{\text{GDP}}$ | GDP 성장률에 대한 민감도 |
| $\beta_{\text{LRC}}$ | 장기 소비 성장률(Long-Run Consumption growth)에 대한 민감도 |
| $\beta_{\text{TERM}}$ | 만기 스프레드(장기 국채 - 단기 국채)에 대한 민감도 |
| $\beta_{\text{DEF}}$ | 디폴트 스프레드(회사채 - 국채)에 대한 민감도 |
| $\beta_{\text{MKT}}$ | 글로벌 시장(MSCI World)에 대한 민감도 |
| $\beta_{\text{Value}}$ | VAL_everywhere에 대한 민감도 |
| $\beta_{\text{Mom}}$ | MOM_everywhere에 대한 민감도 |
| $\beta_{\text{FundLiq}}$ (행6-7) | Funding 유동성만 사용한 베타 |
| $\beta_{\text{MktLiq}}$ (행8-9) | Market 유동성만 사용한 베타 |

---

#### 행별 해석

**행 1: 유동성만**

> "As the first row of Table V shows, liquidity risk betas capture part of the cross-sectional variation in average returns across the 48 portfolios, as indicated by the positive and significant coefficient on the liquidity beta. That coefficient also represents the risk premium for liquidity risk among the 48 test assets, which is 24 basis points per month or about 3% per year."

- 유동성 베타 계수 = **0.0024**, t = **3.05** → 강하게 유의
- **경제적 크기**: 0.0024/월 × 12 = **약 3%/년**
  - "유동성 리스크에 1단위 더 노출되면 연 3% 더 번다"
  - 이건 상당한 프리미엄이다

**행 2: 거시변수만 (유동성 제외)**

> "The second row of Table V shows that neither GDP growth nor long-run consumption growth captures much cross-sectional variation in returns, but TERM and DEF do, exhibiting a risk premium of 21 and 23 basis points, respectively."

- GDP (0.43), LRC (0.42) → 미유의. 경기 사이클과 소비 성장은 가치/모멘텀의 횡단면을 설명 못 함
- TERM (2.19), DEF (2.18) → 유의. 만기 프리미엄과 디폴트 프리미엄은 설명력 있음

**행 3: 유동성 + 거시변수 동시 투입**

> "the third row of Table V adds liquidity betas to the regression, where we find that the significance of TERM and DEF are subsumed by liquidity risk."

- 유동성 0.0023 (2.29) → 여전히 유의
- TERM 0.0014 (1.59), DEF 0.0001 (0.11) → **유의성 소멸**

**해석**: TERM과 DEF가 설명하던 것을 유동성이 **흡수(subsume)**했다. 만기 프리미엄과 디폴트 프리미엄이 사실은 유동성 리스크의 다른 얼굴이었다는 것이다. 유동성이 나빠지면 장기 채권과 회사채의 스프레드가 벌어지는 것은 자연스러운 현상이니까.

**행 4: 유동성 + TERM/DEF + 가치 팩터**

- 유동성 0.0005 (0.56) → **유의성 소멸!**
- 가치 팩터 0.0029 (2.58) → 유의

**행 5: 전체 모형 (모든 변수)**

> "Finally, we add betas with respect to the global three-factor model -- the MSCI World Index, and the value and momentum everywhere factors. It is perhaps not too surprising that betas with respect to value and momentum factors capture average returns to value and momentum portfolios and that they subsume a significant portion of the explanatory power of other factors such as liquidity risk."

- 유동성 0.0016 (1.38) → 미유의
- GDP **0.0018** (**2.87**) → 유의! (다른 변수 통제 후 유의해짐)
- TERM **0.0033** (**2.87**) → 유의
- 가치 **0.0031** (**3.96**), 모멘텀 **0.0030** (**3.53**) → 강하게 유의

**핵심 패턴**: 유동성 → 가치/모멘텀을 추가하면 유동성의 유의성이 사라진다. 이건 **가치/모멘텀 팩터가 유동성 리스크를 포섭**한다는 뜻이다. 가치/모멘텀 프리미엄의 일부가 유동성 리스크에 대한 보상이지만, 가치/모멘텀 팩터가 그 이상의 것을 포착하고 있다.

**행 6-7: Funding 유동성만**

- 행 6: funding 유동성 0.0022 (2.06) → **유의**
- 행 7: 전체 모형에서도 0.0012 (1.80) → 경계선

**행 8-9: Market 유동성만**

- 행 8: market 유동성 0.0001 (0.07) → **완전 미유의**
- 행 9: 전체 모형에서 -0.0013 (-0.88) → 미유의

> "only funding liquidity appears to be priced in the cross section of our global assets, and exposure to value and momentum common factors seems to capture part of funding liquidity risk exposure."

**결론**: **펀딩 유동성만 유의하고, 시장 유동성은 유의하지 않다.** Section III에서 발견한 것과 일치한다 -- 가치/모멘텀의 공변동은 주로 펀딩 유동성(돈을 빌릴 수 있는 능력)과 관련 있지, 시장 유동성(매매 용이성)과는 관련이 약하다.

---

### C.2. 시계열 가격결정 검정 (p.971~975)

> "To gain more insight into the economic magnitudes that liquidity risk and the other factors explain, we use the factor mimicking portfolios created from the Fama-MacBeth regressions to conduct time-series asset pricing tests. Specifically, we regress each of the 48 portfolios' time series of monthly returns on the factor mimicking portfolio returns for liquidity risk, GDP growth, and long-run consumption growth, as well as TERM, DEF, and the value and momentum everywhere factors."

#### 뜯기

C.1(횡단면)에서 C.2(시계열)로 넘어간다. 왜 둘 다 하는가?

- **횡단면 검정**: "어떤 리스크가 **가격결정**되는가?" (유의한 프리미엄이 있는가?)
- **시계열 검정**: "모형이 각 포트폴리오의 **시간에 따른 변동**을 얼마나 설명하는가?"

시계열 검정에서는 FMP를 독립변수로 쓴다. FMP는 Fama-MacBeth의 계수 시계열 -- 즉 실제 투자 가능한 포트폴리오의 수익률이다. 종속변수와 독립변수 모두 **수익률**이므로 공식적인 자산가격결정 검정이 가능하다.

#### 보고 통계량

| 통계량 | 의미 | 좋은 모형의 조건 |
|--------|------|-------------|
| GRS F-stat | "모든 알파가 동시에 0인가?" 검정 | 작을수록 좋음 |
| p-value | GRS의 유의확률 | 클수록 좋음 (0.05 이상이면 기각 못 함) |
| avg $\|\alpha\|$ | 평균 절대 알파 | 작을수록 좋음 |
| avg TS $R^2$ | 시계열 평균 결정계수 | 클수록 좋음 |
| xs $R^2$ | 횡단면 결정계수 | 클수록 좋음 |
| Eig% | Moskowitz (2003) 고유값 비율 | 클수록 좋음 |

**Eig%란?** 모형이 함축하는 공분산 행렬의 고유값 합 / 표본 공분산 행렬의 고유값 합. 직관적으로: "테스트 자산들 사이의 공변동 중 몇 %를 이 모형이 포착하는가?"

---

### Table VI: 시계열 가격결정 검정 (p.972~973)

3개 패널로 구성. 각 패널마다 글로벌 팩터 모형들과 미국 팩터 모형들을 비교한다.

---

#### Panel A: 48개 글로벌 가치/모멘텀 포트폴리오

| # | 모형 | GRS F | p-value | avg $\|\alpha\|$ | avg TS $R^2$ | xs $R^2$ | Eig% |
|---|------|-------|---------|-----------------|-------------|---------|------|
| | **글로벌 팩터** | | | | | | |
| 1 | CAPM (글로벌) | 6.02 | 0.000 | 0.0035 (35bp) | 0.40 | 0.52 | 57% |
| 2 | + $FP_{\text{liq}}$ | 5.02 | 0.000 | 0.0031 (31bp) | 0.48 | 0.54 | 64% |
| 3 | + $FP_{\text{GDP}}$ + $FP_{\text{LRC}}$ + TERM + DEF | 4.09 | 0.000 | 0.0027 (27bp) | 0.59 | 0.56 | 80% |
| 4 | **+ VAL + MOM (3팩터)** | **2.66** | **0.000** | **0.0018 (18bp)** | **0.68** | **0.72** | **84%** |
| 5 | VAL만 (MKT + VAL) | 3.72 | 0.000 | 0.0028 (28bp) | 0.59 | 0.43 | 68% |
| 6 | MOM만 (MKT + MOM) | 3.80 | 0.000 | 0.0022 (22bp) | 0.42 | 0.57 | 70% |
| | **미국 팩터** | | | | | | |
| 7 | CAPM (미국) | 6.59 | 0.000 | 0.0039 (39bp) | 0.30 | 0.44 | 47% |
| 8 | FF 3-Factor | 7.18 | 0.000 | 0.0036 (36bp) | 0.31 | 0.50 | 53% |
| 9 | FF 4-Factor | 6.70 | 0.000 | 0.0035 (35bp) | 0.31 | 0.55 | 63% |
| 10 | FF 6-Factor | 7.11 | 0.000 | 0.0035 (35bp) | 0.39 | 0.62 | 64% |

#### 행별 해석

> "As the first row of Panel A of Table VI shows, the market portfolio alone (global CAPM) generates substantial pricing errors -- an average absolute alpha of 35 basis points per month that is easily rejected by the GRS test -- and leaves a lot of time-series and cross-sectional variation unexplained. The market portfolio captures about 57% of the covariation among the returns."

**행 1 (글로벌 CAPM)**: GRS=6.02, 알파 35bp, $R^2$=0.40. 시장 팩터만으로는 전혀 부족하다. 가치/모멘텀 프리미엄이 시장 리스크에 대한 보상이 아니라는 증거.

> "The second row adds the liquidity risk factor mimicking portfolio as a regressor, and although the GRS test is still rejected, the average absolute alpha declines to 31 basis points, the cross-sectional R² increases, and the amount of covariation captured increases."

**행 2 (+유동성)**: GRS 6.02→5.02, 알파 35→31bp, Eig% 57→64%. 유동성을 추가하면 약간 개선된다. 하지만 여전히 크게 부족하다.

> "Hence, liquidity risk adds some additional explanatory power for both pricing and common variation of value and momentum portfolios globally across asset classes."

**행 3 (+거시+유동성)**: GRS 4.09, 알파 27bp, TS $R^2$ 0.59, Eig% 80%. 거시변수(GDP, 소비, TERM, DEF)를 추가하면 공변동 설명이 크게 개선(64→80%). 하지만 가격결정 오류는 여전히 상당.

**행 4 (3팩터 = 최적)**: GRS **2.66**, 알파 **18bp**, xs $R^2$ **0.72**, Eig% **84%**. 모든 지표에서 최고.

> "The fourth row uses our three-factor model, which provides the best fit. Here, the average absolute alpha is only 18 basis points, the cross-sectional R² is 72%, and 84% of the covariation among the test assets is captured by these factors."

**행 5-6 (VAL만, MOM만)**:

> "The next two rows further show that having both value and momentum in the model is important, since having only value or momentum by itself increases pricing errors and decreases the fit considerably. This further underscores the difficulty of using a single factor to explain both value and momentum."

- VAL만: GRS 3.72, 알파 28bp, xs $R^2$ 0.43
- MOM만: GRS 3.80, 알파 22bp, xs $R^2$ 0.57

둘 다 넣은 것(행 4)에 비해 **현저히 나쁘다**. 왜? 가치와 모멘텀은 **음의 상관**이다. 한 팩터로는 "양의 수익 + 음의 상관"이라는 두 현상을 동시에 설명할 수 없다.

#### 유동성의 한계 (p.974)

> "While there is a link between value and momentum and liquidity risk, only a small fraction of the return premia and covariation is captured by our proxies for these risks. We view these findings as an important starting point for possible theories related to value and momentum phenomena, but emphasize that we are far from a full explanation of these effects."

> "We also recognize that measurement error in liquidity risk may limit what we can explain. In addition, a single liquidity risk factor alone cannot explain value and momentum since they are negatively correlated with each other but both produce positive returns, unless there is substantial time variation in liquidity risk betas and in the liquidity risk premium."

### 뜯기

이 단락은 저자들의 **솔직한 인정**이다. 유동성으로 설명할 수 있는 것은 **일부분**뿐이다.

왜 단일 유동성 팩터로 가치와 모멘텀을 동시에 설명할 수 없는가?

논리 구조:
1. 가치: 유동성 리스크에 **음의 베타** (유동성 악화 시 가치주가 상대적으로 덜 떨어짐)
2. 모멘텀: 유동성 리스크에 **양의 베타** (유동성 악화 시 모멘텀 전략이 큰 손실)
3. 둘 다 **양의 수익**을 낸다

만약 유동성 리스크 프리미엄이 양수(+)라면:
- 양의 베타를 가진 모멘텀 → 양의 기대수익 ✓
- 음의 베타를 가진 가치 → **음의 기대수익** ✗ (실제로는 양의 수익)

즉, 유동성이 모멘텀은 설명할 수 있지만 가치는 설명할 수 없다. **음의 베타인데 양의 수익**이라는 것은 유동성 이외에 다른 요인이 있다는 뜻이다.

유일한 예외: 유동성 리스크 베타와 프리미엄이 **시간에 따라 크게 변하는** 경우. 하지만 이건 검증하기 어렵다.

**행 7-10 (미국 팩터)**: 미국 CAPM, FF3, FF4, FF6 모두 글로벌 포트폴리오 설명에 부적합.

> "the U.S. factors do not do a great job of describing the global value and momentum portfolio returns, leaving larger pricing errors and lower R²s, and capturing a smaller fraction of their covariance matrix."

미국 CAPM GRS=6.59, FF6 GRS=7.11 -- 글로벌 3팩터의 2.66에 비해 훨씬 크다. 미국 팩터가 미국 밖의 세계를 설명하지 못한다.

---

#### Panel B: Fama-French 25+25 (미국 주식)

| # | 모형 | GRS F | p-value | avg $\|\alpha\|$ | avg TS $R^2$ | xs $R^2$ | Eig% |
|---|------|-------|---------|-----------------|-------------|---------|------|
| | **글로벌 팩터** | | | | | | |
| 1 | CAPM (글로벌) | 4.09 | 0.000 | 0.0030 (30bp) | 0.41 | 0.20 | 48% |
| 2 | + $FP_{\text{liq}}$ | 4.12 | 0.000 | 0.0030 (30bp) | 0.42 | 0.20 | 49% |
| 3 | + 거시 + 유동성 | 4.76 | 0.000 | 0.0035 (35bp) | 0.57 | 0.38 | 66% |
| 4 | **AMP 3-Factor** | **3.22** | **0.000** | **0.0019 (19bp)** | **0.70** | **0.68** | **82%** |
| | **미국 팩터** | | | | | | |
| 5 | CAPM (미국) | 4.25 | 0.000 | 0.0032 (32bp) | 0.73 | 0.17 | 93% |
| 6 | FF 3-Factor | 3.81 | 0.000 | 0.0023 (23bp) | 0.87 | 0.30 | 97% |
| 7 | FF 4-Factor | **3.28** | **0.000** | **0.0011 (11bp)** | **0.91** | **0.77** | **97%** |
| 8 | FF 6-Factor | 3.35 | 0.000 | 0.0011 (11bp) | 0.91 | 0.77 | 97% |

#### 해석

> "Panel B of Table VI repeats the same exercise as Panel A, but uses the 25 size-BE/ME and 25 size-momentum U.S. equity portfolios from Ken French's website as test assets. Not surprisingly, the Fama-French U.S. factors do a good job of capturing these returns, though the GRS test is still rejected. However, the global value and momentum everywhere factors, which consist primarily of non-U.S. equities and other asset classes, also do a good job explaining the 50 U.S. equity-based test assets -- the average absolute alpha is only 19 basis points, the cross-sectional R² is 68%, and the percentage of covariation captured is 66%."

미국 테스트 자산에서는 당연히 미국 팩터가 유리하다:
- FF 4-Factor: 알파 11bp, xs $R^2$ 0.77, Eig% 97% -- 거의 완벽
- AMP: 알파 19bp, xs $R^2$ 0.68, Eig% 82% -- 상당히 좋지만 열세

그런데 주목할 점:
- **미국 CAPM의 TS $R^2$는 0.73인데 xs $R^2$는 0.17**. 미국 시장이 개별 포트폴리오의 시간 변동은 잘 설명하지만(시장과 같이 움직이니까), 포트폴리오 **간의 수익률 차이**는 설명 못 한다.
- AMP는 TS $R^2$ 0.70, xs $R^2$ 0.68 -- 둘 다 균형 잡혀 있다. 글로벌 가치/모멘텀 팩터가 시간 변동과 횡단면 차이를 모두 포착한다.

> "This is better than the Fama-French three factor model does and only slightly worse than the Fama-French four- or six-factor models, which are specifically designed to capture these portfolios and are constructed from the same set of securities as the test assets themselves."

**번역**: AMP가 FF 3팩터보다 낫고, FF 4/6팩터보다 근소하게 뒤진다. FF 4/6팩터는 테스트 자산과 같은 증권으로 설계된 것인데도.

---

#### Panel C: 13개 헤지펀드 지수

> "Finally, Panel C of Table VI considers how well these factor models can explain hedge fund returns. Using the returns of 13 hedge fund indices from Dow Jones Credit Suisse (DJCS) and Hedge Fund Research Institute (HFRI)..."

**헤지펀드 지수 목록**:

| 출처 | 지수 |
|------|------|
| DJCS | Market Neutral, Long-Short, Multi Strategy, Macro, Managed Futures, Currency, Emerging Markets, Overall |
| HFRI | Equity Hedge, Fund of Funds, Macro, Emerging Markets, Overall |

총 **13개** 지수. 이건 **완전히 새로운 테스트 자산**이다 -- 가치/모멘텀 포트폴리오가 아니라 실제 헤지펀드의 수익률.

| # | 모형 | GRS F | p-value | avg $\|\alpha\|$ | avg TS $R^2$ | xs $R^2$ | Eig% |
|---|------|-------|---------|-----------------|-------------|---------|------|
| | **글로벌 팩터** | | | | | | |
| 1 | CAPM (글로벌) | 12.14 | 0.000 | 0.0032 (32bp) | 0.30 | 0.20 | 43% |
| 2 | + $FP_{\text{liq}}$ | 12.36 | 0.000 | 0.0025 (25bp) | 0.34 | 0.30 | 47% |
| 3 | + 거시 + 유동성 | 11.86 | 0.000 | 0.0022 (22bp) | 0.46 | 0.17 | 53% |
| 4 | **AMP 3-Factor** | **7.26** | **0.000** | **0.0018 (18bp)** | **0.41** | **0.47** | **54%** |
| | **미국 팩터** | | | | | | |
| 5 | CAPM (미국) | 12.14 | 0.000 | 0.0028 (28bp) | 0.30 | 0.18 | 43% |
| 6 | FF 3-Factor | 12.64 | 0.000 | 0.0026 (26bp) | 0.35 | 0.19 | 47% |
| 7 | FF 4-Factor | 13.03 | 0.000 | 0.0022 (22bp) | 0.37 | 0.36 | 49% |
| 8 | FF 6-Factor | 12.25 | 0.000 | 0.0021 (21bp) | 0.44 | 0.36 | 51% |

#### 해석

> "Panel C of Table VI shows that the global three-factor model has smaller pricing errors than the Fama-French model and its extensions with the momentum, TERM, and DEF factors."

AMP 3-Factor가 모든 미국 팩터 모형보다 우수하다:
- **GRS**: AMP 7.26 vs FF6 12.25 -- AMP가 훨씬 작다 (훨씬 좋다)
- **알파**: AMP 18bp vs FF6 21bp -- AMP가 더 작다
- **xs $R^2$**: AMP 0.47 vs FF6 0.36 -- AMP가 더 높다

왜 헤지펀드에서 AMP가 더 잘 작동하는가?

> "These results are consistent with Boyson, Stahel, and Stulz (2010), Sadka (2012), and Bali, Brown, and Caglayan (2011, 2012), who find that the Fama and French U.S. stock factors do not explain the cross section of hedge fund returns very well. However, our simple value and momentum factors applied globally across asset classes do appear to capture a sizeable fraction of the returns to hedge funds."

헤지펀드는 **글로벌하게** 투자한다. 주식만이 아니라 통화, 채권, 원자재, 선물 등 다양한 자산에 투자한다. 미국 주식 팩터(FF)로는 이런 글로벌 전략을 설명할 수 없다. 하지만 AMP의 글로벌 가치/모멘텀 팩터는 이런 전략의 핵심을 포착한다.

> "hedge funds are engaged in similar or highly correlated strategies globally"

많은 헤지펀드가 본질적으로 **가치와 모멘텀 전략**을 하고 있다는 것이다. 다른 이름으로, 다른 자산에서, 다른 방식으로 하고 있지만 결국 "싼 걸 사고 비싼 걸 파거나(가치)", "오르는 걸 사고 내리는 걸 파거나(모멘텀)"다.

하지만 **GRS가 여전히 7.26으로 기각**된다. 그리고 Eig%가 54%에 불과하다. 헤지펀드 수익의 절반 가까이는 가치/모멘텀 이외의 요인에서 온다. 이건 당연하다 -- 헤지펀드는 가치/모멘텀만 하는 게 아니라 옵션 전략, 이벤트 드리븐, 통계적 차익거래 등 다양한 전략을 쓴다.

---

### Section IV 종합 결론 (p.975)

> "The evidence in Table VI suggests that the global across-asset three-factor model does a good job of capturing not only the returns to value and momentum globally across asset classes, but also the returns to size and value and size and momentum in U.S. equities, as well as the cross section of hedge fund returns, providing additional testing grounds that are created from a completely different set of securities."

> "Conversely, while local U.S. factors capture U.S. equity returns well, they do not explain a lot of value and momentum returns globally or across asset classes, nor do they capture the returns to various hedge fund strategies well."

> "While our three-factor global model performs better in explaining all of these different test assets, the GRS test still rejects our model in all cases, suggesting that more work needs to be done to fully describe the cross section of returns."

### 뜯기

세 단락의 핵심을 정리하면:

**1. AMP 3팩터의 강점**:
- 글로벌 가치/모멘텀 ✓
- 미국 주식 규모/가치/모멘텀 ✓ (거의)
- 헤지펀드 ✓
- 완전히 다른 증권 집합에서도 작동 ✓

**2. 미국 팩터의 한계**:
- 미국 주식 ✓
- 글로벌 포트폴리오 ✗
- 헤지펀드 ✗

**3. 솔직한 인정**:
- **GRS가 모든 경우에서 기각된다** → 어떤 모형도 완벽하지 않다
- "more work needs to be done" → 아직 갈 길이 멀다

이 솔직함이 이 논문의 신뢰도를 높인다. "우리 모형이 최고다!"가 아니라 "기존보다 낫지만, 아직 부족하다"는 것이다.

---

## 이 섹션에서 배운 것

| # | 핵심 발견 | 근거 |
|---|---------|------|
| 1 | 한 시장의 가치/모멘텀은 **다른 시장의** 가치/모멘텀으로 55% 설명 가능 | Figure 5, 수식 (4) |
| 2 | 글로벌 3팩터(MKT+VAL+MOM)가 48개 포트폴리오를 가장 잘 설명 | Figure 6A, Table VI Panel A |
| 3 | 미국 팩터(FF)는 글로벌 포트폴리오 설명에 부적합 | Table VI Panel A 행7-10 |
| 4 | 글로벌 팩터가 미국 포트폴리오도 꽤 잘 설명 (FF와 근소 차이) | Figure 6B, Table VI Panel B |
| 5 | 펀딩 유동성만 횡단면에서 유의하게 가격결정됨 (시장 유동성은 미유의) | Table V 행6-9 |
| 6 | 가치/모멘텀 팩터가 유동성의 설명력을 포섭 | Table V 행3-5 |
| 7 | 유동성 단독으로는 가치+모멘텀을 동시에 설명 불가 (음의 상관 + 양의 수익 문제) | p.974 |
| 8 | 글로벌 3팩터가 헤지펀드 수익도 FF보다 잘 설명 | Table VI Panel C |
| 9 | 그러나 **모든 모형이 GRS에서 기각** -- 완벽한 모형은 아직 없다 | 전체 |

---

## 여기서 멈추고 생각하기

### 🤔 추론 연습
1. **글로벌 vs 로컬 모형의 최적 범위** 글로벌 3팩터가 FF 6팩터보다 낫다 — 하지만 미국 주식만 보면 FF가 더 낫다. 이건 "글로벌 모형이 로컬보다 항상 낫다"는 뜻이 아니라, "적용 범위에 따라 최적 모형이 다르다"는 뜻이다. 왜 그런가? 글로벌 팩터는 공통 변동을 잡지만, 로컬 특이성을 희생한다.
2. **VAL과 MOM은 합칠 수 없다** VAL만 or MOM만 넣으면 적합도가 급감한다 — 이건 "가치와 모멘텀이 별도의 위험 요인"이라는 강력한 증거다. 하나의 팩터로 합칠 수 없다. 이 결론이 50/50 조합 전략의 이론적 근거가 된다.
3. **헤지펀드 알파의 실체** 헤지펀드 수익률의 상당 부분이 가치/모멘텀으로 설명된다 — "헤지펀드의 알파는 사실 팩터 노출"이라는 비판의 근거다. 연 2%의 관리 수수료와 20%의 성과 보수를 내고 살 수 있는 것이 결국 팩터 베타라면?

### ⚡ 비판적 사고
1. **GRS 기각의 의미** GRS에서 모든 모형이 기각된다(p<0.001). "덜 기각"이 "좋은 모형"이라는 논리는 상대적 비교에 불과하다. 절대적으로는 모두 불완전하다. 누락된 팩터가 있다는 뜻인데, 그게 무엇일까?
2. **Fama-MacBeth 윈도우 의존성** 60개월 롤링 윈도우 — 윈도우 크기에 따라 결과가 달라질 수 있다. 36개월이나 120개월이면 리스크 프리미엄 추정치가 어떻게 변할까? 저자들은 이 민감도를 보고하지 않는다.

> **다음**: [dissect-07 Robustness and Conclusion 해체](dissect-07-robustness.md) -- 구현 실무 이슈 (거래비용, 소형주 제외 등)와 논문의 최종 결론
