# 논문 해체: Section I — 데이터와 포트폴리오 구성 (p.933~939)

> 이 섹션은 논문의 **주방**이다. 어떤 재료(데이터)를 어떻게 손질(방법론)해서 요리(포트폴리오)하는지를 보여준다. Introduction에서 "우리가 이걸 발견했다"고 선언했으니, 이제 "그 발견을 어떻게 했는가"를 설명하는 차례다.

---

## 섹션 도입문

> "We describe our data and methodology for constructing value and momentum portfolios across markets and asset classes."

### 뜯기

이 한 문장이 Section I 전체를 요약한다.

- **"our data"** = 우리가 사용한 데이터. 어떤 자산을, 어떤 기간에, 어디서 가져왔는가.
- **"methodology"** = 방법론. 데이터를 어떻게 가공해서 포트폴리오를 만들었는가.
- **"constructing value and momentum portfolios"** = 가치 포트폴리오와 모멘텀 포트폴리오를 구성. 단순히 데이터를 모은 게 아니라, **투자 전략을 실제로 시뮬레이션**하는 것이다.
- **"across markets and asset classes"** = 시장과 자산군을 걸쳐서. 이것이 이 논문의 핵심 — "Everywhere".

왜 이 섹션이 중요한가? 실증 논문에서 **데이터 섹션은 모든 결론의 기반**이다. 데이터가 잘못되면 그 위에 쌓은 모든 분석이 무너진다. 심사자(reviewer)가 가장 꼼꼼히 보는 부분이기도 하다.

---

## A. Data

> 이제 5개 자산군의 데이터를 하나씩 설명한다. 왜 5개인가? 8개 시장/자산군 중 주식은 4개 시장(US, UK, Europe, Japan)이지만 데이터 소스가 비슷하므로 하나의 소절(A.1)에서 다루고, 나머지는 각각 하나씩 소절을 갖는다.

---

### A.1. Global Individual Stocks (글로벌 개별 주식)

> "We examine value and momentum portfolios of individual stocks globally across four equity markets: the United States, the United Kingdom, continental Europe, and Japan."

#### 뜯기

첫 문장부터 범위를 명확히 잡는다.

- **"individual stocks"** = 개별 종목. 삼성전자, 애플 같은 개별 회사의 주식 한 종목 한 종목을 의미한다. 이후에 나오는 "국가지수(equity indices)"는 나라 전체의 주식시장을 하나의 자산으로 보는 것이므로 구별해야 한다.
- **4개 시장**: 미국, 영국, 유럽 대륙(영국 제외), 일본. 왜 이 4개인가? 이것이 전 세계 **선진국 주식시장의 대부분**을 차지하기 때문이다. 글로벌 시가총액의 약 85% 이상.

💡 **왜 "continental Europe"인가?** 영국은 주식시장의 역사, 규모, 데이터 접근성이 유럽 대륙 국가들과 다르다. 런던 증권거래소(LSE)는 세계 최대 거래소 중 하나이고, 데이터가 별도로 잘 정리되어 있다. 그래서 UK를 따로 떼어내고, 프랑스/독일/이탈리아 등을 묶어서 "continental Europe"으로 분류한다.

> 📚 **더 깊이**: [ch02 금융시장 기초](../chapters/ch02-finance-basics.md) — 주식시장의 구조, 시가총액의 의미

---

#### 미국 주식 데이터

> "The U.S. stock universe consists of all common equity in CRSP (sharecodes 10 and 11) with a book value from Compustat in the previous 6 months, and at least 12 months of past return history from January 1972 to July 2011."

##### 뜯기

이 문장 하나에 **미국 주식 연구의 표준 레시피**가 압축되어 있다. 하나씩 풀어보자.

**"common equity in CRSP (sharecodes 10 and 11)"**

- **CRSP** = Center for Research in Security Prices. 시카고 대학이 운영하는 미국 주가 데이터베이스. 1926년부터 모든 미국 상장 주식의 가격, 수익률, 거래량 데이터를 제공한다. 금융학 실증 연구의 **표준 데이터 소스**.
- **sharecode** = CRSP가 주식 유형을 분류하는 코드. 숫자 2자리.
  - **10** = 일반 보통주 (ordinary common shares)
  - **11** = 일반 보통주 (certificates, 약간 다른 형태이지만 본질적으로 동일)
- 왜 10과 11만? 다른 코드들은 ADR(외국 주식의 미국 거래분), REIT(부동산투자신탁), 클로즈드엔드 펀드 등 "순수한 보통주"가 아닌 것들이다. 이것들을 섞으면 분석이 오염된다.

**"a book value from Compustat in the previous 6 months"**

- **Compustat** = Standard & Poor's가 운영하는 기업 재무제표 데이터베이스. 기업의 매출, 이익, 자산, 부채 등 회계 정보가 담겨 있다.
- **book value** = 장부가치(Book Equity). 회사의 순자산. 총자산에서 총부채를 빼면 나온다.
- **"in the previous 6 months"** = 직전 6개월 이내에 장부가치 데이터가 있어야 한다. 왜 6개월? 기업의 재무제표는 보통 **회계연도 종료 후 몇 달 뒤에야 공개**된다. 12월에 끝나는 회계연도의 재무제표가 실제로 투자자에게 도달하는 건 다음 해 3~6월이다. 6개월 래그(lag)를 두는 것은 **"아직 공개되지 않은 정보를 사용하는 선견편향(look-ahead bias)을 방지"**하기 위함이다.

💡 **선견편향(Look-ahead Bias)이란?** 실제 투자자가 그 시점에 알 수 없었던 미래 정보를 사용해서 과거의 투자 성과를 시뮬레이션하는 오류. 예: "2023년 3월에 투자 결정을 내린다"고 가정하면서, 2023년 6월에야 발표될 재무제표 데이터를 사용하면 → 실제로는 불가능한 전략이 "성과가 좋다"고 나올 수 있다.

**"at least 12 months of past return history"**

- 모멘텀 시그널(MOM2-12)을 계산하려면 **과거 12개월의 수익률 데이터**가 필요하다. 데이터가 12개월 미만인 종목은 모멘텀을 계산할 수 없으므로 제외.

**"from January 1972 to July 2011"**

- **기간**: 1972년 1월 ~ 2011년 7월. **약 40년**의 데이터. 왜 1972년부터? Compustat의 장부가치 데이터가 1962년경부터 시작되지만, 초기에는 커버리지가 얇다. 1972년이면 충분히 넓은 종목 커버리지가 확보된다. 또한 CRSP의 일간 수익률 데이터도 1962년 이후 안정적이다.

---

#### 제외 항목

> "We exclude ADRs, REITs, financials, closed-end funds, foreign shares, and stocks with share prices less than $1 at the beginning of each month."

##### 뜯기

제외 목록 하나하나에 이유가 있다.

| 제외 항목 | 이유 |
|----------|------|
| **ADRs** (American Depositary Receipts) | 외국 기업이 미국에서 거래되는 증서. 이미 해당 국가 시장(UK, Europe, Japan)에서 원주식으로 포함됨 → 이중 계산 방지 |
| **REITs** (Real Estate Investment Trusts) | 부동산투자신탁. 수익 구조가 일반 주식과 매우 다름. 배당 의무(소득의 90% 이상)가 있어 가격 움직임이 다르다 |
| **Financials** (금융업) | 은행, 보험사 등. 장부가치의 의미가 제조업과 완전히 다름. 금융업의 "자산"은 대부분 대출금이고, 레버리지가 극단적이라 BE/ME 비교가 왜곡됨 |
| **Closed-end funds** | 폐쇄형 펀드. 이것은 "회사"가 아니라 "다른 주식들의 바구니". 포함하면 이중 계산 |
| **Foreign shares** | 미국 거래소에 상장된 외국 주식. ADR과 유사한 이유 |
| **$1 미만 주식** | 페니스탁(penny stock). 유동성이 극히 낮고, 매수-매도 호가 차이(bid-ask spread)가 가격의 수십%에 달할 수 있어 실제 거래가 사실상 불가능 |

> 📚 **더 깊이**: [ch08 논문의 데이터](../chapters/ch08-data.md) — 각 제외 항목의 상세 이유

---

#### 유동성 필터: 시총 상위 90%

> "We limit the remaining universe of stocks in each market to a very liquid set of securities that could be traded for reasonably low cost at reasonable trading volume size."

##### 뜯기

왜 유동성이 중요한가? 논문에서 "전략이 돈을 번다"고 말하려면, **실제로 그 전략을 실행할 수 있어야** 한다. 하루에 100주만 거래되는 초소형주로 10억 원을 운용하면, 주문 자체가 가격을 움직여서 "이론적 수익"이 증발한다.

> "Specifically, we rank stocks based on their beginning-of-month market capitalization in descending order and include in our universe the number of stocks that account cumulatively for 90% of the total market capitalization of the entire stock market."

##### 뜯기

**방법**: 매월 초, 모든 주식을 시가총액(주가 × 발행주식수) 순서로 큰 것부터 나열한다. 위에서부터 내려가면서 시가총액을 누적한다. 누적 합이 전체 시장 시가총액의 **90%**에 도달하면 그 선까지의 종목만 유니버스에 포함.

숫자 예시로 이해해보자:

| 순위 | 종목 | 시총 | 누적 시총 | 누적 비율 | 포함? |
|------|------|------|---------|---------|------|
| 1 | 애플 | 500조 | 500조 | 25% | O |
| 2 | 마이크로소프트 | 400조 | 900조 | 45% | O |
| 3 | 아마존 | 300조 | 1,200조 | 60% | O |
| ... | ... | ... | ... | ... | O |
| 354 | XYZ | 1조 | 1,800조 | 90% | O ← 여기까지 |
| 355 | ABC | 0.5조 | 1,800.5조 | 90.025% | X |
| ... | 소형주 수천 개 | ... | ... | ... | X |

결과: **수천 개 종목 중 상위 수백 개만** 남는다. 나머지 10% 시가총액에 해당하는 수천 개의 소형주는 제외.

---

> "This universe corresponds to an extremely liquid and tradeable set of securities."

##### 뜯기

이 필터가 만들어내는 유니버스는 **실제로 거래 가능한** 종목들이다. 기관투자자가 수억 달러를 운용해도 문제 없는 수준.

> "For instance, over our sample period this universe corresponds to the largest 17% of firms on average in the"

(p.934로 이어짐)

> "United States. For the U.S. stock market, at the beginning of the sample period (January 1972) our universe consists of the 354 largest firms and by the end of our sample period (July 2011) the universe comprises the 676 largest names. Hence, our sample of U.S. equities is significantly larger and more liquid than the Russell 1000."

##### 뜯기

구체적 숫자를 주고 있다:

- **평균적으로 상위 17%의 기업** — 전체 기업 수의 17%만 포함. 시가총액 기준으로 자르니까, 종목 수로 보면 소수만 남는다.
- **1972년 초**: 354개 기업. **2011년 7월**: 676개 기업. 시간이 지남에 따라 상장 기업 수가 늘었으니 유니버스도 커졌다.
- **Russell 1000보다 크고 유동적** — Russell 1000은 미국 상위 1,000개 기업의 지수. 이 논문의 유니버스는 종목 수는 적지만(354~676개), 시총 기준으로는 Russell 1000보다 **더 큰 기업들만** 포함한다. Russell 1000에는 시총 하위권의 작은 기업도 포함되지만, 이 논문은 시총 누적 90%선까지의 대형주만.

💡 **왜 이걸 강조하는가?** "우리 결과는 소형주의 이상 현상에 기대지 않는다"는 방어. 소형주는 거래비용이 높고 유동성이 낮아서 "논문에서는 돈 되지만 실전에서는 안 된다"는 비판을 자주 받는다. 저자들은 **대형 유동주만** 사용함으로써 이 비판을 선제적으로 차단한다.

---

#### 각주 4

> <sup>4</sup> "This procedure is similar to how MSCI defines its universe of stocks for its global stock indices."

##### 뜯기

**MSCI**(Morgan Stanley Capital International)는 전 세계 기관투자자들이 벤치마크로 사용하는 **글로벌 주가지수**를 만드는 회사다. MSCI World Index, MSCI Emerging Markets Index 등.

MSCI도 자사 지수에 포함할 종목을 선정할 때 **시가총액 누적 커버리지** 방식을 사용한다 — "전체 시장의 약 85%를 커버하는 대형+중형주"를 포함하는 식. 이 논문의 90% 기준과 원리가 같다.

이 각주의 목적: **"우리의 유니버스 구성 방법은 자의적인 게 아니라, 업계 표준(MSCI)과 유사하다"**는 정당화.

---

#### 미국 외 주식 데이터

> "For stocks outside of the United States, we use Datastream data from the United Kingdom, continental Europe (across all European stock markets, excluding the United Kingdom), and Japan. We restrict the universe in each market using the same criteria used for U.S. stocks."

##### 뜯기

- **Datastream** = Thomson Reuters(현 Refinitiv)가 운영하는 글로벌 금융 데이터베이스. CRSP가 미국 전문이라면, Datastream은 **미국 외 시장**의 표준 데이터 소스. 주가, 재무제표, 경제 지표 등을 전 세계적으로 커버한다.
- **"same criteria"** = 미국과 동일한 기준 적용. ADR/REIT/금융업 제외, 시총 상위 90% 필터 등. **방법론의 일관성**이 핵심이다. 각 시장마다 다른 기준을 쓰면, 결과 차이가 데이터 차이 때문인지 시장 특성 때문인지 구분할 수 없다.

> "On average over the sample period, our universe represents the largest 13%, 20%, and 26% of firms in the United Kingdom, Europe, and Japan, respectively."

##### 뜯기

| 시장 | 포함 비율 (종목 수 기준) |
|------|----------------------|
| 미국 | 상위 17% |
| 영국 | 상위 13% |
| 유럽 | 상위 20% |
| 일본 | 상위 26% |

미국(17%)보다 영국(13%)이 더 적은 비율을 포함하는 건 영국 시장의 시가총액 집중도가 높다는 뜻이다(HSBC, BP 같은 초대형주가 전체 시총의 큰 비중). 일본(26%)이 가장 많은 비율을 포함하는 건 일본 시장에 중소형주가 많아서 90% 커버리지를 채우려면 더 많은 종목이 필요하다는 뜻.

> "Data on prices and returns come from Datastream, and data on book values are from Worldscope."

##### 뜯기

- **Worldscope** = Datastream과 함께 제공되는 글로벌 기업 재무 데이터. 미국의 Compustat에 해당하는 해외판이라고 보면 된다. 장부가치(book equity) 계산에 필요한 회계 데이터가 여기서 온다.

---

#### 보수적 추정의 논리

> "Most studies of individual stocks examine a much broader and less liquid set of securities. We restrict our sample to a much more liquid universe (roughly the largest 20% of stocks in each market) to provide reasonable and conservative estimates of an implementable set of trading strategies and to better compare those strategies with the set of strategies we employ in index futures, currencies, government bonds, and commodity futures, which are typically more liquid instruments."

##### 뜯기

세 가지 이유를 제시한다:

1. **"reasonable and conservative estimates"** — 대형 유동주만 사용하면 거래비용이 낮으므로, 전략의 **순수익이 더 현실적**. 소형주를 포함하면 총수익은 커 보이지만 거래비용을 빼면 이야기가 달라진다.

2. **"implementable set of trading strategies"** — **실제로 실행 가능**한 전략. 논문에서만 존재하는 이론적 전략이 아니라, 펀드매니저가 실제로 따라할 수 있는 전략.

3. **"better compare"** — 주식 외 자산군(선물, 통화, 채권, 원자재)은 **원래 유동성이 매우 높다**. 소형주를 포함한 주식 전략과 비교하면 유동성 수준이 맞지 않는다. 비교의 공정성을 위해 주식도 유동성을 맞춰준다.

> "Our results are conservative since value and momentum premia are larger among smaller, less liquid securities over the sample period we study."

##### 뜯기

핵심 방어 논리: **"우리가 과장하는 게 아니라, 오히려 과소평가하고 있다."** 소형주에서 가치/모멘텀 효과가 더 크다는 것은 기존 연구에서 잘 알려진 사실이다. 대형주만 사용함으로써 이 추가 수익을 포기했다 → **결과가 보수적(conservative)**이다.

---

#### 각주 5

> <sup>5</sup> "Hong, Lim, and Stein (2000), Grinblatt and Moskowitz (2004), Fama and French (2012), and Israel and Moskowitz (2012) show that value and momentum returns are inversely related to the size of securities over the time period studied here, though Israel and Moskowitz (2012) show this relation is not robust for momentum in other sample periods. Value and momentum returns have also been shown to be stronger in less liquid emerging markets (Rouwenhorst (1998), Erb and Harvey (2006), Griffin, Ji, and Martin (2003)). A previous version of this paper used a broader and less liquid set of stocks that exhibited significantly stronger value and momentum returns."

##### 뜯기

이 각주는 **"소형주 제외 = 보수적"이라는 주장의 근거 문헌**을 제시한다.

| 논문 | 핵심 발견 |
|------|---------|
| **Hong, Lim, Stein (2000)** | 소형주에서 모멘텀이 더 강함. 이유: 소형주는 애널리스트 커버리지가 적어서 정보가 느리게 퍼짐 |
| **Grinblatt & Moskowitz (2004)** | 소형주에서 가치/모멘텀 프리미엄이 더 큼 |
| **Fama & French (2012)** | 글로벌 주식에서 가치/모멘텀은 소형주일수록 강함 |
| **Israel & Moskowitz (2012)** | 가치는 소형주에서 일관되게 강하지만, 모멘텀은 시기에 따라 다름 (소형주 우위가 항상은 아님) |
| **Rouwenhorst (1998)** | 신흥국 시장(유동성 낮음)에서도 모멘텀 존재, 더 강함 |
| **Erb & Harvey (2006)** | 신흥국에서 가치/모멘텀 효과가 더 큼 |
| **Griffin, Ji, Martin (2003)** | 글로벌 시장에서 모멘텀은 국가별 요인이 지배적 |

마지막 문장이 특히 중요하다: **"이 논문의 이전 버전은 더 넓고 덜 유동적인 종목 집합을 사용했는데, 가치와 모멘텀 수익이 훨씬 더 강했다."** 즉, 심사 과정에서 유니버스를 좁힌 것이다. 심사자가 "소형주 효과를 빼라"고 요구했을 가능성이 높다. 그래도 결론이 바뀌지 않았다 = 결과가 강건(robust)하다.

---

#### 시계열과 종목 수

> "All series are monthly and end in July 2011. The U.S. and U.K. stock samples begin in January 1972. The Europe and Japan stock samples begin in January 1974."

##### 뜯기

- **월간(monthly) 데이터** — 일간이 아니라 월간. 왜? (1) 일간 데이터의 노이즈가 크고, (2) 실제 포트폴리오 리밸런싱은 보통 월 단위, (3) 계산량을 줄일 수 있다.
- **US/UK: 1972년 1월** — 약 40년.
- **Europe/Japan: 1974년 1월** — 2년 늦게 시작. Datastream의 유럽/일본 데이터 커버리지가 1974년부터 충분해지기 때문.

> "The average (minimum) number of stocks in each market over their respective sample periods is 724 (354) in the United States, 147 (76) in the United Kingdom, 290 (96) in Europe, and 471 (148) in Japan."

##### 뜯기

| 시장 | 평균 종목 수 | 최소 종목 수 | 기간 |
|------|-----------|-----------|------|
| **미국** | 724 | 354 | 1972.01~2011.07 |
| **영국** | 147 | 76 | 1972.01~2011.07 |
| **유럽** | 290 | 96 | 1974.01~2011.07 |
| **일본** | 471 | 148 | 1974.01~2011.07 |

**평균(average)**은 전체 기간의 평균이고, **최소(minimum)**는 데이터가 가장 적었던 시점(보통 기간 초기)의 종목 수다.

미국의 354→676개(앞에서 언급)는 시간에 따라 유니버스가 커졌음을 보여주고, 평균 724개는 후반기에 더 많았음을 의미한다. 영국이 147개로 가장 적은 것은 영국 시장 자체가 미국보다 작고, 상위 13%만 취했기 때문이다.

이 숫자들이 중요한 이유: 포트폴리오를 3분위(tertile)로 나눌 때, 최소 종목 수가 76개(영국)면 각 분위에 약 25개씩 들어간다. 25개면 포트폴리오 분산이 **어느 정도는 되지만 완벽하지는 않다**. 이것이 후에 "왜 3분위인가(5분위가 아닌가)"의 이유와 연결된다.

---

### A.2. Global Equity Indices (글로벌 주가지수)

> "The universe of country equity index futures consists of the following 18 developed equity markets: Australia, Austria, Belgium, Canada, Denmark, France, Germany, Hong Kong, Italy, Japan, Netherlands, Norway, Portugal, Spain, Sweden, Switzerland, the United Kingdom, and the United States."

#### 뜯기

여기서부터는 **개별 종목이 아니라 "나라 전체"**를 하나의 자산으로 본다. 18개 선진국의 주가지수 선물(equity index futures)을 거래하는 것이다.

18개국을 전부 나열하자:

| 지역 | 국가 |
|------|------|
| 북미 | 미국, 캐나다 |
| 아시아-태평양 | 호주, 홍콩, 일본 |
| 서유럽 | 영국, 프랑스, 독일, 이탈리아, 네덜란드, 벨기에, 스위스, 스페인, 포르투갈 |
| 북유럽 | 스웨덴, 노르웨이, 덴마크, 오스트리아 |

💡 **왜 "선진국"만?** 2011년 기준으로 신흥국(한국, 중국, 인도 등)의 주가지수 선물 시장은 역사가 짧고 유동성이 불안정했다. 일관된 장기 데이터를 얻기 어렵다.

> <sup>6</sup> "Austria, Belgium, Denmark, Norway, and Portugal are not index futures but are constructed from the returns of an equity index swap instrument using the respective local market index from MSCI."

#### 각주 6 뜯기

18개 중 5개국(오스트리아, 벨기에, 덴마크, 노르웨이, 포르투갈)은 **실제 인덱스 선물이 아니다**. 이 나라들은 시장 규모가 작아서 유동적인 주가지수 선물 시장이 없다.

대신 **주가지수 스왑(equity index swap)**을 사용했다. 스왑이란 두 당사자가 미래의 현금흐름을 교환하는 계약이다. 여기서는 "MSCI 현지 시장 지수의 수익률"을 주고받는 스왑 — 즉 선물과 경제적으로 거의 동일한 효과를 내는 대체 수단.

왜 이걸 공개하는가? **데이터의 정확성과 한계를 솔직히 밝히는 것**이 학술 논문의 의무다. 선물과 스왑은 수수료 구조가 약간 다르므로, 수익률에 미세한 차이가 있을 수 있다.

---

> "Returns and price data as well as book values are obtained from MSCI and Bloomberg. The sample covers the period January 1978 to July 2011, with the minimum number of equity indices being 8 and all 18 indices represented after 1980."

#### 뜯기

- **MSCI + Bloomberg** = 데이터 소스. MSCI는 자사 지수의 BE/ME 비율을 제공하고, Bloomberg은 가격/수익률 데이터를 제공.
- **1978년 1월~2011년 7월** = 약 34년. 개별 주식(1972년)보다 6년 늦게 시작. MSCI 국가지수 데이터가 1970년대 후반부터 이용 가능해지기 때문.
- **최소 8개 지수** = 초기(1978~1979)에는 8개국만 데이터 존재.
- **1980년 이후 18개 전부** = 1980년부터 모든 18개국 커버.

> "The returns on the country equity index futures do not include any returns on collateral from transacting in futures contracts, hence these are comparable to returns in excess of the risk-free rate."

#### 뜯기

이 문장은 기술적이지만 중요하다.

**선물(futures) 계약**은 주식과 달리, 처음에 전액을 지불하지 않는다. 증거금(margin, 보통 계약 가치의 5~15%)만 내면 된다. 나머지 돈은 국채 등에 투자해서 이자(담보 수익, collateral return)를 벌 수 있다.

이 논문에서는 **담보 수익을 포함하지 않았다**. 왜?

- 담보 수익을 포함하면 = **총수익률(total return)** = 전략 수익 + 무위험 이자
- 담보 수익을 빼면 = **초과수익률(excess return)** = 전략 수익만

초과수익률로 보고하면 다른 자산군의 수익률과 **사과 대 사과** 비교가 가능하다. "이 전략이 시장 무위험 이자율 위에 얼마나 더 벌어주는가?"라는 질문에 바로 답할 수 있다.

---

### A.3. Currencies (통화)

> "We obtain spot exchange rates from Datastream covering the following 10 currencies: Australia, Canada, Germany (spliced with the Euro), Japan, New Zealand, Norway, Sweden, Switzerland, the United Kingdom, and the United States."

#### 뜯기

10개 통화:

| # | 국가 | 통화 | 비고 |
|---|------|------|------|
| 1 | 호주 | AUD | |
| 2 | 캐나다 | CAD | |
| 3 | 독일→유로존 | DEM→EUR | 1999년 유로 도입 전 독일 마르크, 이후 유로로 접합(splice) |
| 4 | 일본 | JPY | |
| 5 | 뉴질랜드 | NZD | |
| 6 | 노르웨이 | NOK | |
| 7 | 스웨덴 | SEK | |
| 8 | 스위스 | CHF | |
| 9 | 영국 | GBP | |
| 10 | 미국 | USD | 기준 통화(base currency) |

💡 **"spliced with the Euro"란?** 1999년 1월 유로가 도입되면서 독일 마르크(DEM)가 사라졌다. 이 논문은 1999년 이전에는 DEM 환율을, 1999년 이후에는 EUR 환율을 이어붙여(splice) 하나의 연속 시계열로 만들었다. 환율 비율을 고정 전환율(1 EUR = 1.95583 DEM)로 맞추면 연속성이 유지된다.

> "The data cover the period January 1979 to July 2011, where the minimum number of currencies is 7 at any point in time and all 10 currencies are available after 1980."

#### 뜯기

- **1979년 1월~2011년 7월** = 약 33년.
- **최소 7개** = 초기에 일부 통화 데이터 부재.
- **1980년 이후 10개 전부**.

> "We compute returns from currency forward contracts or MSCI spot price data and Libor rates, where currency returns are all dollar denominated and implicitly include the local interest rate differential."

#### 뜯기

통화 수익률 계산 방법이 다른 자산군과 다르다. 두 가지 방법을 사용:

**방법 1: 선도환 계약(forward contract)**

선도환이란 "미래의 특정 날짜에, 미리 정한 환율로 통화를 교환하겠다"는 계약이다. 1개월 선도환을 매월 롤오버(갱신)하면 통화 투자의 수익률을 얻을 수 있다.

**방법 2: 현물 환율(spot rate) + 금리차(Libor)**

현물 환율의 변동 + 두 나라의 금리 차이. 예를 들어 호주 달러에 투자하면 AUD/USD 환율 변동 + (호주 금리 - 미국 금리)를 벌 수 있다.

- **"all dollar denominated"** = 모든 수익률을 미국 달러 기준으로 표시. 일본 투자자가 엔화로 볼 때와 미국 투자자가 달러로 볼 때 수익이 다를 수 있으므로, 기준 통화를 통일.
- **"implicitly include the local interest rate differential"** = 금리차가 암묵적으로 포함. 선도환 가격 자체가 금리차를 반영하기 때문이다 (이것은 **무위험 금리 평형(Covered Interest Rate Parity)**이라는 금융 원리에 의한 것).

💡 **Libor란?** London Interbank Offered Rate. 런던에서 대형 은행들이 서로 돈을 빌려줄 때 적용하는 금리. 2012년 조작 스캔들 이후 SOFR 등으로 대체되고 있지만, 이 논문의 데이터 기간(~2011)에는 글로벌 단기 금리의 표준 지표였다.

---

### A.4. Global Government Bonds (글로벌 국채)

> "Bond index returns come from Bloomberg and Morgan Markets, short rates and 10-year government bond yields are from Bloomberg, and inflation forecasts are obtained from investment bank analysts' estimates as compiled by Consensus Economics."

#### 뜯기

세 종류의 데이터와 세 개의 소스:

| 데이터 | 소스 | 용도 |
|--------|------|------|
| 채권지수 수익률 | Bloomberg, Morgan Markets | 모멘텀 계산(과거 수익률) |
| 단기 금리, 10년 국채 금리 | Bloomberg | 가치 측정(금리 변화) |
| 인플레이션 전망 | Consensus Economics | 실질환율 계산(통화 가치 측정에 사용) |

- **Morgan Markets** = JP Morgan이 운영하는 채권 데이터 플랫폼.
- **Consensus Economics** = 주요 투자은행 애널리스트들의 경제 전망을 종합하는 서비스. "앞으로 인플레이션이 얼마나 될 것인가"에 대한 전문가 합의치.

> "We obtain government bond data for the following 10 countries: Australia, Canada, Denmark, Germany, Japan, Norway, Sweden, Switzerland, the United Kingdom, and the United States."

#### 뜯기

10개국:

| # | 국가 | 비고 |
|---|------|------|
| 1 | 호주 | |
| 2 | 캐나다 | |
| 3 | 덴마크 | |
| 4 | 독일 | 유로 도입 후에도 독일 국채(Bund)는 유로존 벤치마크 |
| 5 | 일본 | |
| 6 | 노르웨이 | |
| 7 | 스웨덴 | |
| 8 | 스위스 | |
| 9 | 영국 | |
| 10 | 미국 | |

주가지수(18개국)나 통화(10개)와 비교하면, 채권은 **10개국**이다. 이 나라들은 모두 (1) 독립적인 통화정책을 가지고, (2) 유동적인 국채 시장이 있는 선진국이다.

💡 **왜 프랑스, 이탈리아, 스페인 등이 빠졌나?** 유로존 국가들은 유로 도입 이후 통화정책이 통합되어 금리가 수렴했다. 독일 국채(Bund)가 유로존 전체의 벤치마크 역할을 하므로, 독일만 포함해도 유로존을 대표할 수 있다.

> "The sample covers the period January 1982 to July 2011, where the minimum number of country bond returns is 5 at any point in time and all 10 country bonds are available after 1990."

#### 뜯기

- **1982년 1월~2011년 7월** = 약 30년. 다른 자산군보다 늦게 시작. 채권 데이터의 체계적 수집이 1980년대 초부터.
- **최소 5개** = 1982~1989년에는 5~9개국만 데이터 존재.
- **1990년 이후 10개 전부**.

---

### A.5. Commodity Futures (원자재 선물)

> "We cover 27 different commodity futures obtained from several sources."

#### 뜯기

**27개** 원자재. 이것은 다른 원자재 연구와 비교해도 매우 포괄적인 범위다.

> "Data on Aluminum, Copper, Nickel, Zinc, Lead, and Tin are from the London Metal Exchange (LME). Brent Crude and Gas Oil are from the Intercontinental Exchange (ICE). Live Cattle, Feeder Cattle, and Lean Hogs are from the Chicago Mercantile Exchange (CME). Corn, Soybeans, Soy Meal, Soy Oil, and Wheat are from the Chicago Board of Trade (CBOT). WTI Crude, RBOB Gasoline, Heating Oil, and Natural Gas are from the New York Mercantile Exchange (NYMEX). Gold and Silver are from the New York Commodities Exchange (COMEX). Cotton, Coffee, Cocoa, and Sugar are from New York Board of Trade (NYBOT), and Platinum data are from the Tokyo Commodity Exchange (TOCOM)."

#### 뜯기

27개 원자재를 거래소별로 정리하면:

| 거래소 | 위치 | 원자재 | 개수 |
|--------|------|--------|------|
| **LME** (London Metal Exchange) | 런던 | 알루미늄, 구리, 니켈, 아연, 납, 주석 | 6 |
| **ICE** (Intercontinental Exchange) | 런던/뉴욕 | 브렌트유, 가스오일 | 2 |
| **CME** (Chicago Mercantile Exchange) | 시카고 | 생우, 비육우, 린호그(돼지) | 3 |
| **CBOT** (Chicago Board of Trade) | 시카고 | 옥수수, 대두, 대두박, 대두유, 밀 | 5 |
| **NYMEX** (New York Mercantile Exchange) | 뉴욕 | WTI 원유, RBOB 가솔린, 난방유, 천연가스 | 4 |
| **COMEX** (New York Commodities Exchange) | 뉴욕 | 금, 은 | 2 |
| **NYBOT** (New York Board of Trade) | 뉴욕 | 면화, 커피, 코코아, 설탕 | 4 |
| **TOCOM** (Tokyo Commodity Exchange) | 도쿄 | 백금 | 1 |
| | | **합계** | **27** |

이 원자재들은 크게 **5가지 카테고리**로 나뉜다:
- **금속**: 알루미늄, 구리, 니켈, 아연, 납, 주석, 금, 은, 백금
- **에너지**: 브렌트유, WTI 원유, RBOB 가솔린, 난방유, 천연가스, 가스오일
- **축산**: 생우, 비육우, 린호그
- **곡물/유지**: 옥수수, 대두, 대두박, 대두유, 밀
- **소프트(열대작물)**: 면화, 커피, 코코아, 설탕

💡 **왜 이렇게 다양한 원자재를 포함하는가?** "Everywhere"라는 제목의 의미다. 금과 원유만 보면 "금융 자산에만 해당하는 현상"이라고 반박당할 수 있다. 하지만 돼지고기, 커피, 설탕에서도 가치/모멘텀이 작동한다면? 이건 **자산의 특성이 아니라 투자자 행동의 패턴**이라는 강력한 증거가 된다.

---

> "The sample covers the period January 1972 to July 2011, with the minimum number of commodities being 10 at any point in time and all 27 commodities available after 1995."

#### 뜯기

- **1972년 1월~2011년 7월** = 약 40년. 미국 주식과 동일하게 가장 긴 기간.
- **최소 10개** = 초기에는 10개 원자재만.
- **1995년 이후 27개 전부** = LME의 알루미늄, 니켈 등이 1980~90년대에 선물 시장이 열리면서 추가.

---

#### 원자재 수익률 계산

> "Returns for commodity futures are calculated as follows. Each day we compute the daily excess return of the most liquid futures contract, which is typically the nearest- or next nearest-to-delivery contract, and then compound the daily returns to a total return index from which we compute returns at"

(p.936으로 이어짐)

> "a monthly horizon."

##### 뜯기

원자재 선물의 수익률 계산은 주식보다 복잡하다. 단계별로:

1. **가장 유동적인 선물 계약 선택** — 보통 만기가 가장 가까운(nearest) 계약이나 그 다음(next nearest) 계약. 만기가 가까울수록 거래가 활발하다.

2. **일간 초과수익률 계산** — 선물 가격의 일일 변동. "초과(excess)"라 하는 이유는 선물이 증거금만 내고 거래하므로, 담보 수익(무위험 이자)을 포함하지 않기 때문.

3. **일간 → 월간 복리** — 일간 수익률을 복리로 쌓아서 월간 수익률로 만든다.

$$r_{\text{monthly}} = \prod_{d=1}^{D}(1 + r_d) - 1$$

여기서 $r_d$는 일간 수익률, $D$는 해당 월의 거래일 수.

💡 **왜 일간으로 계산해서 월간으로 합산하나?** 선물은 **만기(delivery date)가 있어서 롤오버(rollover)**가 필요하다. 만기 전에 다음 달 계약으로 갈아타는데, 이 롤오버가 월중에 일어날 수 있다. 일간 단위로 수익률을 계산해야 롤오버 시점의 수익률을 정확히 포착할 수 있다.

---

> "Bessembinder (1992), de Roon, Nijman, and Veld (2000), Moskowitz, Ooi, and Pedersen (2012), and Koijen et al. (2012) compute futures returns similarly."

##### 뜯기

이 수익률 계산 방법이 자의적이지 않음을 보여주는 선행 연구 인용.

| 논문 | 맥락 |
|------|------|
| **Bessembinder (1992)** | 원자재 선물 수익의 체계적 분석 선구자 |
| **de Roon, Nijman, Veld (2000)** | 원자재 선물의 위험 프리미엄 분석 |
| **Moskowitz, Ooi, Pedersen (2012)** | "Time Series Momentum" 논문. 이 논문의 공저자 2명이 참여한 자매 논문 |
| **Koijen et al. (2012)** | "Carry" 전략 논문. 선물 수익률 계산법 동일 |

> "All returns are denominated in U.S. dollars and do not include the return on collateral associated with the futures contract."

##### 뜯기

두 가지 통일 원칙:

1. **달러 표시** — 모든 원자재의 수익률을 미국 달러 기준으로. 원자재 선물은 대부분 달러로 거래되므로 자연스럽다.

2. **담보 수익 미포함** — 주가지수 선물과 동일한 논리. 선물에 투자할 때 증거금 외의 돈을 국채에 투자해서 얻는 이자를 포함하지 않음 → **초과수익률**로 비교 가능.

---

## B. Value and Momentum Measures (가치와 모멘텀 측정)

> 지금까지 "어떤 데이터를 모았는가"를 설명했다. 이제 "그 데이터로 어떻게 가치와 모멘텀을 측정하는가"를 설명한다. 이것이 연구 설계의 핵심이다 — **같은 데이터라도 측정 방법이 다르면 결론이 달라질 수 있다.**

---

### 설계 철학

> "To measure value and momentum, we use the simplest and, to the extent a standard exists, most standard measures. We are not interested in coming up with the best predictors of returns in each asset class. Rather, our goal is to maintain a simple and fairly uniform approach that is consistent across asset classes and minimizes the pernicious effects of data snooping."

#### 뜯기

이 문단은 **전체 연구의 방법론적 철학**을 선언한다. 세 가지 핵심:

**1. "simplest... most standard measures" — 가장 단순하고 표준적인 측정치**

수십 가지의 가치 측정치(BE/ME, P/E, EV/EBITDA, P/S 등)와 모멘텀 측정치(MOM1-3, MOM2-12, MOM7-12 등)가 존재한다. 이 논문은 그 중 **가장 기본적인 것**만 사용한다.

**2. "not interested in coming up with the best predictors" — 최고의 예측력에 관심 없다**

이것은 반직관적이다. 더 잘 맞추면 좋은 거 아닌가? 하지만 이 논문의 목표는 "돈을 가장 많이 버는 전략 찾기"가 아니라 "가치와 모멘텀이 어디서나 존재하는가?"라는 학술적 질문에 답하는 것이다. 최적의 측정치를 자산군마다 다르게 고르면 "그건 데이터에 맞춰서 골랐잖아"라는 공격을 받는다.

**3. "minimizes the pernicious effects of data snooping" — 데이터 스누핑의 해악 최소화**

💡 **데이터 스누핑(Data Snooping)이란?** 같은 데이터로 수백 가지 전략을 시도해서 "우연히 잘 맞는 것"을 찾아내는 것. 동전을 100번 던져서 "아, 37번째에서 43번째까지 7연속 앞면!" → "이 동전에는 37번째부터 앞면이 나오는 패턴이 있다!"라고 주장하는 것과 같다. 학술 연구의 **치명적 함정**.

이 논문은 데이터 스누핑을 최소화하기 위해 **모든 자산군에 거의 동일한(uniform) 측정치**를 사용한다. "주식에는 A, 채권에는 B, 원자재에는 C"처럼 각각 최적화하면 8번의 시도가 되지만, "전부 BE/ME 류의 단순 가치 측정"으로 통일하면 1번이다.

> "As such, if data snooping can be avoided, our results may therefore understate the true gross returns to value and momentum available from more thoughtfully chosen measures."

#### 뜯기

**"understate the true gross returns"** = 실제 가능한 수익률을 과소평가할 수 있다.

이것은 A.1에서 소형주를 제외한 것과 같은 논리다. **보수적(conservative) 접근**: "우리 결과가 부풀려진 게 아니다. 오히려 최적의 측정치를 썼다면 수익이 더 컸을 것이다."

> 📚 **더 깊이**: [ch09 가치와 모멘텀 측정](../chapters/ch09-measures.md) — 다양한 가치/모멘텀 측정치의 비교

---

### 주식의 가치 측정: BE/ME

> "For individual stocks, we use the common value signal of the ratio of the book value of equity to market value of equity, or book-to-market ratio, *BE/ME* (see Fama and French (1992, 1993) and Lakonishok, Shleifer, and Vishny (1994)), of the stock."

#### 뜯기

**BE/ME** = Book Equity / Market Equity = 장부가치 / 시장가치

$$\text{BE/ME} = \frac{\text{장부가치(Book Equity)}}{\text{시장가치(Market Equity)}}$$

이것이 **가장 기본적이고 가장 많이 연구된** 가치 측정치다. 인용된 논문들이 이 분야의 초석:

| 논문 | 기여 |
|------|------|
| **Fama & French (1992)** | BE/ME가 주식 수익률의 횡단면을 설명하는 핵심 변수임을 입증. "3팩터 모형"의 시작 |
| **Fama & French (1993)** | 위 발견을 팩터 모형으로 체계화. SMB(규모), HML(가치) 팩터 탄생 |
| **Lakonishok, Shleifer, Vishny (1994)** | BE/ME가 높은 주식이 수익이 좋은 이유는 위험 때문이 아니라 **투자자의 과잉반응** 때문이라고 주장. 행동재무학 진영의 대표 논문 |

---

#### 장부가치 래그

> "Book values are lagged 6 months to ensure data availability to investors at the time, and the most recent market values are used to compute the ratios."

##### 뜯기

두 가지 결정:

1. **장부가치: 6개월 래그** — 1월에 투자 결정을 내릴 때, 전년 6월까지의 장부가치를 사용. 왜? 회계 데이터가 실제로 공개되기까지 시간이 걸리기 때문 (선견편향 방지, 위에서 설명).

2. **시장가치: 현재 값 사용** — 장부가치는 6개월 전 것을 쓰지만, 시장가치(주가 × 발행주식수)는 **투자 결정 시점의 최신 값**을 사용.

이 두 번째 결정이 흥미로운데, Fama & French (1992)에서는 시장가치도 래그(6개월 전)를 사용했다. 이 논문은 왜 다르게 했는가? 바로 다음에 설명한다.

---

#### 동시 시장가치 사용: Asness & Frazzini (2012)

> "For the purposes of this paper, using lagged or contemporary prices rather than market values matched contemporaneously in time as in Fama and French (1992) is not important."

##### 뜯기

**"for the purposes of this paper"** — 이 논문의 목적상, 래그 가격을 쓰든 동시 가격을 쓰든 결론은 동일하다.

> "When using more recent prices in the value measure, the negative correlation between value and momentum is more negative and the value premium is slightly reduced, but our conclusions are not materially affected."

##### 뜯기

최신 가격을 쓰면:
- 가치와 모멘텀의 **음의 상관이 더 강해진다** (더 음수)
- 가치 프리미엄이 **약간 줄어든다**
- 하지만 **결론은 실질적으로 영향받지 않는다**

왜 이런 일이 일어나나? 최근에 주가가 크게 올랐다고 하자(= 높은 모멘텀). 동시 시장가치를 쓰면 분모(ME)가 커져서 BE/ME가 낮아진다(= 낮은 가치 시그널). 즉 **높은 모멘텀 주식이 자동으로 낮은 가치 주식이 된다** → 음의 상관이 더 강해진다.

> "A combination of value and momentum—one of the themes in this paper—obtains nearly identical pricing results regardless of whether we lag the price in the value measure."

##### 뜯기

가치와 모멘텀을 **결합(combination)**하면, 래그 여부에 관계없이 거의 동일한 결과. 이것이 이 논문의 핵심 주제 중 하나와 연결된다: **가치와 모멘텀을 함께 보는 것이 중요하다.**

> "Asness and Frazzini (2012) investigate this issue more thoroughly and argue that using contemporaneous market values can be important and ease interpretation when examining value in the presence of momentum, as we do in this paper."

##### 뜯기

- **Asness & Frazzini (2012)** — 이 주제에 대한 전문 논문. 이 논문의 공저자 Asness가 참여. "동시 시장가치를 사용하는 것이 더 깨끗한 가치 측정치를 만든다"고 주장.
- **"in the presence of momentum"** — 모멘텀도 함께 연구하는 상황에서는, 래그된 시장가치를 쓰면 가치 시그널에 **과거 모멘텀 정보가 오염**되는 문제가 있다.

> "Gerakos and Linnainmaa (2012) decompose value into book and market components and find that the market value of equity drives most of the relevant pricing information."

##### 뜯기

- **Gerakos & Linnainmaa (2012)** — BE/ME를 분해하면, 수익률 예측력의 대부분은 **분모(시장가치)**에서 온다. 장부가치(분자)는 상대적으로 덜 중요. 즉, "싼 주식이 돈을 버는 것"은 사실 "시장 가격이 낮은 주식이 돈을 버는 것"에 더 가깝다.

---

#### 각주 7

> <sup>7</sup> "While research has shown that other value measures are more powerful for predicting stock returns (e.g., Lakonishok, Shleifer, and Vishny (1994), Asness, Porter, and Stevens (2000), Piotroski (2000)), we maintain a basic and simple approach that is somewhat consistent across asset classes."

##### 뜯기

더 좋은 가치 측정치가 있다는 것을 **솔직히 인정**한다:

| 논문 | 더 강력한 가치 측정치 |
|------|-------------------|
| **Lakonishok, Shleifer, Vishny (1994)** | C/P (현금흐름/주가), E/P (이익/주가) 등 여러 비율의 조합 |
| **Asness, Porter, Stevens (2000)** | 복합 가치 시그널 (여러 비율의 결합) |
| **Piotroski (2000)** | F-Score: 재무 건전성 9가지 지표 조합 |

하지만 이것들은 **주식에만 적용 가능**하다. 원자재에는 "이익"이 없고, 통화에는 "장부가치"가 없다. **자산군 전체에 일관되게 적용할 수 있는 단순한 접근**을 유지하는 것이 이 논문의 선택이다.

---

### 주식의 모멘텀 측정: MOM2-12

> "For momentum, we use the common measure of the past 12-month cumulative raw return on the asset (see Jegadeesh and Titman (1993), Asness (1994), Fama and French (1996), and Grinblatt and Moskowitz (2004)), skipping the most recent month's return, *MOM2–12*."

#### 뜯기

$$\text{MOM2-12} = r_{t-12 \to t-2} = \prod_{k=2}^{12}(1+r_{t-k}) - 1$$

말로 풀면: **"2개월 전부터 12개월 전까지의 누적 수익률"**.

예시: 지금이 2024년 7월이라면
- $r_{t-12}$부터 $r_{t-2}$까지 = 2023년 7월 ~ 2024년 5월의 수익률
- 2024년 6월(직전 1개월)은 제외

인용 논문들:

| 논문 | 기여 |
|------|------|
| **Jegadeesh & Titman (1993)** | 모멘텀 전략의 수익성을 체계적으로 입증한 최초의 핵심 논문 |
| **Asness (1994)** | 이 논문의 공저자 Asness의 박사논문. 모멘텀과 가치의 관계 분석 |
| **Fama & French (1996)** | 모멘텀이 3팩터 모형으로 설명되지 않음을 인정(효율적 시장 진영의 양보) |
| **Grinblatt & Moskowitz (2004)** | 이 논문의 공저자 Moskowitz. 모멘텀의 소형주 의존성 분석 |

---

#### 왜 최근 1개월을 빼는가

> "We skip the most recent month, which is standard in the momentum literature, to avoid the 1-month reversal in stock returns, which may be related to liquidity or microstructure issues (Jegadeesh (1990), Lo and MacKinaly (1990), Boudoukh, Richardson, and Whitelaw (1994), Asness (1994), Grinblatt and Moskowitz (2004))."

##### 뜯기

**1개월 반전(1-month reversal)** — 지난 달에 많이 오른 주식이 **이번 달에 약간 떨어지는** 경향. 반대도 마찬가지: 지난 달에 많이 떨어진 주식이 이번 달에 약간 반등.

왜 이런 일이 일어나는가? 두 가지 설명:

1. **유동성(liquidity)** — 큰 매도 주문이 들어와서 가격이 일시적으로 하락 → 다음 달 원래 가격으로 복귀
2. **시장 미시구조(microstructure)** — 매수-매도 호가 사이의 바운스(bid-ask bounce). 가격이 매수가와 매도가 사이를 왔다 갔다 하면서 가짜 반전이 나타남

이 1개월 반전은 모멘텀과 **반대 방향**이므로, 포함하면 모멘텀 시그널에 노이즈가 섞인다. 빼면 더 깨끗한 모멘텀 측정.

인용된 논문들:

| 논문 | 기여 |
|------|------|
| **Jegadeesh (1990)** | 단기(1개월) 반전 현상 최초 발견 |
| **Lo & MacKinlay (1990)** | 주가의 단기 시계열 패턴 분석 |
| **Boudoukh, Richardson, Whitelaw (1994)** | 산업별 단기 반전 |
| **Asness (1994)** | 1개월 반전과 모멘텀의 관계 |

---

#### 각주 8

> <sup>8</sup> "Novy-Marx (2012) shows that the past 7- to 12-month return is a better momentum predictor in U.S. stocks than the past 2- to 6-month return, though the past 2- to 6-month return is still a"

(각주 이어짐)

> "positive predictor. We use the more standard momentum measure based on the past 2- to 12-month return for several reasons. First, as Novy-Marx (2012) shows, the benefit of using returns from the past 7- to 12-months as opposed to the entire 2- to 12-month past return is negligible in U.S. stocks. Second, Goyal and Wahal (2012) examine the power of past 7- to 12-month versus past 2- to 6-month returns across 36 countries and find that there is no significant difference between these past return predictors in 35 out of 36 countries—the exception being the United States. Third, *MOM2–12* is the established momentum signal that has worked well out of sample over time and across geography. While we believe using *MOM2–12* is the most prudent and reasonable measure to use for these reasons, using other momentum signals, such as *MOM7–12*, should not alter any of our conclusions."

##### 뜯기

이 각주는 **"왜 MOM7-12가 아니라 MOM2-12를 쓰는가?"**에 대한 상세 방어다.

**Novy-Marx (2012)**는 미국 주식에서 모멘텀의 예측력이 주로 **7~12개월 전** 수익률에서 온다고 주장했다. 2~6개월 전 수익률(중간 모멘텀)은 상대적으로 약하다는 것이다.

이 도전에 대해 저자들이 MOM2-12를 고수하는 세 가지 이유:

1. **미국에서의 차이는 무시할 수준** — Novy-Marx 본인도 인정하듯, MOM7-12와 MOM2-12의 차이가 미국에서조차 작다.

2. **글로벌로 보면 차이 없음** — **Goyal & Wahal (2012)**이 36개국을 조사한 결과, 35개국에서 MOM7-12와 MOM2-6 사이에 유의한 차이가 없었다. 유일한 예외가 미국. 즉 Novy-Marx의 발견은 **미국 특수 현상**일 수 있다.

3. **MOM2-12는 확립된 표준** — "out of sample over time and across geography"에서 잘 작동해온 검증된 시그널. 학술적 표준을 바꿀 만큼의 증거가 아직 없다.

마지막 문장: **"MOM7-12를 사용해도 결론은 바뀌지 않을 것"** — 강건성에 대한 자신감.

---

### 비주식 자산의 모멘텀 측정

> "For all other asset classes, we attempt to define similar value and momentum measures. Momentum is straightforward since we can use the same measure for all asset classes, namely, the return over the past 12 months skipping the most recent month."

#### 뜯기

모멘텀은 간단하다: **모든 자산군에서 동일하게 MOM2-12 사용.** 주식이든 원자재든 통화든, "과거 12개월 수익률에서 최근 1개월을 빼는 것"은 똑같이 적용 가능하다. 수익률은 어떤 자산에든 존재하기 때문.

> "While excluding the most recent month of returns is not necessary for some of the other asset classes we consider because they suffer less from liquidity issues (e.g., equity index futures and currencies), we do so to maintain uniformity across asset classes."

#### 뜯기

비주식 자산(선물, 통화)은 유동성이 높아서 **1개월 반전 문제가 적다**. 따라서 최근 1개월을 빼지 않아도 된다. 하지만 빼는 이유? **균일성(uniformity)**. 자산군마다 다른 규칙을 적용하면 비교가 어렵다.

> "Momentum returns for these asset classes are in fact stronger when we don't skip the most recent month, hence our results are conservative."

#### 뜯기

최근 1개월을 빼면 **모멘텀 수익이 더 낮아진다** (비주식에서). 즉 빼지 않았으면 더 좋은 성과가 나왔을 것이다. → **보수적(conservative)** 접근. 또다시 같은 패턴: 저자들은 "우리가 과장하고 있지 않다"는 메시지를 반복적으로 보낸다.

---

### 비주식 자산의 가치 측정

> "For measures of value, attaining uniformity is more difficult because not all asset classes have a measure of book value."

#### 뜯기

여기가 어려운 부분이다. 모멘텀은 "과거 수익률"이면 되지만, 가치는 **"무언가의 내재 가치"를 측정**해야 한다. 원자재에 "장부가치"는 없다. 옥수수의 BE/ME는 무엇인가? 의미가 없다.

> "For these assets, we try to use simple and consistent measures of value."

#### 뜯기

핵심 원칙 재확인: **단순하고 일관된** 측정치.

---

#### 국가지수의 가치 측정

> "For country indices, we use the previous month's *BE/ME* ratio for the MSCI index of the country."

##### 뜯기

국가지수의 가치 = 해당 국가 MSCI 지수의 **BE/ME 비율**. MSCI가 각 국가 지수에 포함된 기업들의 장부가치와 시장가치를 합산해서 제공한다. 직전 월의 값을 사용.

이것은 개별 주식의 BE/ME와 원리가 같지만, **나라 전체**에 적용한 것이다. "이 나라의 주식시장 전체가 싼가, 비싼가?"를 측정.

---

#### 원자재의 가치 측정

> "For commodities, we define value as the log of the spot price 5 years ago (actually, the average spot price from 4.5 to 5.5 years ago), divided by the most recent spot price, which is essentially the negative of the spot return over the last 5 years."

##### 뜯기

원자재 가치 측정치:

$$\text{Value}_{\text{commodity}} = \log\left(\frac{\text{4.5\textasciitilde5.5년 전 평균 현물가격}}{\text{최근 현물가격}}\right)$$

이것은 본질적으로 **"지난 5년간 현물가격 수익률의 음수(negative)"**이다.

왜? 과거 5년간 가격이 **크게 올랐으면** → 분모(최근 가격)가 분자(5년 전 가격)보다 크다 → 로그 값이 음수 → **가치가 낮다** (= 비싸다)

과거 5년간 가격이 **크게 떨어졌으면** → 분자가 분모보다 크다 → 로그 값이 양수 → **가치가 높다** (= 싸다)

직관: **"5년 전보다 많이 싸진 것이 저평가되었다"**는 가정. 이것은 **장기 평균 회귀(long-term mean reversion)** 현상에 기반한다.

💡 **왜 정확히 5년 전이 아니라 "4.5~5.5년 전 평균"인가?** 단일 시점의 가격은 노이즈가 클 수 있다. 1년 구간의 평균을 취함으로써 "5년 전 가격"의 추정을 안정화한다.

---

#### 통화의 가치 측정

> "Similarly, for currencies, our value measure is the negative of the 5-year return on the exchange rate, measured as the log of the average spot exchange rate from 4.5 to 5.5 years ago divided by the spot exchange rate today minus the log difference in the change in CPI in the foreign country relative to the U.S. over the same period."

##### 뜯기

통화 가치 측정은 원자재보다 한 단계 더 복잡하다:

$$\text{Value}_{\text{currency}} = -\left[\log\left(\frac{e_t}{e_{t-5}}\right) - \log\left(\frac{\text{CPI}_{\text{foreign},t}/\text{CPI}_{\text{foreign},t-5}}{\text{CPI}_{\text{US},t}/\text{CPI}_{\text{US},t-5}}\right)\right]$$

여기서 $e$는 환율(달러/외국통화).

말로 풀면:

1. 지난 5년간의 **명목 환율 변화**를 계산 (외국 통화가 달러 대비 얼마나 올랐나/떨어졌나)
2. 같은 기간의 **물가 변화 차이**를 뺀다 (인플레이션이 높은 나라의 통화는 자연히 약세)
3. 결과에 **음수(negative)**를 취한다

> "The currency value measure is therefore the 5-year change in purchasing power parity."

##### 뜯기

이것은 **구매력 평가(Purchasing Power Parity, PPP)의 5년 변화**와 같다.

💡 **PPP란?** "같은 물건은 어디서나 같은 가격이어야 한다"는 경제학 원리. 빅맥이 미국에서 $5이고 일본에서 500엔이면, 환율은 $1 = 100엔이어야 한다. 현실의 환율이 PPP에서 벗어나면, 장기적으로 돌아오는 경향이 있다.

이 측정치의 직관: **통화가 PPP 수준에 비해 5년 동안 크게 약세를 보였으면 → "싸다" → 앞으로 강세로 돌아올 것이다.**

---

#### 채권의 가치 측정

> "For bonds, we use the 5-year change in the yields of 10-year bonds as our value measure, which is similar to the negative of the past 5-year return."

##### 뜯기

채권 가치 = **10년 국채 금리의 5년 변화**

$$\text{Value}_{\text{bond}} = y_{10,t} - y_{10,t-5}$$

여기서 $y_{10,t}$는 현재 10년 국채 금리, $y_{10,t-5}$는 5년 전 10년 국채 금리.

왜 이것이 가치 측정치인가?

- 채권 가격과 금리는 **반대로** 움직인다 (금리가 오르면 채권 가격이 떨어진다)
- 5년간 금리가 크게 **올랐으면** → 채권 가격이 크게 **떨어졌다** → 채권이 "싸다"
- 금리 상승 = 과거 5년 수익률의 음수 ≈ 가치 시그널

이것은 원자재의 "5년 수익률의 음수"와 같은 논리다. 장기적으로 **많이 떨어진 것이 싸다**.

---

#### 왜 5년인가

> "These long-term past return measures of value are motivated by DeBondt and Thaler (1985), who use similar measures for individual stocks to identify 'cheap' and 'expensive' firms."

##### 뜯기

- **DeBondt & Thaler (1985)** — 행동재무학의 초석 논문. 과거 3~5년 동안 많이 떨어진 주식이 이후 수익이 좋다는 것을 발견 ("장기 반전" 효과). 이것이 **과잉반응 가설**의 시작: 투자자가 나쁜 뉴스에 과잉반응해서 가격을 너무 떨어뜨리고, 시간이 지나면 원래 가치로 돌아온다.

> "Fama and French (1996) show that the negative of the past 5-year return generates portfolios that are highly correlated with portfolios formed on *BE/ME*, and Gerakos and Linnainmaa (2012) document a direct link between past returns and *BE/ME* ratios."

##### 뜯기

두 논문이 **"5년 과거 수익률 ≈ BE/ME"**임을 입증:

- **Fama & French (1996)** — 5년 수익률의 음수로 포트폴리오를 만들면 BE/ME 포트폴리오와 **매우 높은 상관**. 즉 "과거에 많이 떨어진 주식" ≈ "BE/ME가 높은(싼) 주식".
- **Gerakos & Linnainmaa (2012)** — 과거 수익률과 BE/ME 사이의 **직접적 메커니즘**: 주가가 떨어지면 → 시장가치(분모)가 줄어든다 → BE/ME가 올라간다 (장부가치는 잘 안 변하니까).

---

#### 이론적 연결

> "Theory also suggests a link between long-term returns and book-to-market value measures (e.g., Daniel, Hirshleifer, and Subrahmanyam (1998), Barberis, Shleifer, and Vishny (1998), Hong and Stein (1999), and Vayanos and Wooley (2012))."

##### 뜯기

이론적으로도 장기 수익률과 BE/ME가 연결되어야 한다:

| 논문 | 이론 |
|------|------|
| **Daniel, Hirshleifer, Subrahmanyam (1998)** | **DHS 모형**: 투자자의 과잉자신감(overconfidence)과 자기귀인편향(self-attribution bias)이 모멘텀과 장기 반전을 모두 설명 |
| **Barberis, Shleifer, Vishny (1998)** | **BSV 모형**: 대표성 편향(representativeness)과 보수주의(conservatism)로 과잉/과소반응 설명 |
| **Hong & Stein (1999)** | **HS 모형**: 정보 확산의 느림(뉴스 워처)과 추세 추종(모멘텀 트레이더)이 단기 모멘텀과 장기 반전을 만듦 |
| **Vayanos & Wooley (2012)** | 위임 투자(delegated management)와 자금 흐름으로 가치/모멘텀 설명 |

핵심: **모멘텀(단기 지속)과 장기 반전은 같은 행동 편향의 양면**이다. 좋은 뉴스에 과잉반응 → 가격 계속 오름(모멘텀) → 결국 너무 올라감 → 되돌아옴(반전/가치).

---

#### 각주 9

> <sup>9</sup> "An Internet Appendix may be found in the online version of this article."

##### 뜯기

**Internet Appendix** = 논문 본문에 싣지 못한 추가 분석. JF 같은 탑 저널은 본문 길이 제한이 엄격하므로, 부차적이지만 중요한 분석은 온라인 부록에 담는다. 여기에는 **5년 수익률 반전과 BE/ME의 상관** 등 상세 분석이 포함되어 있다.

---

#### 5년 수익률 반전과 BE/ME의 상관

> "In the Internet Appendix accompanying this paper, we show that individual stock portfolios formed from the negative of past 5-year returns are highly correlated with those formed on *BE/ME* ratios in our sample."

##### 뜯기

Internet Appendix의 핵심 결과 미리보기. "5년 과거 수익률의 음수"로 정렬한 포트폴리오와 "BE/ME"로 정렬한 포트폴리오가 **거의 같은 종목들로 구성된다**.

> "For example, among U.S. stocks the correlation between returns to a value factor formed from the negative of the past 5-year return and the returns formed from *BE/ME* sorts is 0.83."

##### 뜯기

미국 주식에서 상관: **0.83**. 상관 0.83은 매우 높다. 1이 완벽한 일치이고, 0.83이면 두 팩터가 **거의 같은 것**을 포착하고 있다.

> "In the United Kingdom, Europe, and Japan the correlation between portfolio returns formed on negative past 5-year returns and *BE/ME* ratios is similarly high."

##### 뜯기

UK, Europe, Japan에서도 마찬가지로 높은 상관.

> "Globally, a value factor averaged across all four stock markets estimated from negative past 5-year return sorts has a correlation of 0.86 with a value factor formed from *BE/ME* sorts."

##### 뜯기

4개 시장을 합산한 글로벌 상관: **0.86**. 미국 단독(0.83)보다 더 높다. 이것은 **"5년 과거 수익률의 음수"가 비주식 자산에서 BE/ME의 합리적 대리변수**임을 정당화한다.

> "Hence, using past 5-year returns to measure value seems reasonable."

##### 뜯기

결론: **5년 수익률을 써도 된다.** 이것으로 원자재, 통화, 채권에서 BE/ME가 없어도 가치를 측정할 수 있는 근거가 마련되었다.

---

## C. Value and Momentum Portfolios: 48 New Test Assets (48개 새로운 테스트 자산)

> "Using the measures above, we construct a set of value and momentum portfolios within each market and asset class by ranking securities within each asset class by value or momentum and sorting them into three equal groups."

### 뜯기

포트폴리오 구성 방법:

1. 각 자산군 내에서 모든 자산을 **가치 시그널** 크기순으로 정렬
2. **3등분**: 상위 1/3(높은 가치 = 싼 것) / 중간 1/3 / 하위 1/3(낮은 가치 = 비싼 것)
3. 모멘텀에 대해서도 동일하게 3등분

> "We then form three portfolios—high, middle, and low—from these groups,"

#### 뜯기

- **High** = P3 = 시그널이 높은 그룹 (가치 전략에서는 "가장 싼 1/3", 모멘텀 전략에서는 "가장 많이 오른 1/3")
- **Middle** = P2 = 중간
- **Low** = P1 = 시그널이 낮은 그룹 (가치에서는 "가장 비싼 1/3", 모멘텀에서는 "가장 많이 떨어진 1/3")

---

#### 포트폴리오 가중 방식

> "where for individual stocks we value weight the returns in the portfolios by their beginning-of-month market capitalization, and for the nonstock asset classes we equal weight securities."

##### 뜯기

두 가지 가중 방식:

| 자산군 | 가중 방식 | 이유 |
|--------|----------|------|
| **주식** | 시가총액 가중 (value-weighted) | 대형주의 영향을 실제 시장 비중에 맞춤. 소형주가 결과를 지배하는 것 방지 |
| **비주식** | 동일 가중 (equal-weighted) | 국가지수 18개, 통화 10개 등 종목 수가 적으므로 시가총액 가중의 의미가 적음 |

💡 **시가총액 가중 vs 동일 가중**: 시총 가중은 큰 회사에 더 많은 비중을 주고, 동일 가중은 모든 종목에 같은 비중. 시총 가중이 실제 거래 가능한(implementable) 전략에 더 가깝다.

> "Given that our sample of stocks focuses exclusively on very large and liquid securities in each market, typically the largest quintile of securities, further value weighting the securities within this universe creates an extremely large and liquid set of portfolios that should yield very conservative results compared to typical portfolios used in the literature."

##### 뜯기

이미 상위 90% 시총 필터로 대형주만 남겼는데, 그 안에서 다시 시총 가중을 하면 → **초대형주가 지배하는 포트폴리오**. 이것은 기존 문헌의 포트폴리오보다 훨씬 **보수적**이다. 기존 연구 대부분은 소형주를 포함하거나 동일 가중을 사용해서, 소형주의 큰 수익률이 결과를 부풀린다.

---

#### 각주 10

> <sup>10</sup> "Weighting the nonstock asset classes by their ex ante volatility gives similar results. In addition, rebalancing back to equal weights annually rather than monthly produces similar results."

##### 뜯기

두 가지 강건성 체크:

1. **변동성 역수 가중(inverse volatility weighting)** — 변동성이 큰 자산에 적은 비중, 작은 자산에 큰 비중. 이렇게 해도 결과 비슷 → 가중 방식에 민감하지 않다.

2. **연간 리밸런싱 vs 월간 리밸런싱** — 매월 비중을 재조정하는 대신 매년 한 번만 해도 결과 비슷 → 빈번한 거래에 의존하는 효과가 아니다.

---

#### 왜 3분위인가

> "Thus, we generate three portfolios—low, middle, and high—for each of the two characteristics—value and momentum—in each of the eight asset classes, producing $3 \times 2 \times 8 = 48$ test portfolios."

##### 뜯기

계산:
- **3** 분위(low, middle, high)
- **2** 특성(value, momentum)
- **8** 자산군(US 주식, UK 주식, 유럽 주식, 일본 주식, 국가지수, 통화, 채권, 원자재)
- = **48개** 테스트 포트폴리오

왜 **3분위(tercile)**이고 5분위(quintile)나 10분위(decile)가 아닌가?

주식 연구에서는 보통 5분위나 10분위를 사용한다. 하지만 비주식 자산은 **종목 수가 적다**: 통화 10개, 국채 10개, 국가지수 18개. 10개를 10분위로 나누면 각 그룹에 1개씩밖에 안 들어간다! 3분위면 3~6개씩 — 그래도 적지만 최소한의 분산은 확보.

이 48개 포트폴리오가 이 논문의 **테스트 자산(test assets)**이 된다. Section IV의 3팩터 모형이 이 48개 포트폴리오의 수익률 변동을 얼마나 설명하는지를 검증한다.

---

## D. Value and Momentum Factors (가치와 모멘텀 팩터)

> "We also construct value and momentum factors for each asset class, which are zero-cost long-short portfolios that use the entire cross section of securities within an asset class."

### 뜯기

48개 테스트 포트폴리오와 별개로, **팩터(factor)**도 구성한다. 팩터는 **제로비용 롱숏 포트폴리오(zero-cost long-short portfolio)**: 싼 것을 매수(long)하고 비싼 것을 매도(short)해서 초기 투자금이 0인 포트폴리오.

💡 **왜 "zero-cost"인가?** 1달러어치를 매수하고 동시에 1달러어치를 매도하면 순투자금은 0이다. 돈이 필요 없다(이론적으로). 이렇게 하면 수익률이 **시장 전체의 움직임과 무관**해진다 — 순수하게 가치(또는 모멘텀) 시그널의 수익만 측정.

핵심 차이: **48개 테스트 포트폴리오 vs 팩터**

| | 48개 포트폴리오 | 팩터 |
|---|---------------|------|
| 구성 | 3분위 정렬 | 시그널에 비례한 가중 |
| 자산 분류 | 이산적 (상/중/하) | 연속적 (시그널에 선형 비례) |
| 롱숏 | P3 - P1로 스프레드 계산 가능 | 구조적으로 롱숏 |
| 용도 | 수익률 패턴 관찰 | 가격결정 모형의 팩터 |

---

### 수식 (1): 포트폴리오 가중치

> "For any security $i = 1, \ldots, N$ at time $t$ with signal $S_{it}$ (value or momentum), we weight securities in proportion to their cross-sectional rank based on the signal minus the cross-sectional average rank of that signal."

#### 뜯기

먼저 말로:

**"각 종목의 가중치 = (그 종목의 시그널 순위) - (전체 평균 순위)"**

시그널이 높은 종목은 양수 가중치(매수), 낮은 종목은 음수 가중치(매도). 가중치의 합은 0 (롱숏).

> "Simply using ranks of the signals as portfolio weights helps mitigate the influence of outliers, but portfolios constructed using the raw signals are similar and generate slightly better performance."

#### 뜯기

왜 **순위(rank)**를 쓰는가?

원래 시그널(BE/ME 값 자체)을 그대로 가중치로 쓸 수도 있다. 하지만 이상치(outlier)가 문제다. 예: 어떤 회사의 BE/ME가 50이면(보통 1~3 범위), 그 종목에 극단적인 비중이 가게 된다.

순위를 쓰면: BE/ME가 1이든 50이든, 순위에서 1칸 차이일 뿐이다. **이상치의 영향을 완화**.

흥미로운 고백: 원래 시그널을 쓰면 성과가 **약간 더 좋다**. 하지만 이상치 리스크가 있으므로 순위를 선택. 또다시 **보수적** 접근.

> "Specifically, the weight on security $i$ at time $t$ is"

> $$w_{it}^S = c_t(\text{rank}(S_{it}) - \Sigma_i \text{rank}(S_{it})/N), \tag{1}$$

#### 수식 해체

$$w_{it}^S = c_t\left(\text{rank}(S_{it}) - \frac{\sum_i \text{rank}(S_{it})}{N}\right)$$

**기호 해설**:

| 기호 | 의미 |
|------|------|
| $w_{it}^S$ | 시점 $t$에 종목 $i$에 부여하는 가중치. 위첨자 $S$는 시그널 종류(VALUE 또는 MOM) |
| $c_t$ | 시점 $t$의 스케일링 상수. 전체 포트폴리오를 "1달러 롱 + 1달러 숏"으로 맞추는 역할 |
| $\text{rank}(S_{it})$ | 종목 $i$의 시그널 $S$의 횡단면 순위. 시그널이 가장 낮으면 1, 가장 높으면 $N$ |
| $\sum_i \text{rank}(S_{it})/N$ | 모든 종목 순위의 평균 = $(N+1)/2$ |
| $N$ | 해당 자산군의 총 종목 수 |

**숫자 예시** — 5개 종목으로:

| 종목 | BE/ME | rank | rank - 평균(3) | 정규화 후 가중치 |
|------|-------|------|-------------|-------------|
| A | 0.5 | 1 | -2 | -0.20 (숏) |
| B | 0.8 | 2 | -1 | -0.10 (숏) |
| C | 1.2 | 3 | 0 | 0.00 (중립) |
| D | 1.8 | 4 | +1 | +0.10 (롱) |
| E | 3.0 | 5 | +2 | +0.20 (롱) |

순위 평균 = (1+2+3+4+5)/5 = 3. 가중치의 합 = (-2)+(-1)+0+1+2 = **0** (제로비용).

$c_t$가 가중치를 스케일링해서 "롱 쪽 합 = 1달러, 숏 쪽 합 = -1달러"로 만든다. 이 예시에서 롱 쪽 합은 3, 숏 쪽 합은 -3이므로 $c_t = 1/3$.

---

> "where the weights across all stocks sum to zero, representing a dollar-neutral long-short portfolio. We include a scaling factor $c_t$ such that the overall portfolio is scaled to one dollar long and one dollar short."

#### 뜯기

두 가지 속성을 확인:

1. **달러 중립(dollar-neutral)**: $\sum_i w_{it}^S = 0$. 롱과 숏이 정확히 상쇄.
2. **$c_t$의 역할**: 총 롱 포지션 = 1달러, 총 숏 포지션 = 1달러. 즉 "1달러 투자"로 정규화. 서로 다른 시점, 서로 다른 자산군의 수익률을 **비교 가능**하게 만든다.

---

### 수식 (2): 팩터 수익률

> "The return on the portfolio is then"

> $$r_t^S = \Sigma_i w_{it}^S r_{it}. \quad \text{where } S \in \{\text{value, momentum}\}. \tag{2}$$

#### 수식 해체

$$r_t^S = \sum_{i=1}^{N} w_{it}^S \cdot r_{it}$$

말로: **"팩터의 수익률 = 각 종목의 가중치 × 각 종목의 수익률, 전부 합산"**

| 기호 | 의미 |
|------|------|
| $r_t^S$ | 시점 $t$에서 시그널 $S$ 팩터의 수익률 |
| $w_{it}^S$ | 수식 (1)에서 계산한 종목 $i$의 가중치 |
| $r_{it}$ | 종목 $i$의 시점 $t$ 수익률 |
| $S$ | VALUE 또는 MOM |

위의 5종목 예시를 이어가면:

| 종목 | 가중치 $w$ | 이번 달 수익률 $r$ | $w \times r$ |
|------|----------|---------------|-------------|
| A (숏) | -0.20 | +5% | -1.0% |
| B (숏) | -0.10 | +3% | -0.3% |
| C | 0.00 | +2% | 0.0% |
| D (롱) | +0.10 | -1% | -0.1% |
| E (롱) | +0.20 | +8% | +1.6% |
| | | **팩터 수익률** | **+0.2%** |

이 예시에서 가치 팩터가 이번 달 +0.2%를 벌었다. "싼 주식(D, E)의 성과 - 비싼 주식(A, B)의 성과" = 순수한 **가치 프리미엄**.

---

### 수식 (3): 50/50 결합 (COMBO)

> "We also construct a 50/50 equal combination (*COMBO*) factor of value and momentum, whose returns are"

> $$r_t^{COMBO} = 0.5 r_t^{VALUE} + 0.5 r_t^{MOM}. \tag{3}$$

#### 수식 해체

$$r_t^{COMBO} = 0.5 \cdot r_t^{VALUE} + 0.5 \cdot r_t^{MOM}$$

말로: **"COMBO 수익률 = 가치 팩터 수익률의 절반 + 모멘텀 팩터 수익률의 절반"**

왜 50/50? 가장 **단순한** 결합. 최적 비율을 찾으면 데이터 스누핑. 사전 지식 없이 "반반"으로 가는 것이 **가장 보수적**이다.

이 COMBO가 왜 강력한가? 초록에서 말했듯 가치와 모멘텀은 **음의 상관**이다. 하나가 잃을 때 다른 하나가 번다. 50/50 결합의 변동성은 개별보다 **크게 줄어들고**, 수익은 양쪽의 평균이므로 여전히 양수. 결과: **샤프 비율이 급상승**.

---

### 시그널 가중 팩터 vs P3-P1 스프레드

> "These zero-cost signal-weighted portfolios are another way to examine the efficacy of value and momentum across markets and are used as factors in our pricing model."

#### 뜯기

시그널 가중 팩터(수식 1~2)와 단순 스프레드(P3 - P1) 두 가지 방법이 있다. 둘 다 가치/모멘텀의 수익성을 측정하지만, 특성이 다르다.

> "Although these factors are not value weighted, the set of securities used to generate them are extremely large and liquid."

#### 뜯기

주의: 시그널 가중 팩터는 **시가총액 가중이 아니다**. 시그널의 순위에 비례한 가중. 하지만 유니버스 자체가 상위 90% 시총의 대형주이므로 유동성 문제는 없다.

> "As we will show, the signal-weighted factor portfolios outperform simple portfolio sort spreads because security weights are a positive (linear) function of the signal, as opposed to the coarseness of only classifying securities into three groups."

#### 뜯기

시그널 가중이 3분위 스프레드보다 **성과가 더 좋다**. 이유:

- 3분위: "상위 1/3" 안에서 1등이든 꼴찌든 **같은 가중치**. 정보 낭비.
- 시그널 가중: 시그널이 강할수록 더 큰 가중치. 정보를 **선형적으로(linearly) 활용**. 시그널이 강한 종목에 더 집중.

비유: 시험 점수로 반을 나눌 때, "상중하 3반" vs "점수에 비례해 자원 배분" — 후자가 더 효율적.

> "In addition, the factors are better diversified since more securities in the cross section are given nonzero weight and the weights are less extreme."

#### 뜯기

분산 투자 측면에서도 시그널 가중이 유리하다:

- 3분위 스프레드: 중간 1/3은 가중치 0 (포트폴리오에 안 들어감)
- 시그널 가중: 극단값(순위 = 평균)을 제외한 **거의 모든 종목이 비중을 가짐**

모든 종목이 참여하므로 분산이 더 잘 되고, 극단적인 가중치도 없다.

---

## 이 섹션에서 배운 것

Section I 전체를 한 눈에 정리하면:

| 자산군 | 데이터 소스 | 기간 | 종목 수 | 가치 측정 | 모멘텀 측정 |
|--------|-----------|------|---------|---------|-----------|
| **US 주식** | CRSP + Compustat | 1972.01~2011.07 | 724 (354) | BE/ME | MOM2-12 |
| **UK 주식** | Datastream + Worldscope | 1972.01~2011.07 | 147 (76) | BE/ME | MOM2-12 |
| **유럽 주식** | Datastream + Worldscope | 1974.01~2011.07 | 290 (96) | BE/ME | MOM2-12 |
| **일본 주식** | Datastream + Worldscope | 1974.01~2011.07 | 471 (148) | BE/ME | MOM2-12 |
| **국가지수** | MSCI + Bloomberg | 1978.01~2011.07 | 18 (8) | MSCI BE/ME | MOM2-12 |
| **통화** | Datastream + MSCI + Libor | 1979.01~2011.07 | 10 (7) | 5년 실질환율 변화(PPP) | MOM2-12 |
| **국채** | Bloomberg + Morgan Markets | 1982.01~2011.07 | 10 (5) | 10년 금리의 5년 변화 | MOM2-12 |
| **원자재** | 각 거래소 | 1972.01~2011.07 | 27 (10) | 5년 현물가격 변화의 음수 | MOM2-12 |

**설계 철학 3가지**:
1. **단순하고 균일한 측정치** — 데이터 스누핑 방지
2. **대형 유동주 집중** — 실행 가능성, 보수적 추정
3. **"Everywhere" 일관성** — 모든 자산군에 가능한 한 같은 방법

**포트폴리오 2종**:
- **48개 테스트 자산**: 3분위 × 2특성 × 8자산군. 수익률 패턴 관찰용.
- **시그널 가중 팩터**: 수식 (1)~(3). 가격결정 모형의 팩터, COMBO까지.

---

## 여기서 멈추고 생각하기

데이터와 방법론을 다 읽었다. 결과를 보기 전에 스스로 예측해보자.

### 🤔 추론 연습

1. **시총 상위 90%만 사용** — 소형주에서 가치/모멘텀 효과가 더 크다고 알려져 있다(각주 5). 그렇다면 이 논문의 결과는 **하한(lower bound)**이다. "대형주에서도 이만큼 되면, 소형주 포함하면 더 클 것" — 이건 논문의 주장을 **강화**하는가 **약화**하는가?

2. **왜 가치 측정이 자산군마다 다른가?** — 주식은 BE/ME, 통화는 PPP, 원자재는 5년 가격변화. "균일성"을 추구한다면서 왜 다르게 하는가? → 진짜 균일한 건 **모멘텀**(모든 곳에서 MOM2-12). 가치는 자산의 본질이 달라서 균일화가 불가능. 이건 논문의 약점인가 강점인가?

3. **48개 테스트 자산의 설계** — 3분위 × 2 × 8 = 48. 만약 5분위로 했으면 80개, 10분위로 했으면 160개가 된다. 테스트 자산이 많을수록 좋은가? → 반드시 그렇지 않다. 비주식은 종목이 10개밖에 안 되므로 10분위가 불가능. 3분위는 "모든 자산군에 적용 가능한 최대 공약수".

### ⚡ 설계 변형 아이디어

이 논문의 설계를 **바꾸면** 어떤 결과가 나올까?

- MOM2-12 대신 **MOM7-12** (최근 7~12개월만)를 쓰면? → Novy-Marx (2012)가 이게 더 낫다고 주장
- BE/ME 대신 **earnings yield** (이익수익률)를 쓰면? → 더 강한 가치 신호일 수 있음
- **신흥국**을 포함하면? → 데이터 품질 문제가 있지만, "Everywhere"가 더 강해질 것
- **2011년 이후**는? → 이 논문의 가장 큰 한계. 2011~2024년에도 작동하는가?

> **다음**: [dissect-03 수익률과 공행성](dissect-03-returns.md) — 이 48개 포트폴리오와 팩터의 실제 성과가 Table I에 펼쳐진다. "어디서나 돈을 버는가?"에 대한 답.
