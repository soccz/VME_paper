# 논문 해체: Introduction (p.929~933)

> 초록이 논문의 "예고편"이었다면, Introduction은 "1화"다. 왜 이 연구를 하는지, 기존 연구의 어떤 구멍을 메우는지, 무엇을 발견했는지, 어떤 이론적 의미가 있는지 — 논문의 전체 뼈대를 5페이지에 걸쳐 풀어놓는다. 한 문장도 빠짐없이 뜯는다.

---

## 첫 문단: 이 논문은 무엇에 대한 것인가 (p.929)

### 문장 1

> "Two of the most studied capital market phenomena are the relation between an asset's return and the ratio of its 'long-run' (or book) value relative to its current market value, termed the 'value' effect, and the relation between an asset's return and its recent relative performance history, termed the 'momentum' effect."

**뜯기**: 논문의 첫 문장. "자본시장에서 가장 많이 연구된 현상 두 가지"라고 시작한다. 첫 문장에서 "가장"이라는 표현을 쓴다는 건, 이 주제가 금융학의 중심부에 있다는 선언이다.

**첫 번째 현상: 가치 효과(Value Effect)**

자산의 수익률과, "장기적(long-run) 또는 장부상(book) 가치"를 "현재 시장가치(current market value)"로 나눈 비율 사이의 관계.

쉽게 말하면:
- **장부가치(Book Value)** = 회사가 가진 실체적 자산(공장, 현금, 특허 등)을 장부에 기록한 금액. "해체해서 팔면 이 정도"라는 최소한의 가치.
- **시장가치(Market Value)** = 주식시장에서 투자자들이 매기는 가격. 주가 × 발행주식수.
- 이 비율(장부/시장, BE/ME)이 **높은** 주식 = 시장이 싸게 평가한 주식 = **가치주(Value Stock)**
- 이 비율이 **낮은** 주식 = 시장이 비싸게 평가한 주식 = **성장주(Growth Stock)**

**가치 효과** = "이 비율이 높은(싼) 자산이, 낮은(비싼) 자산보다 수익률이 높더라" 라는 관찰. 싼 걸 사고 비싼 걸 팔면 돈을 번다.

**두 번째 현상: 모멘텀 효과(Momentum Effect)**

자산의 수익률과, "최근의 상대적 성과 이력(recent relative performance history)" 사이의 관계.

쉽게 말하면:
- 최근 많이 올랐던 자산이 **계속 오르고**, 최근 많이 떨어졌던 자산이 **계속 떨어지는** 현상.
- 과거 12개월 수익률(최근 1개월 제외)로 측정한다.
- "오르는 놈은 계속 오르고, 떨어지는 놈은 계속 떨어진다" — 이것이 모멘텀.

> 📚 **더 깊이**: [ch04 가치와 모멘텀 직관](../chapters/ch04-val-mom-intuition.md) — BE/ME 비율, 모멘텀 측정(MOM2-12)의 상세한 계산법

### 문장 2

> "The returns to value and momentum strategies have become central to the market efficiency debate and the focal points of asset pricing studies, generating numerous competing theories for their existence."

**뜯기**: 가치와 모멘텀 전략의 수익률은 **시장 효율성 논쟁(market efficiency debate)**의 중심이 되었고, 자산가격결정 연구의 핵심 주제가 되어, 이것들이 왜 존재하는지를 놓고 **수많은 경쟁 이론**이 나왔다.

**시장 효율성 논쟁이란?**

"주식시장은 효율적인가?" — 금융학의 가장 큰 전쟁이다.

- **효율적 시장 가설(Efficient Market Hypothesis, EMH)**: Eugene Fama가 제안. "시장 가격에는 모든 정보가 이미 반영되어 있으므로, 시장을 체계적으로 이길 수는 없다."
- **반론**: 가치와 모멘텀 전략이 수십 년째 돈을 번다면, 시장이 정말 효율적인가?

이 질문에 대해 세 진영이 싸운다:
1. **위험 보상파(Risk-based)**: "돈을 버는 건 사실이지만, 그건 더 큰 위험을 감수한 대가다. 시장은 효율적이다."
2. **행동재무파(Behavioral)**: "아니, 투자자들이 비합리적이라서 가격이 틀리는 거다. 시장은 비효율적이다."
3. **제도적 마찰파(Institutional)**: "시장 구조(거래 비용, 차입 제약 등)가 가격을 왜곡한다."

이 논문은 **세 진영 모두에** 새로운 증거를 던진다.

> 📚 **더 깊이**: [ch03 금융학의 3대 전쟁](../chapters/ch03-theory-wars.md) — 세 진영의 논리, 핵심 논문, 논쟁의 역사

### 문장 3

> "We offer new insights into these two market anomalies by examining their returns jointly across eight diverse markets and asset classes."

**뜯기**: "우리는 이 두 시장 이상현상(market anomalies)에 대해, 8개의 다양한 시장과 자산군에 걸쳐 수익률을 **공동으로(jointly)** 검토함으로써 새로운 통찰을 제공한다."

핵심 단어 두 개:

1. **"jointly"** = 가치와 모멘텀을 **따로따로가 아니라 함께** 본다. 기존 연구 대부분은 "가치"만 연구하거나 "모멘텀"만 연구했다. 이 논문은 둘을 동시에 본다. 왜? 둘 사이의 **관계**(음의 상관)가 핵심 발견이기 때문이다.

2. **"eight diverse markets"** = 8개의 서로 다른 시장/자산군. 미국 주식 하나만이 아니라 전 세계, 전 자산을 본다. 이것이 제목의 "Everywhere".

### 문장 4

> "We find significant return premia to value and momentum in every asset class and strong comovement of their returns across asset classes, both of which challenge existing theories for their existence."

**뜯기**: 두 가지 핵심 발견을 미리 보여준다:

1. **"significant return premia... in every asset class"** = 가치와 모멘텀의 수익 프리미엄이 **모든** 자산군에서 통계적으로 유의미하다. "몇 개"가 아니라 "전부".

2. **"strong comovement of their returns across asset classes"** = 자산군 간에 가치/모멘텀 수익률이 **강하게 같이 움직인다(comovement)**. 미국 주식의 가치 전략이 잘 되는 달에, 일본 주식이나 통화의 가치 전략도 잘 된다.

그리고 이 두 발견이 "기존 이론에 도전한다(challenge existing theories)"고 선언한다. 왜 도전인지는 뒤에서 상세히 나온다.

### 문장 5

> "We provide a simple three-factor model that captures the global returns across asset classes, the Fama–French U.S. stock portfolios, and a set of hedge fund indices."

**뜯기**: 단순한 3팩터 모형(three-factor model)을 제시하는데, 이 모형이 세 가지를 동시에 설명한다:

1. **전 자산군의 글로벌 수익률** — 이 논문의 8개 자산군
2. **Fama-French 미국 주식 포트폴리오** — 기존 학계의 표준 벤치마크
3. **헤지펀드 지수들** — 실무에서 쓰이는 투자 전략의 수익률

"단순한(simple)"이라는 단어가 중요하다. 복잡한 모형은 누구나 만들 수 있다. 변수를 100개 넣으면 뭐든 설명한다. 하지만 **3개**로 이 모든 걸 설명한다? 그게 과학의 힘이다.

💡 **이 3팩터란?**
1. **MKT** — 글로벌 시장 수익률 (MSCI World Index 같은 것)
2. **VAL** — 전 자산군 가치 전략의 평균 수익률 (싼 것 매수 - 비싼 것 매도)
3. **MOM** — 전 자산군 모멘텀 전략의 평균 수익률 (올랐던 것 매수 - 떨어졌던 것 매도)

> 📚 **더 깊이**: [ch05 팩터와 회귀분석](../chapters/ch05-factors-regression.md) — 팩터 모형이 뭔지, 왜 3개인지

---

## 기존 문헌의 한계 (p.930 상단)

### 문장 6

> "The literature on market anomalies predominantly focuses on U.S. individual equities, and often examines value or momentum separately."

**뜯기**: 기존 문헌의 **첫 번째 한계**. 시장 이상현상에 대한 연구가 "주로(predominantly)" 미국 개별 주식에 집중하고, 가치 **또는** 모멘텀을 따로 연구한다.

왜 이게 문제인가?
- **미국만 보면**: "이건 미국만의 특수한 현상 아냐? 데이터 마이닝(data mining) 아냐?" 하는 반론에 취약하다.
- **따로 보면**: 가치와 모멘텀 사이의 음의 상관이라는 핵심 패턴을 놓친다.

### 문장 7

> "In the rare case in which value and momentum are studied outside of U.S. equities, they are also typically studied in isolation—separate from each other and separate from other markets."

**뜯기**: 기존 문헌의 **두 번째 한계**. 미국 밖에서 연구한 드문 경우에도, "격리(isolation)" 상태로 연구한다. "가치"만 따로, "모멘텀"만 따로. 그리고 다른 시장과도 따로.

"isolation"이라는 단어를 일부러 쓴 것이다. 과학에서 "격리"는 실험을 통제할 때 쓰는 단어인데, 여기서는 **비판**의 의미로 사용된다. "격리해서 봤기 때문에 전체 그림을 놓쳤다."

### 문장 8: 8개 시장/자산군 나열

> "We uncover unique evidence and features of value and momentum by examining them jointly across eight different markets and asset classes (individual stocks in the United States, the United Kingdom, continental Europe, and Japan; country equity index futures; government bonds; currencies; and commodity futures)."

**뜯기**: 이 논문이 보는 8개 시장/자산군을 처음으로 명시적으로 나열한다.

| # | 자산군 | 원문 | 무엇을 사고파는가 |
|---|--------|------|-----------------|
| 1 | 미국 개별주식 | individual stocks in the United States | 애플, 엑슨모빌 등 미국 상장 기업 주식 |
| 2 | 영국 개별주식 | the United Kingdom | HSBC, 유니레버 등 런던거래소 상장 주식 |
| 3 | 유럽대륙 개별주식 | continental Europe | 네슬레, LVMH 등 유럽 (영국 제외) 주식 |
| 4 | 일본 개별주식 | Japan | 토요타, 소니 등 도쿄거래소 상장 주식 |
| 5 | 국가 주가지수 선물 | country equity index futures | 18개 선진국 주가지수의 선물 계약 |
| 6 | 국채 | government bonds | 10개국 정부채권 |
| 7 | 통화 | currencies | 10개 주요 통화 |
| 8 | 원자재 선물 | commodity futures | 금, 원유, 밀 등 27개 상품 선물 |

**왜 이 8가지인가?** 이 자산군들은 **서로 완전히 다른 세계**다:
- 개별주식: 기업의 미래 수익에 베팅 → 정보 원천은 재무제표, 실적 발표
- 국채: 정부의 이자 지급 능력에 베팅 → 금리, 인플레이션이 핵심
- 통화: 국가 간 경제력 차이에 베팅 → 중앙은행 정책, 무역수지
- 원자재: 실물 공급/수요에 베팅 → 날씨, 전쟁, 재고량

이렇게 **근본적으로 다른** 시장에서 같은 패턴이 나타난다면, 그건 우연이 아니다.

---

### 각주 1: 선행 연구 총정리

> <sup>1</sup> Early evidence on U.S. equities finds that value stocks on average outperform growth stocks (Stattman (1980), Rosenberg, Reid, and Lanstein (1985), and Fama and French (1992)) and stocks with high positive momentum (high 6- to 12-month past returns) outperform stocks with low momentum (Jegadeesh and Titman (1993), Asness (1994)). Similar effects are found in other equity markets (Fama and French (1998), Rouwenhorst (1998), Liew and Vassalou (2000), Griffin, Ji, and Martin (2003), Chui, Wei, and Titman (2010)), and in country equity indices (Asness, Liew, and Stevens (1997) and Bhojraj and Swaminathan (2006)). Momentum is also found in currencies (Shleifer and Summers (1990), Kho (1996), LeBaron (1999)) and commodities (Erb and Harvey (2006), Gorton, Hayashi, and Rouwenhorst (2008)).

**뜯기**: 이 각주 하나에 **가치와 모멘텀 연구의 계보** 전체가 압축되어 있다. 논문 나열이 아니다. 각 논문이 "왜" 여기서 인용되는지가 중요하다.

#### 미국 주식에서의 가치 효과: 최초 발견들

| 논문 | 핵심 기여 |
|------|---------|
| **Stattman (1980)** | 미국 주식에서 BE/ME(장부가/시가) 비율이 높은 주식의 수익률이 높다는 것을 **최초로** 체계적으로 문서화. 당시엔 거의 주목받지 못했다. |
| **Rosenberg, Reid, and Lanstein (1985)** | 같은 결과를 더 정교한 방법으로 확인. "가치주가 성장주를 이긴다"는 증거를 미국 주식에서 실증. |
| **Fama and French (1992)** | **결정적 논문**. BE/ME가 주식 수익률의 횡단면(cross-section)을 설명하는 핵심 변수임을 보여줌. 이전까지 "수익률을 설명하는 건 시장 베타뿐"이라던 CAPM의 근간을 흔들었다. 이후 모든 가치 연구의 출발점. |

💡 **왜 이 순서인가?** 금융학의 발견은 보통 이렇게 진행된다: (1) 누군가 패턴을 발견하지만 주목받지 못함 → (2) 다른 사람이 확인 → (3) 대가(Fama)가 체계적으로 정리하면 학계가 받아들임.

#### 미국 주식에서의 모멘텀 효과: 최초 발견들

| 논문 | 핵심 기여 |
|------|---------|
| **Jegadeesh and Titman (1993)** | 모멘텀 전략(과거 승자 매수, 패자 매도)이 미국 주식에서 유의미한 수익을 낸다는 것을 **최초로** 학술적으로 문서화한 논문. "3~12개월 과거 수익률 기준" 전략. 모멘텀 연구의 모든 것이 이 논문에서 시작된다. |
| **Asness (1994)** | 바로 이 논문의 제1저자 Asness의 **박사논문**. 시카고 대학에서 Fama 지도하에 가치와 모멘텀을 함께 연구한 최초의 시도. 이 논문(2013)의 씨앗이 1994년에 심어졌다는 뜻. |

#### 해외 주식으로의 확장

| 논문 | 핵심 기여 |
|------|---------|
| **Fama and French (1998)** | 가치 효과가 미국만의 현상이 아님을 보여줌. 13개국 주식시장에서 가치 프리미엄 확인. "미국 편향(U.S. bias)" 비판에 대한 첫 반격. |
| **Rouwenhorst (1998)** | 유럽 12개국에서 모멘텀 효과 확인. 미국 밖에서도 모멘텀이 작동한다. |
| **Liew and Vassalou (2000)** | 가치와 모멘텀 수익이 미래 GDP 성장과 관련 있다는 증거. "이것은 거시경제 위험의 보상일 수 있다"는 위험 보상파의 논거에 기여. |
| **Griffin, Ji, and Martin (2003)** | 모멘텀이 글로벌 현상인지 국가별 현상인지 조사. 결론: 모멘텀은 주로 **국가 내** 현상이며, 글로벌 팩터보다 로컬 팩터가 중요. 이 논문(2013)과 다소 대비되는 결론이라 인용됨. |
| **Chui, Wei, and Titman (2010)** | 모멘텀의 크기가 나라마다 다르다는 것을 보여줌. **개인주의(individualism)**가 높은 문화에서 모멘텀이 더 강함. 행동재무학적 설명에 유리한 증거. |

#### 국가 주가지수로의 확장

| 논문 | 핵심 기여 |
|------|---------|
| **Asness, Liew, and Stevens (1997)** | 개별 주식이 아니라 **국가 지수** 수준에서도 가치와 모멘텀이 작동하는지 조사한 최초의 논문. 역시 이 논문의 제1저자 Asness가 관련. |
| **Bhojraj and Swaminathan (2006)** | 국가 간 주가 수렴(convergence)과 가치 효과의 관계. 해외 투자에서의 가치 전략. |

#### 통화에서의 모멘텀

| 논문 | 핵심 기여 |
|------|---------|
| **Shleifer and Summers (1990)** | 엄밀히 말하면 통화 모멘텀 자체를 연구한 논문은 아니고, **"노이즈 트레이더(noise trader)" 모형**을 제안한 이론 논문. 비합리적 투자자가 가격을 왜곡할 수 있다는 프레임워크를 제시. 통화 시장의 비효율성을 설명하는 이론적 기반. |
| **Kho (1996)** | 통화 시장에서 모멘텀(추세 추종) 전략의 수익성을 분석. |
| **LeBaron (1999)** | 외환 시장에서 기술적 거래 규칙(이동평균 등)이 돈을 번다는 증거. 통화 모멘텀의 변형. |

#### 원자재에서의 모멘텀

| 논문 | 핵심 기여 |
|------|---------|
| **Erb and Harvey (2006)** | 원자재 선물의 수익률 원천을 분석. 원자재에서도 모멘텀 패턴이 나타남. 원자재 투자의 학술적 기초를 놓은 논문. |
| **Gorton, Hayashi, and Rouwenhorst (2008)** | 원자재 선물 시장의 장기 데이터를 구축하고 수익률 패턴을 문서화. 재고 수준이 수익률 예측에 중요하다는 발견. |

💡 **이 각주가 말하는 것**: 가치와 모멘텀은 이미 많은 시장에서 개별적으로 연구되었다. 하지만 **아무도 이것들을 한꺼번에, 체계적으로, 서로의 관계까지** 본 적이 없다. 이 논문이 하는 것이 바로 그것이다.

---

## 핵심 질문 4가지 (p.930 중단)

> "Although some of these markets have been analyzed in isolation, our joint approach provides unique evidence on several key questions about these pervasive market phenomena."

**뜯기**: 일부 시장은 이미 **격리 상태로** 분석된 적이 있지만, "우리의 공동 접근법(joint approach)"이 이 광범위한 시장 현상들에 대해 **독자적인 증거(unique evidence)**를 제공한다.

"joint approach"가 왜 기존과 다른 증거를 주는가? 비유: 눈 하나로 보면 2D 세계, 눈 두 개로 보면 3D 세계가 된다. **깊이(depth)**가 생긴다. 이 논문은 8개의 "눈"으로 본다.

그리고 4개의 구체적 질문을 던진다:

### Q1

> "Specifically, how much variation exists in value and momentum premia across markets and asset classes?"

**뜯기**: "구체적으로, 가치와 모멘텀 프리미엄에 시장과 자산군에 따른 **변이(variation)**가 얼마나 있는가?"

쉽게 말하면: 가치 전략이 미국에서 연 5% 벌면, 일본에서도 5%인가? 통화에서는? 원자재에서는? 시장마다 **크기가 다른가, 비슷한가?** 비슷하다면 뭔가 보편적인 원인이 있다는 증거가 된다.

### Q2

> "How correlated are value and momentum returns across these diverse markets and asset classes with different geographies, structures, investor types, and securities?"

**뜯기**: "서로 다른 지리, 구조, 투자자 유형, 증권을 가진 이 다양한 시장들에 걸쳐, 가치와 모멘텀 수익률은 얼마나 **상관**되어 있는가?"

핵심: **"different geographies, structures, investor types, and securities"** — 이 네 가지를 나열한 이유가 있다. 미국 주식과 유럽 주식은 같은 종류(주식)이니까 상관이 있을 수 있다. 하지만 미국 주식과 원자재 선물은?
- 지리가 다르다 (전 세계)
- 구조가 다르다 (현물 vs 선물)
- 투자자가 다르다 (주식 펀드 vs 원자재 트레이더)
- 증권이 다르다 (주식 vs 선물)

이렇게 완전히 다른데도 상관이 있다면, 그건 **매우** 강력한 증거다.

### Q3

> "What are the economic drivers of value and momentum premia and their correlation structure?"

**뜯기**: "가치와 모멘텀 프리미엄, 그리고 이들의 상관 구조를 만드는 **경제적 동인(economic drivers)**은 무엇인가?"

Q1과 Q2는 "무엇이 일어나는가(what)"를 묻는다. Q3는 "왜 일어나는가(why)"를 묻는다. 이 논문의 답: **유동성 리스크(liquidity risk)**가 부분적 동인이다. "부분적"이라는 것이 솔직한 지점.

### Q4

> "What is a natural benchmark model for portfolios of global securities across different asset classes?"

**뜯기**: "다양한 자산군에 걸친 글로벌 증권 포트폴리오에 대한 **자연스러운 벤치마크 모형**은 무엇인가?"

"벤치마크 모형"이란? 투자 성과를 판단할 때 "이 정도는 기본이다"라는 기준. 예를 들어 "시장 평균 수익률"이 가장 기본적인 벤치마크다. 시장 평균 10% 올랐는데 내 포트폴리오가 12% 올랐다면, 진짜 실력은 2%뿐.

기존에는 미국 주식에 대한 벤치마크(Fama-French 3팩터)만 있었다. **전 자산군에 걸친** 벤치마크는 없었다. 이 논문이 그것을 제안한다 — 글로벌 3팩터.

---

## 핵심 발견 미리보기 (p.930 하단 ~ p.931 상단)

### 문장 9

> "We find consistent and ubiquitous evidence of value and momentum return premia across all the markets we study, including value and momentum in government bonds and value effects in currencies and commodities, which are all novel to the literature."

**뜯기**: 핵심 발견 첫 번째.

- **"consistent and ubiquitous"** = "일관되고 편재하는". ubiquitous는 "어디에나 있는"이라는 뜻으로, 제목의 "Everywhere"를 학술 용어로 바꾼 것.
- **"including value and momentum in government bonds"** = 국채에서도 가치와 모멘텀이 작동한다. 이건 **이 논문이 최초(novel)**로 보여주는 것.
- **"value effects in currencies and commodities"** = 통화와 원자재에서의 가치 효과도 최초.

모멘텀이 통화나 원자재에서 나타나는 건 이미 알려져 있었다(각주 1의 논문들). 하지만 **가치**가 이 시장들에서도 작동한다는 건 이 논문이 처음이다. 그리고 국채에서 가치와 모멘텀 **모두** 작동한다는 것도 처음.

**"novel to the literature"** = 학술 문헌에서 새로운 것. 논문에서 이 표현을 쓰면 "이건 우리가 처음 발견한 거다"라는 명시적 주장이다.

### 문장 10

> "Our broader set of portfolios generates much larger cross-sectional dispersion in average returns than those from U.S. stocks only, providing a richer set of asset returns that any asset pricing model should seek to explain."

**뜯기**:

- **"broader set of portfolios"** = 8개 자산군에 걸친 더 넓은 포트폴리오 세트
- **"much larger cross-sectional dispersion"** = 평균 수익률의 **횡단면 분산(cross-sectional dispersion)**이 훨씬 크다

횡단면 분산이란? 같은 시점에 여러 포트폴리오의 수익률이 얼마나 **퍼져 있는가**. 미국 주식만 보면 가치 포트폴리오와 성장 포트폴리오의 수익률 차이가 예를 들어 연 5%. 하지만 8개 자산군 전체를 보면 그 차이가 훨씬 커진다.

왜 이게 좋은가? **분산이 클수록 자산가격결정 모형을 더 엄격하게 검증할 수 있다.** 시험 문제가 다 비슷하면 누가 잘하는지 구별하기 어렵다. 문제가 다양하고 난이도 범위가 넓으면 실력 차이가 드러난다. 마찬가지로, 분산이 큰 데이터는 "이 모형이 진짜 좋은 모형인가?"를 더 정확하게 판별해준다.

### 문장 11

> "Most strikingly, we discover significant comovement in value and momentum strategies across diverse asset classes."

**뜯기**: "가장 놀라운 것은(Most strikingly)" — 논문에서 이런 표현을 쓰는 건 드물다. 학술 논문은 보통 감정을 절제한다. 이 표현은 "이건 정말 예상 못 한 발견"이라는 신호.

발견: 가치와 모멘텀 전략이 **다양한 자산군에 걸쳐** 유의미하게 **같이 움직인다(comovement)**.

### 문장 12-13

> "Value strategies are positively correlated with other value strategies across otherwise unrelated markets, and momentum strategies are positively correlated with other momentum strategies globally."

**뜯기**: 
- **가치끼리 양의 상관**: 미국 주식의 가치 전략이 좋은 달에, 일본 주식의 가치 전략도, 통화의 가치 전략도, 원자재의 가치 전략도 좋다. "otherwise unrelated markets" — 이 시장들은 다른 면에서는 전혀 관련이 없는데도 불구하고.
- **모멘텀끼리 양의 상관**: 같은 이야기. 모멘텀 전략들이 전 세계적으로 같이 움직인다.

### 문장 14

> "However, value and momentum are negatively correlated with each other within and across asset classes."

**뜯기**: 그런데 가치와 모멘텀은 서로 **음의 상관**이다.
- **"within"** = 같은 자산군 안에서. 미국 주식의 가치가 좋을 때, 미국 주식의 모멘텀은 나쁘다.
- **"across"** = 다른 자산군 사이에서. 미국 주식의 가치가 좋을 때, 통화의 모멘텀도 나쁘다.

정리하면 상관관계의 전체 그림:

```
가치(미국) ↔ 가치(일본)  = + (양의 상관)
가치(미국) ↔ 가치(통화)  = + (양의 상관)
모멘텀(미국) ↔ 모멘텀(원자재) = + (양의 상관)
가치(미국) ↔ 모멘텀(미국) = − (음의 상관)
가치(미국) ↔ 모멘텀(일본) = − (음의 상관)
```

이 패턴이 왜 기존 이론에 도전인가? 기존 이론은 대부분 **하나의 시장 안에서** 가치 또는 모멘텀을 설명한다. "전 세계 가치 전략이 같이 움직이고, 전 세계 모멘텀과는 반대로 움직인다"는 현상을 예측하는 이론이 **없다**.

---

## 글로벌 3팩터 모형 (p.930 하단 ~ p.931 상단)

### 문장 15

> "The striking comovement pattern across asset classes is one of our central findings and suggests the presence of common global factors related to value and momentum."

**뜯기**: 자산군 간의 눈에 띄는 공동움직임(comovement) 패턴이 "우리의 핵심 발견 중 하나"이며, 가치와 모멘텀에 관련된 **공통 글로벌 팩터**의 존재를 시사한다.

"시사한다(suggests)"라는 단어가 중요하다. "증명한다(proves)"가 아니다. 학술 논문에서는 상관관계(correlation)를 인과관계(causation)로 단정하지 않는다. 공동움직임이 있다 → 뭔가 공통 원인이 있을 **수 있다** → 그 원인이 뭔지 조사하겠다 — 이런 논리 흐름.

### 문장 16

> "This common risk structure implies a set of results that we investigate further."

**뜯기**: 이 공통 위험 구조(common risk structure)는 일련의 결과를 **함의(imply)**하며, 이를 추가로 조사한다. 즉, 공통 팩터가 있다면 특정한 예측이 가능해지고, 그 예측이 맞는지 검증하겠다는 것.

### 문장 17

> "For example, using a simple three-factor model consisting of a global market index, a zero-cost value strategy applied across all asset classes, and a zero-cost momentum strategy across all assets, we capture the comovement and the cross section of average returns both globally across asset classes and locally within an asset class."

**뜯기**: 3팩터 모형의 구체적 구성:

1. **글로벌 시장 지수(global market index)** — 전 세계 시장의 전반적 움직임
2. **제로코스트 가치 전략(zero-cost value strategy)** — 싼 것 매수 + 비싼 것 매도. "제로코스트"란 매수 금액과 매도 금액이 같아서 **순투자금이 0원**이라는 뜻. $100 사고 $100 팔면 자기 돈 $0으로 운영.
3. **제로코스트 모멘텀 전략(zero-cost momentum strategy)** — 올랐던 것 매수 + 떨어졌던 것 매도. 역시 제로코스트.

이 3개 팩터로 두 가지를 동시에 설명한다:
- **"globally across asset classes"** = 자산군 간의 수익률 패턴 (미국 주식 vs 통화 vs 원자재 등)
- **"locally within an asset class"** = 자산군 내의 수익률 패턴 (미국 주식 안에서 가치주 vs 성장주 등)

### 문장 18

> "We further show that the global three-factor model does a good job capturing the returns to the Fama and French U.S. stock portfolios as well as a set of hedge fund indices."

**뜯기**: 이 글로벌 3팩터 모형이 Fama-French 미국 주식 포트폴리오와 헤지펀드 지수의 수익률도 잘 설명한다.

왜 이게 중요한가?
- **Fama-French 포트폴리오**: 미국 주식 연구의 표준 벤치마크. 규모(대형/소형) × 가치(가치주/성장주) 조합의 포트폴리오. 기존 Fama-French 3팩터(미국 시장 + HML + SMB)로 설명되던 것을, **글로벌 팩터만으로도 설명 가능**하다는 것.
- **헤지펀드 지수**: 실무의 투자 전략 수익률. 이론적 모형이 실무에서도 작동하는지 확인.

### 문장 19

> "Our use of a simple three-factor model in pricing a variety of assets globally is motivated by finance research and practice becoming increasingly global and the desire to have a single model that describes returns across asset classes rather than specialized models for each market."

**뜯기**: 왜 굳이 "하나의 모형"을 추구하는가?

- 금융 연구와 실무가 점점 **글로벌화**되고 있다
- 각 시장마다 별도 모형을 만드는 대신, **하나의 모형**으로 전부 설명하고 싶다

물리학에서 중력, 전자기력, 약력, 강력을 하나의 이론으로 통합하려는 것과 같다. "통일 이론(unified theory)"에 대한 열망.

### 문장 20

> "We show that separate factors for value and momentum best explain the data, rather than a single factor, since both strategies produce positive returns on average yet are negatively correlated."

**뜯기**: 가치와 모멘텀을 **하나의 팩터로 합치면 안 되고**, **별도의 팩터로 두어야** 데이터를 가장 잘 설명한다. 이유: 둘 다 양의 수익을 내지만 **음의 상관**이기 때문이다.

왜 하나로 합치면 안 되는가? 하나의 팩터는 "이 팩터가 오르면 둘 다 오르고, 내리면 둘 다 내린다"는 구조다. 그런데 가치와 모멘텀은 반대로 움직인다. 하나의 팩터로는 이걸 잡을 수 없다.

---

### 각주 2

> <sup>2</sup> A single factor would require significant time variation in betas and/or risk premia to accommodate these facts. We remain agnostic as to whether our factors capture such dynamics or represent separate unconditional factors.

**뜯기**: 

"하나의 팩터가 이 사실들을 수용하려면, 베타(beta)와/또는 위험 프리미엄(risk premia)에 유의미한 **시간에 따른 변동(time variation)**이 있어야 할 것이다."

이게 무슨 뜻인가? 가치와 모멘텀이 하나의 공통 원인에서 나온다고 가정하자. 그러면 그 공통 팩터에 대한 가치의 민감도(베타)와 모멘텀의 민감도(베타)가 **시간에 따라 부호가 바뀌어야** 한다. 어떤 때는 같은 방향, 어떤 때는 반대 방향. 이건 기술적으로 가능하지만, 매우 복잡하고 비직관적인 모형이 된다.

"우리는 우리의 팩터가 그런 동적 변화를 포착하는 것인지, 아니면 별도의 무조건적(unconditional) 팩터를 나타내는 것인지에 대해 불가지론적(agnostic) 입장을 취한다."

**"agnostic"** = "모르겠고, 어느 쪽이든 상관없다." 이건 학술적 겸손함. "우리는 패턴을 발견했고, 모형을 제시했지만, 그 모형의 **깊은 이론적 해석**까지는 주장하지 않겠다."

---

## 유동성과의 연결 (p.931 중단~하단)

### 문장 21

> "We then investigate the source of this common global factor structure."

**뜯기**: 공통 팩터 구조의 **원인(source)**을 조사한다. "무엇이 일어나는가"에서 "왜 일어나는가"로 전환.

### 문장 22

> "We find only modest links to macroeconomic variables such as the business cycle, consumption, and default risk."

**뜯기**: 경기순환(business cycle), 소비(consumption), 부도 위험(default risk) 같은 거시경제 변수와는 **미미한 연결(modest links)**만 발견했다.

이건 의외의 결과다. 직관적으로 생각하면, 가치주는 경기 침체에 취약하니까 경기순환과 관련이 있을 것 같다. 하지만 데이터는 그 관계가 약하다고 말한다. 거시경제 변수로는 가치/모멘텀 프리미엄을 설명하기 어렵다.

### 문장 23

> "However, we find significant evidence that liquidity risk is negatively related to value and positively related to momentum globally across asset classes."

**뜯기**: 하지만(However) — 거시경제는 약하지만, **유동성 리스크(liquidity risk)**는 유의미한 관계가 있다.

- **유동성 리스크와 가치 = 음의 관계**: 유동성 리스크가 높아지면 가치 전략 수익이 나빠진다? 아니, 이건 좀 더 복잡하다. "가치 전략의 유동성 리스크 노출(loading)이 음수"라는 뜻이다. 가치 전략은 유동성이 나빠져도 상대적으로 덜 타격받거나, 오히려 유동성 위기에서 이익을 본다.
- **유동성 리스크와 모멘텀 = 양의 관계**: 모멘텀 전략은 유동성 리스크에 양으로 노출. 유동성이 나빠지면 모멘텀이 크게 타격받는다.

왜? 뒤에서 자세히 설명되지만, 핵심 직관은:
- **모멘텀** = "인기 있는 거래(popular trades)". 유동성 위기가 오면 모두가 인기 있는 포지션을 동시에 청산 → 모멘텀 대폭락.
- **가치** = "역발상(contrarian)". 유동성 위기에서 쏟아져 나오는 매물을 줍는 역할 → 타격이 적거나 이득.

### 문장 24-25

> "Pástor and Stambaugh (2003) and Sadka (2006) find that measures of liquidity risk are positively related to momentum in U.S. individual stocks."

**뜯기**: Pastor-Stambaugh(2003)와 Sadka(2006)는 미국 개별 주식에서 유동성 리스크가 모멘텀과 양의 관계라는 것을 발견했다.

| 논문 | 핵심 기여 |
|------|---------|
| **Pastor and Stambaugh (2003)** | **시장 유동성(market liquidity)** 리스크 측정치를 개발. 유동성 리스크에 대한 노출이 높은 주식이 더 높은 수익을 냄. 모멘텀 전략이 유동성 리스크에 양으로 노출. |
| **Sadka (2006)** | 유동성 리스크가 모멘텀 수익의 상당 부분을 설명한다는 직접적 증거. 유동성 쇼크가 모멘텀 전략의 대폭락과 관련. |

### 문장 26

> "We show that this link is also present in other markets and asset classes, and that value returns are significantly negatively related to liquidity risk globally, implying that part of the negative correlation between value and momentum is driven by opposite signed exposure to liquidity risk."

**뜯기**: 이 논문의 새로운 기여:

1. Pastor-Stambaugh와 Sadka의 발견이 미국 주식뿐 아니라 **다른 시장과 자산군에서도** 나타남
2. 가치 수익은 유동성 리스크와 유의미하게 **음의** 관계
3. 가치-모멘텀 음의 상관의 **일부**는, 유동성 리스크에 대해 **반대 부호의 노출**을 가지기 때문

쉽게 말하면: 가치와 모멘텀이 반대로 움직이는 이유 중 하나는, 유동성 위기가 올 때 가치는 방어적이고 모멘텀은 취약하기 때문이다. 같은 충격(유동성 악화)에 반대 방향으로 반응하니 음의 상관이 생긴다.

### 문장 27

> "Separating market from funding liquidity (see Brunnermeier and Pedersen (2009)), we further find that the primary link between value and momentum returns comes from funding risk, whose importance has increased over time, particularly after the funding crisis of 1998."

**뜯기**: 유동성을 두 종류로 나눈다:

1. **시장 유동성(Market Liquidity)** = 자산을 사고팔기 쉬운 정도. 매수-매도 호가 차이(bid-ask spread)가 작으면 시장 유동성이 좋은 것.
2. **펀딩 유동성(Funding Liquidity)** = 돈을 빌리기 쉬운 정도. 은행이 대출을 쉽게 해주면 펀딩 유동성이 좋은 것.

이 구분은 **Brunnermeier and Pedersen (2009)**의 핵심 아이디어다. 이 논문의 제3저자 Pedersen 본인의 이론이다.

핵심 발견: 가치와 모멘텀 수익률과의 **주된 연결고리**는 시장 유동성이 아니라 **펀딩 리스크(funding risk)**에서 온다. 그리고 이 관계의 중요성은 시간이 지나면서 **증가**했으며, 특히 **1998년 펀딩 위기** 이후 더 강해졌다.

💡 **1998년 펀딩 위기란?** LTCM(Long-Term Capital Management)이라는 초거대 헤지펀드가 붕괴한 사건. LTCM은 노벨 경제학상 수상자 2명을 포함한 드림팀이 운영했는데, 러시아 국채 디폴트를 시작으로 전 세계 금융 시장이 패닉에 빠지면서, 은행들이 돈줄을 죄고(펀딩 유동성 악화), LTCM의 레버리지 포지션이 붕괴했다. 이때 모멘텀 전략이 대폭락했고 가치 전략은 상대적으로 선방했다.

> 📚 **더 깊이**: [ch06 1998 LTCM 위기](../chapters/ch06-crisis-1998.md) — LTCM 붕괴의 전말과 유동성 위기의 메커니즘

### 문장 28

> "Importantly, these results cannot be detected by examining a single market in isolation."

**뜯기**: "중요하게도, 이 결과들은 하나의 시장을 격리 상태로 검토하는 것으로는 **발견할 수 없다**."

왜? 하나의 시장만 보면 통계적 검정력(statistical power)이 부족하다. 유동성 리스크와 가치/모멘텀의 관계가 각 시장에서는 노이즈에 묻혀서 "관계가 없다"고 나올 수 있다. 하지만 8개 시장의 데이터를 합치면, 노이즈가 상쇄되고 **진짜 신호**가 드러난다.

비유: 동전이 약간 치우쳐 있는지(51:49) 확인하려면, 10번 던져서는 알 수 없다. 10,000번 던져야 한다. 이 논문은 시장 수를 늘려서 "동전 던지기 횟수"를 늘린 것이다.

### 문장 29

> "The statistical power gained by looking across many markets at once—a unique feature of our analysis—allows these factor exposures to be revealed."

**뜯기**: "여러 시장을 동시에 보면서 얻는 통계적 검정력 — 우리 분석의 **고유한 특징** — 이 이 팩터 노출을 드러나게 해준다."

"unique feature"라는 표현으로, 이것이 단순히 "더 많은 데이터"가 아니라 **방법론적 혁신**임을 강조한다.

---

## 유동성의 한계 (p.931 하단)

### 문장 30

> "In terms of economic magnitudes, however, liquidity risk can only explain a small fraction of value and momentum return premia and comovement."

**뜯기**: "그러나(however), 경제적 크기로 볼 때, 유동성 리스크는 가치와 모멘텀 수익 프리미엄 및 공동움직임의 **작은 부분만** 설명할 수 있다."

이건 매우 솔직한 인정이다. 방금 유동성 리스크가 유의미한 연결고리라고 했는데, 바로 다음에 "크기는 작다"고 말한다. 통계적으로 유의미(p-value가 작다)하지만, 경제적으로는 전체의 일부만 설명한다는 것.

**통계적 유의성 vs 경제적 유의성**: 이 구분이 금융학에서 매우 중요하다.
- 통계적 유의성: "이 관계가 우연인가?" → p-value가 작으면 "우연이 아니다"
- 경제적 유의성: "이 관계가 얼마나 큰가?" → 수익률의 몇 %를 설명하는가

둘은 별개다. "우연이 아니지만 크기가 작다"는 것이 가능하다.

### 문장 31

> "While liquidity risk may partly explain the positive risk premium associated with momentum, because value loads negatively on liquidity risk, the positive premium associated with value becomes an even deeper puzzle."

**뜯기**: 유동성 리스크는 모멘텀의 양의 프리미엄을 **부분적으로** 설명할 수 있다 — "모멘텀은 유동성 위기에 취약하니까, 그 위험을 감수한 대가로 높은 수익을 받는 거야." 이건 말이 된다.

하지만 가치는? 가치는 유동성 리스크에 **음으로** 노출된다 — 유동성 위기 때 오히려 이득이거나 덜 손해본다. 그렇다면 가치는 유동성 위험을 감수하지 **않는** 것이다. 그런데도 양의 프리미엄을 받는다?

**"an even deeper puzzle"** = 유동성으로 설명하려 하면, 가치의 프리미엄은 더 큰 수수께끼가 된다. 위험을 감수하지 않는데 왜 보상을 받는가?

### 문장 32

> "Moreover, a simple equal-weighted combination of value and momentum is immune to liquidity risk and generates substantial abnormal returns."

**뜯기**: 게다가, 가치와 모멘텀을 50:50으로 단순히 합치면 유동성 리스크에 **면역(immune)**이다. 가치가 음, 모멘텀이 양으로 노출되니 합치면 상쇄된다. 그런데도 **상당한 비정상 수익(abnormal returns)**이 발생한다.

"비정상 수익"이란 시장 위험이나 유동성 위험으로 설명되지 않는 나머지 수익. 위험이 없는데 수익이 있다? 효율적 시장 가설에서는 이런 게 존재할 수 없다.

### 문장 33

> "Hence, funding liquidity risk can only provide a partial and incomplete explanation for momentum, but cannot explain the value premium or the value and momentum combination premium."

**뜯기**: 결론:
- 펀딩 유동성 리스크는 모멘텀에 대해 **부분적이고 불완전한** 설명만 제공
- 가치 프리미엄은 **설명 불가**
- 가치+모멘텀 결합 프리미엄도 **설명 불가**

이건 "우리가 원인을 찾았다"가 아니라 "원인의 일부를 찾았지만 나머지는 아직 미스터리"라는 솔직한 고백이다.

---

## 이론에 대한 시사점 (p.931 하단 ~ p.932 상단)

### 문장 34

> "The evidence we uncover sheds light on explanations for the existence of value and momentum premia."

**뜯기**: "우리가 발견한 증거는 가치와 모멘텀 프리미엄의 존재에 대한 설명에 **빛을 비춘다(sheds light on)**." — 완전한 답은 아니지만, 단서를 제공한다.

### 문장 35

> "For example, a strong correlation structure among these strategies in otherwise unrelated asset classes may indicate the presence of common global risk factors for which value and momentum premia provide compensation."

**뜯기**: 두 가지 해석 중 첫 번째 — **위험 보상(risk-based)** 해석.

서로 무관한 자산군에서 전략들이 강하게 상관된다면, **공통 글로벌 위험 팩터**가 존재하고, 가치와 모멘텀 프리미엄은 그 위험을 감수한 **보상(compensation)**일 수 있다.

쉽게 말하면: "전 세계 가치 전략이 같이 떨어지는 때가 있다면, 그건 전 세계적인 나쁜 사건(위험)이 발생했기 때문이고, 그 위험을 감수하는 대가로 평소에 높은 수익을 받는 것이다."

### 문장 36

> "Conversely, such correlation structure is not a prediction of existing behavioral models (e.g., Daniel, Hirshleifer, and Subrahmanyam (1998), Barberis, Shleifer, and Vishny (1998), Hong and Stein (1999))."

**뜯기**: 두 번째 해석 — **행동재무학(behavioral)** 해석에 대한 비판.

"반대로, 이러한 상관 구조는 기존 행동 모형의 **예측이 아니다**."

핵심: 행동재무학 모형들은 가치와 모멘텀이 왜 개별 시장에서 나타나는지는 설명할 수 있다. 하지만 "전 세계 가치 전략이 같이 움직이고, 전 세계 모멘텀과는 반대로 움직인다"는 것은 **예측하지 못한다**. 이건 이 모형들의 심각한 약점.

인용된 세 논문은 행동재무학의 핵심 모형들이다:

| 논문 | 핵심 아이디어 |
|------|-------------|
| **Daniel, Hirshleifer, and Subrahmanyam (DHS, 1998)** | 투자자의 **과잉확신(overconfidence)**과 **자기기여 편향(self-attribution bias)**. 자기 판단을 과신하면, 확인하는 뉴스에는 과잉반응하고 부정하는 뉴스에는 과소반응. → 모멘텀(단기 과잉반응) + 가치(장기 반전) 설명 가능. |
| **Barberis, Shleifer, and Vishny (BSV, 1998)** | **보수주의(conservatism)**와 **대표성 편향(representativeness heuristic)**. 새 정보에 느리게 반응(보수주의) → 모멘텀. 과거 패턴을 과도하게 외삽(대표성) → 가치. |
| **Hong and Stein (HS, 1999)** | 두 종류 투자자: **뉴스 워처(news watchers)**는 정보에 느리게 반응, **모멘텀 트레이더**는 과거 가격을 추종. 정보의 느린 확산 → 모멘텀. 모멘텀 트레이더의 과잉 추종 → 결국 반전(가치). |

문제: 이 모형들은 모두 **개별 시장 내의 개별 투자자 심리**에 기반한다. 미국 주식의 투자자 심리가 왜 일본 원자재 투자자의 심리와 동기화되는지는 설명하지 못한다.

> 📚 **더 깊이**: [ch03 금융학의 3대 전쟁](../chapters/ch03-theory-wars.md) — DHS, BSV, HS 모형의 상세 비교

---

### 각주 3: 투자/성장옵션 이론

> <sup>3</sup> See Gomes, Kogan, and Zhang (2003), Zhang (2005), Li, Livdan, and Zhang (2009), Belo (2010), Li and Zhang (2010), Liu and Zhang (2008), Berk, Green, and Naik (1999), Johnson (2002), Sagi and Seasholes (2007), and Liu, Whited, and Zhang (2009).

**뜯기**: 이 각주는 직전 본문에서 언급된 "rational asset pricing theories"의 구체적 목록이다. 본문에서는:

> "In addition to assuaging data mining concerns, evidence of consistent value and momentum premia across diverse asset classes may be difficult to reconcile under rational asset pricing theories that rely on firm investment risk or firm growth options as explanations for the value and momentum premia, which are predominantly motivated by firm equity."

**번역**: "다양한 자산군에 걸친 일관된 가치와 모멘텀 프리미엄의 증거는, 기업 투자 위험(firm investment risk)이나 기업 성장옵션(firm growth options)에 의존하는 합리적 자산가격결정 이론과 조화시키기 어려울 수 있다. 이 이론들은 주로 기업 주식(firm equity)에 의해 동기부여된 것이다."

핵심 비판: 이 이론들은 **기업**(공장 투자, 성장 기회)의 특성으로 가치/모멘텀을 설명한다. 하지만 **통화, 채권, 원자재**에는 "기업"이 없다. 달러/엔 환율에 "공장 투자 위험"은 적용 불가능하다.

각 논문이 이 맥락에서 왜 인용되는지:

| 논문 | 핵심 아이디어 | 한계 |
|------|-------------|------|
| **Gomes, Kogan, Zhang (2003)** | 기업의 투자 비가역성(irreversibility)이 가치 프리미엄 생성 | 기업 특유 |
| **Zhang (2005)** | 비대칭적 비용 구조 — 불황 시 가치주가 더 위험 → 가치 프리미엄은 위험 보상 | 기업 특유 |
| **Li, Livdan, Zhang (2009)** | 기업의 투자 결정이 기대수익률의 횡단면을 설명 | 기업 특유 |
| **Belo (2010)** | 생산 기반 자산가격결정 — 기업 투자와 자산 수익의 관계 | 기업 특유 |
| **Li and Zhang (2010)** | 투자 기반 모형으로 가치와 모멘텀 동시 설명 시도 | 기업 특유 |
| **Liu and Zhang (2008)** | 모멘텀이 산업 생산 성장률 리스크에 대한 보상 | 기업/산업 특유 |
| **Berk, Green, Naik (1999)** | 기업의 **성장옵션(growth option)**이 기대수익률을 결정 | 기업 특유 |
| **Johnson (2002)** | 성장옵션의 레버리지 효과가 모멘텀 생성 | 기업 특유 |
| **Sagi and Seasholes (2007)** | 기업 수준의 기본 변동이 모멘텀 수익률의 횡단면 변이를 설명 | 기업 특유 |
| **Liu, Whited, Zhang (2009)** | 투자 기반 모형의 정량적 평가 | 기업 특유 |

**공통된 한계**: "predominantly motivated by firm equity" — **전부 기업 주식에 기반**한 이론이다. 통화, 채권, 원자재에서 같은 패턴이 나타나는 것은 이 이론들로 설명할 수 없다.

이어지는 본문:

> "These theories seem ill equipped to explain the same and correlated effects we find in currencies, government bonds, and commodities."

**뜯기**: "이 이론들은 우리가 통화, 국채, 원자재에서 발견하는 동일하고 상관된 효과를 설명하기에 **부적합해 보인다(ill equipped)**."

"ill equipped" — 직역하면 "장비가 부족하다". 이 이론들이 틀렸다고 단정하는 게 아니라, "이 현상을 다룰 도구가 없다"고 완곡하게 비판하는 것.

---

## 결합의 힘 (p.932 상단)

### 문장 37

> "We also highlight that studying value and momentum jointly is more powerful than examining each in isolation."

**뜯기**: 가치와 모멘텀을 **함께** 연구하는 것이 각각을 **따로** 연구하는 것보다 더 강력하다(more powerful).

### 문장 38

> "The negative correlation between value and momentum strategies and their high positive expected returns implies that a simple combination of the two is much closer to the efficient frontier than either strategy alone, and exhibits less variation across markets and over time."

**뜯기**: 

- 음의 상관 + 양의 기대수익 → 단순 조합이 **효율적 프런티어(efficient frontier)**에 훨씬 가깝다

**효율적 프런티어란?** 주어진 위험 수준에서 최대 수익을 달성하는 포트폴리오들의 집합. 그래프에서 위험(x축)과 수익(y축)을 그리면, 효율적 프런티어는 왼쪽 위에 있는 곡선이다. 이 곡선에 가까울수록 "같은 위험으로 더 높은 수익" 또는 "같은 수익으로 더 낮은 위험".

가치와 모멘텀을 합치면:
- 수익 = (가치의 양의 수익 + 모멘텀의 양의 수익) / 2 → 여전히 양수
- 위험 = 둘이 반대로 움직이니까 상쇄 → 대폭 감소

이것이 **분산투자(diversification)**의 교과서적 사례. 둘 다 돈을 벌면서 반대로 움직인다 — 투자의 꿈이다.

"exhibits less variation across markets and over time" — 각 전략을 따로 보면 시장마다, 시기마다 크기가 다르지만, 합치면 그 변동이 줄어든다. 더 안정적.

### 문장 39

> "The return premium to a combination of value and momentum applied across all asset classes therefore presents an even bigger challenge for asset pricing theories to accommodate (e.g., Hansen and Jagannathan (1997))."

**뜯기**: 가치+모멘텀 결합의 수익 프리미엄은 자산가격결정 이론에 **더 큰 도전**이다.

왜 "더 큰"인가? 유동성 리스크로 모멘텀의 일부를 설명할 수 있었다. 하지만 결합 포트폴리오는 유동성 리스크에 면역이다. 그런데도 높은 수익? 이건 어떤 위험 보상 이론으로도 설명하기 어렵다.

**Hansen and Jagannathan (1997)**: HJ 바운드(Hansen-Jagannathan bound). 자산가격결정 이론이 맞으려면, 확률할인인자(stochastic discount factor, SDF)의 변동성이 자산의 샤프 비율(Sharpe ratio) 이상이어야 한다는 수학적 제약 조건. 가치+모멘텀 조합의 샤프 비율이 매우 높으면, 이론이 요구하는 SDF 변동성도 비현실적으로 높아져야 한다 — 이것이 "challenge".

---

## 관련 문헌 (p.932 중단)

### 문장 40

> "Our work also relates to the recent literature on global asset pricing."

**뜯기**: 이 논문과 관련된 최근 문헌을 소개한다. 이건 "우리와 비슷한 주제를 연구하는 다른 사람들이 있고, 우리는 그들과 이런 점에서 다르다"는 학술적 포지셔닝.

### 문장 41

> "Fama and French (2012) examine the returns to size, value, and momentum in individual stocks across global equity markets and find consistent risk premia across markets."

**뜯기**: **Fama and French (2012)** — 금융학의 대가 Fama와 French가 글로벌 주식시장에서 규모(size), 가치(value), 모멘텀(momentum) 프리미엄을 조사하고, 시장에 걸쳐 일관된 위험 프리미엄을 발견.

이 논문과의 차이: Fama-French는 **주식만** 본다. 이 논문은 주식 + 채권 + 통화 + 원자재까지 본다.

### 문장 42

> "Frazzini and Pedersen (2010) find consistent returns to 'betting against beta,' Koijen et al. (2012) document global 'carry' returns, and Moskowitz, Ooi, and Pedersen (2012) present global evidence of 'time series momentum.'"

**뜯기**: 관련 논문 세 편을 한 문장에 압축:

| 논문 | 전략 | 핵심 |
|------|------|------|
| **Frazzini and Pedersen (2010)** | "베타에 반대 베팅(Betting Against Beta, BAB)" | 저베타(안정적) 주식이 고베타(변동성 큰) 주식보다 위험 조정 수익이 높다. 전 세계적으로 일관. 공저자 Pedersen의 다른 연구. |
| **Koijen et al. (2012)** | "캐리(Carry)" | 고금리 자산 매수 + 저금리 자산 매도 전략이 전 자산군에서 작동. |
| **Moskowitz, Ooi, Pedersen (2012)** | "시계열 모멘텀(Time Series Momentum)" | 자산의 과거 수익률이 양수면 매수, 음수면 매도. 전 세계 선물 시장에서 작동. 공저자 Moskowitz와 Pedersen의 다른 연구. |

### 문장 43-45: 시계열 모멘텀과의 차이

> "Time-series momentum is a timing strategy using each asset's own past returns, which is separate from the cross-sectional momentum strategies we study here."

**뜯기**: **시계열 모멘텀(time-series momentum)**과 **횡단면 모멘텀(cross-sectional momentum)**은 다른 전략이다.

| 구분 | 횡단면 모멘텀 (이 논문) | 시계열 모멘텀 (MOP 2012) |
|------|----------------------|----------------------|
| 기준 | 다른 자산 대비 **상대** 수익률 | 자기 자신의 **절대** 수익률 |
| 신호 | "이 주식이 다른 주식보다 많이 올랐나?" | "이 주식이 올랐나 떨어졌나?" |
| 포지션 | 승자 매수 + 패자 매도 (롱-숏) | 올랐으면 매수, 떨어졌으면 매도 (롱 또는 숏) |
| 순포지션 | 항상 0 (롱 = 숏) | 방향 편향 가능 (전체가 올랐으면 순매수) |

> "Focusing on this different time-series phenomenon, Moskowitz, Ooi, and Pedersen (2012) examine returns to futures contracts on equity indices, bonds, currencies, and commodities—ignoring individual stocks, which comprise half our study here—and address a different set of questions."

**뜯기**: MOP(2012)는:
- 선물 계약만 본다 (개별 주식은 무시 — 이 논문 데이터의 절반)
- 다른 질문을 다룬다

> "Our focus is on the interaction between cross-sectional momentum and value strategies and their common factor structure globally, where we find striking comovement across assets and a link to liquidity risk."

**뜯기**: 이 논문의 초점:
- 횡단면 모멘텀과 가치의 **상호작용**
- 글로벌 **공통 팩터 구조**
- 자산 간 공동움직임 + 유동성 리스크와의 연결

MOP(2012)와 보완적이지 대체적이지 않다.

---

## 유동성과 차익거래 (p.932 하단 ~ p.933 상단)

### 문장 46

> "The link to funding liquidity risk may also be consistent with global arbitrage activity in the face of funding constraints influencing value and momentum returns (Brunnermeier and Pedersen (2009))."

**뜯기**: 펀딩 유동성 리스크와의 연결은, **자금 제약(funding constraints)** 하에서 **글로벌 차익거래 활동(global arbitrage activity)**이 가치와 모멘텀 수익에 영향을 미치는 것과도 일관된다.

**Brunnermeier and Pedersen (2009) 프레임워크**:

핵심 아이디어: 차익거래자(트레이더, 헤지펀드)는 돈을 빌려서 투자한다. 돈을 빌릴 수 있는 능력(펀딩 유동성)이 제한되면, 그들의 투자 활동이 위축되고, 시장 가격이 왜곡된다.

메커니즘:
```
시장 유동성 ↔ 펀딩 유동성 (서로 강화)
         ↓
손실 → 마진 콜 → 강제 청산 → 가격 하락 → 더 큰 손실 → ... (악순환)
```

### 문장 47-48

> "Why does momentum load positively on liquidity risk and value load negatively? A simple and natural story might be that momentum represents the most popular trades, as investors chase returns and flock to the assets whose prices appreciated most recently."

**뜯기**: 왜 모멘텀은 유동성 리스크에 양으로 노출되고 가치는 음으로 노출되는가?

**모멘텀 = 가장 인기 있는 거래(most popular trades)**

투자자들은 수익을 쫓는다(chase returns). 최근에 가장 많이 오른 자산에 몰려든다(flock). 그래서 모멘텀 포지션은 **혼잡한 거래(crowded trade)**가 된다.

### 문장 49

> "Value, on the other hand, represents a contrarian view."

**뜯기**: 반면에, 가치는 **역발상(contrarian view)**을 대표한다. 남들이 외면하는 싼 것을 사는 것이니까.

### 문장 50-51

> "When a liquidity shock occurs, investors engaged in liquidating sell-offs (due to cash needs and risk management) will put more price pressure on the most popular and crowded trades, such as high momentum securities, as everyone runs for the exit at the same time (Pedersen (2009)), while the less crowded contrarian/value trades will be less affected."

**뜯기**: 유동성 쇼크가 발생하면:

1. 투자자들이 현금 필요(cash needs)나 리스크 관리(risk management) 때문에 **청산 매도(liquidating sell-offs)**에 나선다
2. 가장 인기 있고 혼잡한 거래(= 모멘텀 포지션)에 **더 큰 가격 압력**이 발생한다
3. 왜? **모두가 동시에 출구로 달려가기 때문(everyone runs for the exit at the same time)**
4. 반면 덜 혼잡한 역발상/가치 거래는 **덜 영향**받는다

**Pedersen (2009)**: "Running for the Exit" — 제목 자체가 비유. 극장에 불이 나면 모두가 출구로 달린다. 문이 좁으면 밟혀 죽는다. 금융 시장도 마찬가지 — 모두가 같은 포지션을 동시에 청산하면 가격이 폭락한다.

비유: 영화관에서 인기 좌석(앞 중앙)에 앉은 사람이 많다. 불이 나면 그 구역 사람들이 가장 많이 밀린다. 비인기 좌석(뒤 구석)에 앉은 사람은 여유롭게 빠져나간다. 모멘텀 = 인기 좌석. 가치 = 비인기 좌석.

### 문장 52-53

> "Vayanos and Wooley (2012) offer a model of value and momentum returns due to delegated management that may be consistent with these results."

**뜯기**: **Vayanos and Wooley (2012)** — **위임 경영(delegated management)** 모형. 투자자가 직접 투자하지 않고 펀드 매니저에게 맡기는 구조에서 가치와 모멘텀이 발생하는 메커니즘.

> "They argue that flows between investment funds can give rise to momentum effects from inertia due to slow moving capital, and eventually push prices away from fundamentals causing reversals or value effects."

**뜯기**:
- **펀드 간 자금 흐름(flows)** → 자본이 느리게 움직이는 관성(inertia) → **모멘텀 효과** 발생
- 결국 가격이 펀더멘털에서 너무 멀어지면 → **되돌림(reversals)** 또는 **가치 효과** 발생

핵심 메커니즘:
1. 좋은 성과를 낸 펀드에 자금이 유입 → 그 펀드가 보유한 자산을 더 매수 → 가격 추가 상승 → 모멘텀
2. 나쁜 성과를 낸 펀드에서 자금 유출 → 보유 자산 매도 → 가격 추가 하락 → 모멘텀
3. 시간이 지나면 가격이 너무 벌어짐 → 결국 펀더멘털로 회귀 → 가치 효과

> "Correlation of value and momentum across different asset classes could also be affected by funds flowing simultaneously across asset classes, which could in turn be impacted by funding liquidity."

**뜯기**: 자산군 간의 가치/모멘텀 상관도 설명 가능 — 펀드가 **여러 자산군에 동시에** 자금을 투입/회수하면, 자산군 간에 같은 방향의 움직임이 생긴다. 그리고 이 자금 흐름은 **펀딩 유동성**의 영향을 받는다.

### 문장 54

> "However, matching the magnitude of our empirical findings remains an open question."

**뜯기**: "그러나, 우리의 실증 결과의 **크기(magnitude)**를 맞추는 것은 아직 **열린 질문(open question)**으로 남아 있다."

이론이 방향(양/음)은 맞출 수 있지만, 실제 데이터에서 관찰되는 수익률의 **크기**까지 설명하지는 못한다. "왜 이렇게 큰 프리미엄이 사라지지 않고 계속 존재하는가?" — 아직 답이 없다.

이건 솔직한 인정이자, 후속 연구를 위한 초대장이기도 하다.

---

## 논문 구조 안내 (p.933)

### 문장 55

> "The paper proceeds as follows."

**뜯기**: 논문의 나머지 부분을 안내하는 전형적인 로드맵 문장.

### Section I

> "Section I outlines our data and portfolio construction."

**뜯기**: **Section I** = 데이터와 포트폴리오 구축. 8개 자산군의 데이터는 어디서 왔는지, 가치와 모멘텀 포트폴리오를 어떻게 만들었는지 설명한다.

> 📚 **다음 해체**: [dissect-02 데이터와 포트폴리오 구축](dissect-02-data.md)

### Section II

> "Section II examines the performance of value and momentum across asset classes and documents their global comovement."

**뜯기**: **Section II** = 성과(performance) 측정 + 공동움직임(comovement) 문서화. 이 논문의 핵심 실증 결과가 여기에 있다. Table I, II와 Figure 1, 2가 포함된다.

> 📚 **다음 해체**: [dissect-03 수익률](dissect-03-returns.md), [dissect-04 공동움직임](dissect-04-comovement.md)

### Section III

> "Section III investigates the source of common variation by examining macroeconomic and liquidity risk."

**뜯기**: **Section III** = 공통 변동의 원인 조사. 거시경제 변수와 유동성 리스크를 검토한다. "왜"에 대한 답을 찾는 섹션.

> 📚 **다음 해체**: [dissect-05 거시경제와 유동성](dissect-05-macro.md)

### Section IV

> "and Section IV offers an empirically motivated three-factor model to describe the cross section of returns across asset classes."

**뜯기**: **Section IV** = 글로벌 3팩터 모형 제시. "실증적으로 동기부여된(empirically motivated)" — 데이터에서 관찰된 패턴에 기반해서 만들었다는 뜻. 순수한 이론이 아니라 데이터가 이끈 모형.

> 📚 **다음 해체**: [dissect-06 자산가격결정 모형](dissect-06-pricing.md)

### Section V

> "Section V briefly discusses the robustness of our results to implementation issues."

**뜯기**: **Section V** = 강건성 검토(robustness). 결과가 특정 가정이나 방법론에 의존하지 않고 **튼튼한지(robust)** 확인한다. 거래 비용, 다른 측정법, 다른 시기 등으로 바꿔도 결과가 유지되는가?

> 📚 **다음 해체**: [dissect-07 강건성](dissect-07-robustness.md)

### Section VI

> "Section VI concludes by discussing the implications of our findings."

**뜯기**: **Section VI** = 결론. 발견의 함의를 논의한다. "우리가 발견한 것이 학계와 실무에 어떤 의미인가?"

> 📚 **다음 해체**: [dissect-08 결론](dissect-08-conclusion.md)

---

## 이 섹션에서 배운 것

Introduction 5페이지에서 논문의 전체 뼈대가 드러났다:

| # | 핵심 | 위치 |
|---|------|------|
| 1 | 기존 연구는 미국 주식 + 가치 또는 모멘텀만 따로 연구 | p.930 상단 |
| 2 | 이 논문은 8개 자산군 × 가치+모멘텀을 함께 연구 | p.930 상단 |
| 3 | 핵심 질문 4가지: 변이, 상관, 경제적 동인, 벤치마크 | p.930 중단 |
| 4 | 가치/모멘텀이 모든 자산군에서 유의미한 프리미엄 | p.930 하단 |
| 5 | 가치끼리 양 상관, 모멘텀끼리 양 상관, 가치-모멘텀 음 상관 | p.930~931 |
| 6 | 글로벌 3팩터 모형(시장 + 가치 + 모멘텀)이 수익률 패턴 포착 | p.931 상단 |
| 7 | 펀딩 유동성이 부분적 원인, 특히 1998년 이후 | p.931 중단 |
| 8 | 유동성 리스크는 경제적 크기로는 작은 부분만 설명 | p.931 하단 |
| 9 | 행동 모형, 합리적 모형 모두 전 자산군 패턴 설명 불가 | p.931~932 |
| 10 | 가치+모멘텀 결합은 유동성 면역 + 효율적 프런티어 근접 | p.932 상단 |
| 11 | 모멘텀=인기 거래, 가치=역발상 → 유동성 쇼크 시 반대 반응 | p.932~933 |

---

## 여기서 멈추고 생각하기

Introduction을 다 읽었다. 저자들의 주장을 수동적으로 받아들이지 말고, 스스로 추론하자.

### 🤔 추론 연습

1. **"여러 시장을 동시에 보면 통계적 파워가 올라간다"** — 그렇다면, 왜 다른 연구자들은 진작 이렇게 안 했을까? (힌트: 데이터 접근성. AQR은 전 세계 데이터를 가지고 있지만, 대학 연구자는 쉽지 않다)

2. **"행동재무 모형이 자산군 간 상관을 설명 못 한다"** — 하지만 만약 **같은 헤지펀드**가 여러 자산군에서 동시에 가치/모멘텀 전략을 운용하면? 그 펀드의 매매가 상관을 만들어내는 것 아닌가? (이건 Vayanos & Wooley 2012가 부분적으로 다룬다)

3. **유동성이 "부분적" 설명** — 나머지는 뭘까? 저자들도 모른다고 했다. 가능한 후보: 투자자 심리의 글로벌 전염? 중앙은행 정책의 동조? 글로벌 경기 사이클?

### ⚡ 설계 비판 연습

이 논문의 데이터/방법론을 아직 안 봤지만(Section I에서 볼 것이다), Introduction만으로 의심할 수 있는 것:

1. **"단순하고 균일한 측정치"** — 단순하면 데이터 마이닝 방어가 되지만, 반대로 **진짜 프리미엄을 과소추정**할 수도 있다. 이건 양날의 검.
2. **시가총액 상위 90%만** — 대형주만 보면 실전 구현 가능성은 높지만, 소형주에서 효과가 더 크다면 "어디서나"가 아니라 "대형주에서만"일 수 있다.
3. **표본 기간** (1972~2011) — 2011년 이후에도 작동하는가? 이 논문은 답하지 않는다.

> **다음**: [dissect-02 데이터와 포트폴리오 구축](dissect-02-data.md) — 8개 자산군의 데이터를 어디서 가져왔고, 가치/모멘텀 포트폴리오를 어떻게 만들었는지 뜯는다.
