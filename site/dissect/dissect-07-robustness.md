# 논문 해체 7: 강건성과 실행 (Section V, p.975~981)

> 지금까지 논문은 대단한 발견을 했다. 가치와 모멘텀이 8개 자산군에서 돈을 벌고, 공통 팩터가 있고, 유동성 리스크가 부분적 원인이고, 3팩터 모형이 수익률의 72%를 설명한다. 하지만 현실 세계의 투자자는 이렇게 묻는다: **"그래서, 진짜로 돈을 벌 수 있는 건가?"** Section V는 그 질문에 정면으로 답한다. 거래 비용, 공매도, 포트폴리오 구성, 변동성 스케일링, 시장 중립, 측정 방법, 그리고 시간에 따른 변화 -- 7개의 반론을 하나씩 받아친다.

---

## Section V 도입 (p.975~976)

> "Finally, we examine the robustness of our findings to implementation issues."

### 뜯기

**"Finally"** -- 이 단어가 논문 구조에서의 위치를 알려준다. Section I(서론) → II(수익률과 공변동) → III(유동성 리스크) → IV(자산가격결정 검정) → 그리고 마지막으로 V(강건성). 주요 발견은 끝났고, 이제 **방어전**이다.

**"robustness"** -- 강건성. 학술 논문에서 이 단어는 특별한 의미를 가진다. "우리의 결과가 **특정 가정이나 방법론에 의존하는 것이 아니라**, 다양한 조건에서도 유지된다"는 것을 보여주는 것이다. 심사자(referee)가 "이거 다르게 하면 결과 달라지지 않느냐?"고 물으면 여기서 답한다.

**"implementation issues"** -- 실행 이슈. 학술 연구의 포트폴리오는 **종이 위의 포트폴리오**(paper portfolio)다. 거래 비용 없고, 공매도 제한 없고, 무한한 유동성을 가정한다. 현실은 다르다. 이 괴리를 인정하고 다루겠다는 것.

> 📚 **더 깊이**: [ch12 강건성 검정의 의미](../chapters/ch12-robustness.md) -- 왜 학술 논문에서 강건성이 필수인지

---

> "A reader convinced of the efficacy of value and momentum strategies, particularly in combination, may be concerned with real world implementation issues."

### 뜯기

**"A reader convinced"** -- "이미 우리 결과를 믿는 독자"라는 전제를 깔고 시작한다. Section I~IV에서 증거를 충분히 제시했으니, 이제 "믿되, 현실에서 되느냐"를 다루겠다는 구조.

**"particularly in combination"** -- 가치와 모멘텀의 50:50 조합이 샤프 비율 1.59를 기록했었다. 이건 너무 좋아서 오히려 의심을 산다. "조합의 효과가 현실에서도 유지되느냐"가 핵심 관심사.

**"real world implementation issues"** -- 현실 세계의 실행 이슈. 구체적으로 뭘 말하는가? 바로 다음 문장에서 나열한다.

---

> "Though well beyond the scope of this paper, in this section we briefly discuss some practical concerns, including implementation costs and portfolio construction, as well as opportunities to improve upon our admittedly but intentionally simple approach."

### 뜯기

**"well beyond the scope of this paper"** -- 이 면책 조항이 중요하다. 저자들은 "우리가 여기서 다루는 건 **맛보기**에 불과하고, 완전한 실행 분석은 별도의 논문이 필요하다"고 선을 긋는다. 이건 솔직한 태도이자, 다른 연구자(특히 Israel & Moskowitz (2012), Frazzini, Israel & Moskowitz (2012))에게 공간을 열어주는 것이다.

**"briefly discuss"** -- 간략히 논의. 이 Section 전체가 약 6페이지인데, 각 하위 주제가 반~1페이지 정도로 짧다. 깊이보다 **범위**에 초점.

**"admittedly but intentionally simple approach"** -- **"인정하건대 단순하지만, 의도적으로 단순한"** 접근법. 이 표현이 이 논문의 방법론적 철학을 압축한다:

- **왜 단순하게 했나?** (1) 데이터 마이닝 위험 최소화 (2) 재현 가능성 극대화 (3) 8개 자산군에 동일한 기준 적용
- **단순함의 대가는?** 각 자산군에 최적화된 전략보다 성과가 낮을 수 있음
- **그래도 단순한 이유는?** "단순한데도 이만큼 된다"가 "최적화해서 겨우 이만큼 된다"보다 **훨씬 강력한 증거**이기 때문

---

## A. Transaction Costs (거래 비용, p.976)

> "Like most academic studies, we focus on gross returns, which are most suitable to illuminating the relation between risk and returns."

### 뜯기

**"gross returns"** -- 총수익률. 거래 비용을 차감하지 않은 수익률이다.

학술 연구가 총수익률을 쓰는 이유: 거래 비용은 **투자자마다 다르다**. 개인 투자자는 수수료가 높고, 대형 기관은 낮다. 선물은 주식보다 훨씬 저렴하다. 따라서 **위험-수익 관계의 본질**을 연구하려면 거래 비용이라는 "잡음"을 걷어내고 보는 것이 맞다.

**하지만** -- 다음 문장이 바로 반론을 인정한다.

---

> "However, gross returns overstate the profits earned by pursuing the strategies we examine in practice."

### 뜯기

**"overstate the profits"** -- 이익을 과장한다. 총수익률 기반의 분석은 **현실에서 벌 수 있는 돈보다 더 많이 벌 것처럼 보인다**. 특히 모멘텀 전략은 회전율(turnover)이 높아서 거래 비용의 영향을 더 크게 받는다.

이건 가치/모멘텀 연구에 대한 가장 오래된 비판 중 하나다. "종이 위에서는 돈을 벌지만, 거래 비용 빼면 남는 게 없다."

---

> "A few papers try to examine the transaction costs and capacity of these strategies, especially momentum, perhaps due to its higher turnover. For example, Korajczyk and Sadka (2004) and Lesmond, Schill, and Zhou (2003) argue that the real world returns and capacity of equity momentum strategies are considerably lower than the theoretical results would imply."

### 뜯기

여기서 **비판적 논문 두 편**을 소개한다:

| 논문 | 주장 |
|------|------|
| **Korajczyk & Sadka (2004)** | 모멘텀의 현실 수익과 **수용력(capacity)**이 이론이 암시하는 것보다 현저히 낮다 |
| **Lesmond, Schill & Zhou (2003)** | 모멘텀 수익의 상당 부분이 거래 비용에 의해 잠식된다 |

**"capacity"(수용력)**란 무엇인가? 전략에 투입할 수 있는 돈의 상한이다. $100만으로 되는 전략이 $100억으로도 되는가? 작은 주식을 사야 하는 전략은 돈이 커지면 시장 충격(market impact)이 커져서 수익이 사라진다.

**"especially momentum, perhaps due to its higher turnover"** -- 모멘텀이 가치보다 회전율이 높다. 왜? 가치주는 "싸면 계속 보유"하면 되지만, 모멘텀은 "최근 승자"가 매달 바뀌므로 포트폴리오를 자주 교체해야 한다. 거래가 많으면 비용도 많다.

---

> "Their conclusions are based on aggregate trade data and theoretical models of transactions costs."

### 뜯기

이 한 문장이 비판자들에 대한 **반격의 포석**이다. Korajczyk-Sadka와 Lesmond 등의 결론이 **실제 거래 데이터가 아니라**, 집계 데이터(aggregate trade data)와 이론적 모형에 기반한다는 점을 짚는다.

왜 이게 중요한가? 이론적 거래 비용 모형은 종종 **현실보다 비용을 과대추정**한다. 실제 대형 기관투자자가 쓰는 VWAP, 알고리즘 트레이딩, 다크풀 등을 반영하지 못하기 때문이다.

---

> "Using live trading data, Frazzini, Israel, and Moskowitz (2012) challenge these results and show that the real world trading costs of value, momentum, and a combination of the two in equities are orders of magnitude lower for a large institution than those implied by the calibrated models of Korajczyk and Sadka (2004) and Lesmond, Schill, and Zhou (2003)."

### 뜯기

여기가 **핵심 반론**이다.

**Frazzini, Israel & Moskowitz (2012)** -- 이 논문은 AQR의 **실제 거래 데이터**(live trading data)를 사용한다. AQR은 이 전략들을 실제로 운용하는 회사다. 그들의 실거래 비용은 이론 모형이 예측한 것보다 **자릿수(orders of magnitude)만큼 낮다**.

**"orders of magnitude lower"** -- "자릿수만큼 낮다"는 것은 10배, 100배 수준의 차이를 말한다. 이론 모형이 거래 비용을 100bp로 추정했다면, 실제는 1~10bp 수준이라는 뜻이다.

**왜 이렇게 차이가 나는가?**
1. 대형 기관은 소매 투자자보다 훨씬 낮은 수수료를 지불
2. 알고리즘 트레이딩으로 시장 충격 최소화
3. 급하지 않게 며칠에 걸쳐 주문 집행
4. 호가-매도 스프레드의 안쪽에서 체결

**이해충돌 주의**: Frazzini, Israel, Moskowitz 모두 AQR 소속이다. "우리 전략이 비용 빼도 잘 된다"고 말하는 것이니 잠재적 편향이 있다. 하지만 데이터가 실거래 데이터라는 점에서, 이론 모형보다 현실을 더 잘 반영하는 것은 사실이다.

---

> "As a result, Frazzini, Israel, and Moskowitz (2012) conclude that these strategies can be scaled considerably and still generate strong net returns."

### 뜯기

**"can be scaled considerably"** -- 상당한 규모까지 확장 가능하다. 즉 수용력(capacity) 문제가 Korajczyk-Sadka가 우려한 것만큼 심각하지 않다.

**"strong net returns"** -- 순수익률도 강하다. 거래 비용을 빼도 의미 있는 수익이 남는다.

---

> "In addition, we focus on an extremely large and liquid set of equities in each market (approximately the largest 17% of firms), where trading costs, price impact, and capacity constraints are minimized."

### 뜯기

저자들이 거래 비용 비판에 대한 **구조적 방어**를 제시한다. 이 논문은 처음부터 **대형주**만 사용했다. 각 시장에서 상위 약 17%의 대형주.

**왜 대형주만?**
- **거래 비용 낮음**: 유동성이 풍부해서 스프레드가 좁고, 시장 충격이 작다
- **가격 충격 최소**: 큰 주문도 가격을 크게 움직이지 않는다
- **수용력 큼**: 많은 돈을 투입해도 전략이 작동한다

이건 "거래 비용이 걱정된다"는 비판에 대해 "우리는 애초에 비용이 가장 적은 영역에서 연구했다"고 답하는 것이다.

---

> "Studies on trading costs also focus exclusively on individual stocks, but half of the markets that we examine are implemented with futures contracts, which typically have much lower trading costs than stocks. Hence, although our equity strategies outperform our nonequity strategies in gross returns, net of trading cost returns are likely to be much closer."

### 뜯기

두 번째 **구조적 방어**. 이 논문의 8개 자산군 중 4개(국가지수, 통화, 국채, 원자재)는 **선물 계약**으로 거래된다.

선물의 거래 비용이 주식보다 훨씬 낮은 이유:
1. **표준화**: 거래소에서 정해진 규격으로 거래되므로 효율적
2. **레버리지**: 증거금만 내고 거래하므로 자본 효율이 높음
3. **스프레드**: 주요 선물의 호가 스프레드는 극히 좁음 (예: S&P 500 E-mini 선물은 0.01% 미만)

따라서 주식 전략의 총수익률이 비주식 전략보다 높지만, **순수익률(거래 비용 차감 후)**로 보면 그 차이가 줄어든다. 비주식 전략의 상대적 매력이 올라간다는 뜻이다.

---

> "Furthermore, Garleanu and Pedersen (2012) model how portfolios can be optimally rebalanced to mitigate transaction costs and demonstrate how this improves the net performance of commodity momentum strategies, for example."

### 뜯기

**Garleanu & Pedersen (2012)** -- Pedersen은 이 논문의 공저자이기도 하다. 이 논문은 **최적 리밸런싱**(optimal rebalancing) 이론을 제시한다.

핵심 아이디어: 매달 포트폴리오를 목표 비중으로 **완전히** 리밸런싱하는 것(naive rebalancing)은 비효율적이다. 목표 비중에서 약간 벗어나더라도 거래를 줄이면 **비용 절약 > 수익 손실**이 되는 구간이 있다. 이 트레이드오프를 최적화하면 순수익을 개선할 수 있다.

---

> "In a similar spirit, Frazzini, Israel, and Moskowitz (2012) demonstrate how equity portfolios can benefit from several practical steps taken to reduce transactions costs that, while having a cost in terms of gross returns (from style drift), can improve net returns."

### 뜯기

**"style drift"** -- 스타일 이탈. 포트폴리오가 원래 의도한 스타일(예: 순수 모멘텀)에서 벗어나는 것. 리밸런싱을 줄이면 스타일이 흐려지지만, 거래 비용 절약이 더 클 수 있다.

거래 비용 절약을 위한 실무적 기법들:
- 리밸런싱 빈도 줄이기 (매월 → 매분기)
- 거래 비용 대비 기대 수익을 고려해 포트폴리오 최적화
- 보유 기간 연장 또는 단축으로 최적 타이밍 선택

---

> "For instance, the strategies we study here are all naively rebalanced exactly monthly no matter what the expected gain per amount traded. Varying the rebalance frequency, optimizing the portfolios for expected trading costs, and extending or occasionally contracting the trade horizon can all improve the basic implementation of these strategies."

### 뜯기

이 문장이 Section V.A의 핵심 메시지를 압축한다:

**이 논문의 전략은 가장 단순한 방식(매월 무조건 리밸런싱)으로 구현했다.** 현실에서는 더 똑똑하게 할 수 있다. 따라서 논문의 결과는 **하한(lower bound)**에 가깝다.

이건 "거래 비용 때문에 안 된다"는 비판을 뒤집는 논리다: "우리는 비용 최적화를 전혀 안 했는데도 이만큼 나온다. 최적화하면 더 좋아진다."

> 📚 **더 깊이**: [ch13 거래 비용과 실행](../chapters/ch13-transaction-costs.md) -- 시장 충격, 스프레드, 수용력의 상세

---

## B. Shorting (공매도, p.976~977)

> "Our paper is, of course, as much about shorting assets as it is about going long."

### 뜯기

이 논문의 모든 전략은 **롱-숏(long-short)** 포트폴리오다. "싼 거 사고 비싼 거 판다"(가치), "오른 거 사고 떨어진 거 판다"(모멘텀). "판다" 부분이 **공매도(shorting)**다.

공매도란? 갖고 있지 않은 자산을 빌려서 팔고, 나중에 싸게 사서 돌려주는 것. 가격이 떨어지면 돈을 번다.

문제: 공매도에는 **추가 비용**이 있다. 주식을 빌리는 비용(대차 비용), 담보 요구, 규제 제한 등. 만약 이 비용이 너무 크면, 숏 쪽에서 번 돈이 비용에 잠식된다.

---

> "While going long versus short is symmetric for futures, shorting involves special costs in stock markets."

### 뜯기

**선물에서는 롱과 숏이 대칭**이다. 선물 매수와 선물 매도의 비용이 동일하다. 왜? 선물은 단순히 "미래에 이 가격에 사겠다/팔겠다"는 계약이므로, 방향에 관계없이 동일한 구조다.

**주식에서는 비대칭**이다. 주식을 사는 것(롱)은 단순하지만, 공매도(숏)는:
1. 주식을 빌려야 한다 → 대차 수수료(lending fee)
2. 담보를 맡겨야 한다 → 자본 비용
3. 갑자기 빌려준 사람이 주식을 돌려달라고 할 수 있다(recall risk)
4. 일부 국가/시기에는 규제로 금지될 수 있다

---

> "If our results are completely dependent on shorting and if shorting is too costly or not implementable, this would certainly raise questions about the real world efficacy of these strategies."

### 뜯기

비판의 정확한 형태를 먼저 서술한다: "만약 결과가 숏에 완전히 의존하고, 공매도가 너무 비싸거나 불가능하면, 현실 세계에서의 효과에 의문이 생긴다."

이건 실제로 많은 비판자들이 제기하는 논점이다. 특히 개인 투자자나 뮤추얼 펀드처럼 공매도가 제한된 투자자에게는 중요한 문제.

---

> "However, Israel and Moskowitz (2012) provide evidence that the return contributions of both value and momentum strategies across the same asset classes we study here are roughly equal from the long and short sides of the portfolio and that long-only portfolios of value and momentum still produce abnormal returns."

### 뜯기

**Israel & Moskowitz (2012)**의 핵심 발견 두 가지:

1. **롱 쪽과 숏 쪽의 기여가 대략 동일** -- 가치 전략의 총수익 중 약 절반이 롱(싼 주식 매수)에서, 약 절반이 숏(비싼 주식 매도)에서 온다. 모멘텀도 마찬가지.

2. **롱 온리 포트폴리오도 이상 수익을 낸다** -- 숏을 완전히 빼도, 롱 쪽만으로 벤치마크를 이기는 알파가 있다.

이 두 가지가 의미하는 것: 공매도가 불가능하더라도 **수익의 절반은 살릴 수 있다**. 완벽하진 않지만, "숏 없으면 아무것도 아니다"라는 비판은 틀렸다.

---

> "Thus, these strategies are still effective even if shorting is restricted."

### 뜯기

결론: 공매도가 제한되어도 전략은 여전히 효과적이다.

---

> "In addition, Frazzini, Israel, and Moskowitz (2012) provide some evidence that the trading costs of shorting stocks are not materially different from the costs of buying or selling stocks, and that real-world shorting costs for a large institutional investor are not prohibitive to running sizeable funds in these strategies."

### 뜯기

Frazzini, Israel & Moskowitz (2012)의 추가 증거:

- **공매도 비용 ≈ 매수/매도 비용** -- 대형 기관투자자 수준에서, 주식을 공매도하는 비용이 주식을 매수하거나 매도하는 비용과 **실질적으로 다르지 않다**. 대형주의 경우 대차 비용이 아주 낮기 때문이다.

- **실행 불가능할 정도로 비싸지 않다** -- 상당한 규모의 펀드를 운용해도 괜찮다.

다시 한번 주의: 이 증거를 제공하는 사람들이 **AQR 소속**이다. 하지만 "대형 기관의 대형주 공매도 비용이 낮다"는 것 자체는 업계 통설과 부합한다.

> 📚 **더 깊이**: [ch13 거래 비용과 실행](../chapters/ch13-transaction-costs.md) -- 공매도 메커니즘, 대차 비용, recall risk 상세

---

## C. Portfolio Formation (포트폴리오 구성, p.977)

> "In this paper we intentionally keep everything as simple as possible, both for clarity and as a precaution against the pernicious effects of data mining."

### 뜯기

**"intentionally simple"** -- 의도적으로 단순하게. 이 표현이 이 논문에서 세 번째 등장한다. 저자들이 이 철학을 얼마나 강조하는지 알 수 있다.

**"data mining"** -- 데이터 마이닝. 여기서는 부정적 의미로 쓰인다. 데이터를 이리저리 가공해서 좋은 결과만 골라 보고하는 것. 예: "10분위로 나누면 안 되길래 7분위로 나눴더니 됐다" 같은 식.

**왜 단순함이 데이터 마이닝 방어가 되는가?** 연구자가 선택할 수 있는 "자유도"가 줄어든다. 3분위와 시그널 가중치 -- 이 두 가지 단순한 방법만 쓰면, "최적 결과를 찾아서 보고했다"는 의심을 줄일 수 있다.

---

> "In fact, one of the paper's objectives is to provide a robust out-of-sample test of ideas that have been largely tested in individual, particularly U.S., stocks and extend them to other asset classes."

### 뜯기

이 문장이 논문의 **방법론적 정체성**을 규정한다. 이 논문은 새로운 전략을 발명한 것이 아니다. **이미 알려진 전략이 다른 시장에서도 되는지** 확인하는 **표본 외 검정(out-of-sample test)**이다.

**왜 이게 가치 있는가?** 미국 주식에서 발견된 패턴은 데이터 마이닝의 산물일 수 있다. 하지만 같은 패턴이 영국 주식, 일본 주식, 통화, 원자재에서도 나타난다면? 데이터 마이닝일 확률이 급격히 낮아진다.

---

> "However, when faced with real world implementation, there are many choices to consider. For example, we look at two simple portfolio implementations in the paper: top 1/3 minus bottom 1/3, and a linear weighting scheme based on ranking securities."

### 뜯기

논문의 두 가지 포트폴리오 구성 방법:

| 방법 | 설명 | 장점 | 단점 |
|------|------|------|------|
| **3분위 스프레드** (P3-P1) | 상위 1/3 매수, 하위 1/3 매도 | 단순, 직관적 | 중간 1/3의 정보를 버림 |
| **시그널 가중** | 순위에 비례해 선형적으로 가중 | 모든 종목의 정보 활용 | 약간 더 복잡 |

---

> "These are far from the only possibilities, and the choice of weighting scheme can impact not only gross returns, but also transactions costs."

### 뜯기

현실에서는 선택지가 훨씬 많다:
- 5분위, 10분위(decile) 분류
- 시총 가중 vs 동일 가중
- 시그널 강도에 따른 비선형 가중
- 섹터 중립(sector-neutral) 포트폴리오

각 선택이 수익률뿐 아니라 거래 비용에도 영향을 미친다. 예를 들어 10분위는 3분위보다 극단적인 종목을 포함하므로 수익은 높을 수 있지만, 소형주가 많아 거래 비용도 높아진다.

---

> "While we do not claim that either of these choices is optimal in either a gross or net return sense, we also explore more extreme sorts of securities into deciles and find that doing so does not materially affect the results."

### 뜯기

**10분위(decile) 분류도 시도**했다. 결과가 실질적으로 달라지지 않았다. 이건 결과가 포트폴리오 구성 방법에 민감하지 않다는 증거.

---

> "In the Internet Appendix we replicate our main results for individual equity markets in the United States, the United Kingdom, Europe, and Japan for decile portfolios and find very similar results."

### 뜯기

Internet Appendix(온라인 부록)에서 4개 주식시장의 10분위 포트폴리오 결과를 제시. 주요 결과와 매우 유사.

---

> "In the Internet Appendix we also plot the pricing errors of our three-factor model for these 80 decile portfolios of value and momentum in each of the four equity markets (the United States, the United Kingdom, Europe, and Japan). As the accompanying figure shows and the asset pricing statistics verify, our three-factor model does a good job of capturing these more extreme portfolio returns, too."

### 뜯기

80개 10분위 포트폴리오 (= 4개 시장 x 가치/모멘텀 2개 x 10분위) 에 대해서도 3팩터 모형이 잘 작동한다. 이건 Section IV의 자산가격결정 결과가 포트폴리오 구성 방법에 강건하다는 것을 보여준다.

---

> "We also value weight stocks within our portfolios and equal weight the securities in other asset classes. However, other weighting schemes yield similar results and, because we focus on the largest, most liquid securities, trading costs are unlikely to be affected much by such changes."

### 뜯기

가중 방식:
- **주식**: 시가총액 가중(value weight) -- 큰 회사에 더 많은 돈 투입
- **비주식**: 동일 가중(equal weight)

다른 가중 방식으로 바꿔도 결과가 비슷하다. 그리고 대형 유동주에 집중하기 때문에 가중 방식 변경이 거래 비용에 미치는 영향도 작다.

---

> "Hence, our main findings are robust to a variety of perturbations and portfolio formations."

### 뜯기

Section V.C의 결론: 포트폴리오 구성 방법을 다양하게 바꿔도 주요 결과가 유지된다.

---

## D. Volatility Scaling (변동성 스케일링, p.977~978)

> "When we aggregate our strategies across asset classes, we ensure that the different asset classes are scaled to have similar volatility. To do so, we scale each asset class by the inverse of its realized volatility over the full sample."

### 뜯기

**변동성 스케일링**이란? 자산군마다 변동성(가격 변동 폭)이 다르다. 원자재 선물 전략의 변동성이 20%이고 통화 전략의 변동성이 5%라면, 단순히 합치면 원자재가 전체 포트폴리오를 지배한다. 이걸 방지하기 위해 각 자산군의 수익률을 변동성의 역수로 곱해서 **동일한 변동성**으로 맞춘다.

**"full sample"** -- 전체 표본 기간의 실현 변동성을 사용한다. 이건 **사후적(ex post)** 정보다.

문제: 사후 변동성은 **투자 시점에 알 수 없다**. 미래에 실현될 변동성을 써서 스케일링하는 것이므로, "미래를 훔겨보는" 것이다(look-ahead bias). 현실에서는 불가능하다.

---

> "However, since the full sample is not known in advance, a real world portfolio would need to scale by a measure of volatility that is estimated ex ante."

### 뜯기

저자들이 이 문제를 인정한다. 현실의 포트폴리오는 **사전적(ex ante)** 변동성 추정치를 써야 한다.

---

> "For robustness, in the Internet Appendix we report results for all of our value and momentum strategies scaled to the same ex ante volatility of 2% per annum using a rolling 3-year estimate of each portfolio's volatility from daily returns."

### 뜯기

Internet Appendix에서 **사전적 방법**으로 재검증:

| 항목 | 사후적 (본문) | 사전적 (부록) |
|------|-------------|-------------|
| 정보 | 전체 표본 실현 변동성 | 과거 3년 롤링 변동성 |
| 목표 | 동일 변동성 | 연 2% 변동성 |
| 데이터 | 전 기간 한 번에 | 일별 수익률, 3년 창 |
| 현실성 | 불가능 (미래 정보) | 가능 (과거 정보만 사용) |

**연 2%** -- 이건 각 전략의 목표 변동성을 연 2%로 맞춘다는 뜻. 매우 보수적인 수준.

---

> "The results are reported together with the original unadjusted returns. The Sharpe ratios and correlations of the strategies are very similar and yield identical conclusions."

### 뜯기

핵심 결론: 사전적 변동성 스케일링을 사용해도 **샤프 비율과 상관 구조가 거의 동일**하다. 사후 정보 편향이 결과를 왜곡하지 않았다.

이건 안심이 되는 결과다. 만약 사전/사후가 크게 달랐다면, "논문의 결과가 미래 정보를 활용해서 좋아 보이는 것"이라는 치명적 비판에 노출되었을 것이다.

> 📚 **더 깊이**: [ch14 변동성 스케일링](../chapters/ch14-vol-scaling.md) -- 사전 vs 사후 변동성, 롤링 추정, 목표 변동성 전략

---

## E. Dollar Neutral vs. Beta Neutral (달러 중립 vs 베타 중립, p.978)

> "As is standard in academic studies, our strategies are constructed to be $1 long and $1 short, but they need not have a zero market beta exposure (at the local or global level)."

### 뜯기

**달러 중립(Dollar Neutral)**: $1 매수 + $1 매도 = 순투자 $0. 이 논문의 모든 전략이 이 방식이다.

**하지만** 달러 중립 ≠ 시장 중립. 왜?

예를 들어, 가치 전략의 롱 쪽(싼 주식)이 베타 1.2이고 숏 쪽(비싼 주식)이 베타 0.8이면:
- 달러로는 중립: $1 롱 - $1 숏 = $0
- 베타로는 비중립: 1.2 - 0.8 = 0.4만큼 시장에 노출

이 0.4의 시장 노출이 수익의 일부를 설명할 수 있다.

---

> "However, real world portfolios can, and often do, attempt to create long-short portfolios that are ex ante beta neutral (in addition to, or instead of, being dollar neutral)."

### 뜯기

**베타 중립(Beta Neutral)**: 롱 쪽과 숏 쪽의 시장 베타를 동일하게 맞추는 것. 이렇게 하면 시장 전체의 상승/하락에 영향을 받지 않는 **순수한 팩터 수익**만 남는다.

현실의 헤지펀드는 대부분 베타 중립을 추구한다. 시장 방향에 베팅하는 것이 아니라 가치/모멘텀의 **순수 효과**에만 베팅하기 위해.

---

> "We find that our inferences based on the strategies' alpha from factor regressions are not affected by market hedging."

### 뜯기

결론: 팩터 회귀에서 나온 알파가 **시장 헤징 여부에 영향받지 않는다**.

왜 그런가? 이 논문의 팩터 회귀(Section IV)에서 이미 시장 팩터(MKT)를 통제했다. 따라서 알파는 이미 시장 노출을 제거한 후의 초과 수익이다. 포트폴리오를 베타 중립으로 구성하든 달러 중립으로 구성하든, 회귀의 알파에는 차이가 없다.

---

## F. Value and Momentum Measures (가치와 모멘텀 측정치, p.978~979)

> "We use one measure for value and one for momentum for all eight markets we study."

### 뜯기

8개 시장 전부에 **단일 측정치**를 적용:
- **가치**: 자산군별로 하나의 가치 지표 (예: 주식은 BE/ME, 통화는 5년 PPP 편차)
- **모멘텀**: 전 자산군 공통으로 MOM2-12

---

> "We choose the most studied or simplest measure in each case and attempt to maintain uniformity across asset classes to minimize the potential for data mining."

### 뜯기

다시 **데이터 마이닝 방어**. 가장 많이 연구된 또는 가장 단순한 측정치를 선택하고, 자산군 간 **균일성(uniformity)**을 유지.

"가장 많이 연구된" 측정치를 쓰면 왜 데이터 마이닝이 줄어드는가? 이미 알려진 측정치는 연구자가 "이게 안 되길래 저걸로 바꿨더니 됐다"고 할 수 없기 때문이다. 사전에 규정된(pre-specified) 측정치를 쓰는 것이다.

---

> "Using these simple, uniform measures results in positive risk premia for value and momentum in every asset class we study, though some of the results are statistically insignificant."

### 뜯기

**모든** 자산군에서 양(+)의 프리미엄. 하지만 일부는 통계적으로 유의하지 않다. 특히 채권의 가치 효과가 약했다 (Section II에서 다룸).

---

> "In particular, our weakest results pertain to bonds, which do not produce statistically significant premia."

### 뜯기

가장 약한 결과 = 채권. 이건 Section II.B에서 이미 인정한 사실이다. 채권의 가치 측정치(10년 만기 수익률의 5년 변화)가 최적이 아닐 수 있다.

---

> "However, data mining worries may be weighed against the potential improvements from having better measures of value and momentum."

### 뜯기

트레이드오프: **데이터 마이닝 위험** vs **더 나은 측정치의 잠재적 개선**. 저자들은 보수적으로 전자를 선택했다.

---

> "For example, value strategies among bonds can be markedly improved with more thoughtful measures."

### 뜯기

채권의 가치 전략은 더 정교한 측정치를 쓰면 **현저히 개선**된다. 구체적으로:

---

> "Using our current measure of value, the 5-year change in yields of 10-year maturity bonds, we are only able to produce a Sharpe ratio of 0.18 and an alpha of 1.9% that is not statistically significant (t-statistic of 1.68)."

### 뜯기

현재 측정치의 채권 가치 성과:
- **샤프 비율**: 0.18 (매우 낮음)
- **알파**: 1.9% (t = 1.68, 통계적 유의성 미달 -- 보통 2.0 이상 필요)

---

> "However, Panel C of Table I reports results for value strategies among bonds that use alternative measures, such as the real bond yield, which is the yield on 10-year bonds minus the 5-year forecast in inflation, and the term spread, which is the yield on 10-year bonds minus the short rate."

### 뜯기

대안 측정치 두 가지:

| 측정치 | 계산 | 의미 |
|--------|------|------|
| **실질 채권 수익률** | 10년 수익률 - 5년 인플레이션 전망 | 인플레이션 보정 후 진짜 수익 |
| **기간 스프레드** | 10년 수익률 - 단기 금리 | 장단기 금리차 |

---

> "As Panel C of Table I shows, these alternative value measures produce Sharpe ratios of 0.73 and 0.55, respectively, and the t-statistics of their alphas are significant at 2.36 and 2.78."

### 뜯기

대안 측정치의 성과:

| 측정치 | 샤프 비율 | 알파 t-통계량 |
|--------|---------|-------------|
| 실질 수익률 | **0.73** | **2.36** ✓ |
| 기간 스프레드 | **0.55** | **2.78** ✓ |
| (원래 측정치) | 0.18 | 1.68 ✗ |

개선 폭이 극적이다. 0.18 → 0.73. 하지만 저자들은 **원래 측정치를 유지**한다. 왜? 데이터 마이닝 방어를 위해.

---

> "Moreover, we are able to produce even more reliable risk premia when using multiple measures of value simultaneously that diversify away measurement error and noise across the variables."

### 뜯기

**복합 측정치**(composite measure): 여러 가치 지표를 평균내면 개별 측정치의 노이즈가 상쇄되어 더 안정적인 시그널이 된다. 이건 통계학의 기본 원리 -- 독립적 노이즈원의 평균은 분산이 줄어든다.

---

> "Creating a composite average index of value measures using all three measures above produces even stronger results, where value strategies generate Sharpe ratios of 0.91 and 1.10 with t-statistics on their alphas of 4.40 and 5.48."

### 뜯기

3개 가치 측정치의 복합 평균:
- **샤프 비율**: 0.91, 1.10
- **알파 t-통계량**: 4.40, 5.48 (매우 높음)

원래 0.18이었던 것이 복합 지표로 **1.10까지** 올라간다. 다섯 배 이상. 이건 "단순한 측정치를 쓴 것이 보수적 선택이었다"는 주장의 강력한 뒷받침이다.

---

> "These alternative measures of value also blend nicely with our original measure for momentum, where, in each case, the 50/50 value/momentum combination portfolios also improve with these alternative measures."

### 뜯기

대안 가치 측정치를 쓰더라도 모멘텀과의 **음의 상관** 및 **조합 효과**가 유지되고 심지어 개선된다. 가치와 모멘텀의 상보적 관계가 측정 방법에 의존하지 않는다.

---

> "Hence, our use of single, simple, and uniform value and momentum measures may understate the true returns to these strategies in each asset class."

### 뜯기

핵심 메시지: **이 논문의 결과는 과소추정(understate)일 가능성이 높다.** 더 정교한 측정치를 쓰면 더 좋아진다.

---

> "Nevertheless, we stick with these simple measures to be conservative and to mitigate data mining concerns, even though, in the case of bonds, the results appear to be insignificant with such simple measures."

### 뜯기

그럼에도 **단순한 측정치를 고수**한다. 채권에서 결과가 유의하지 않게 나오는 대가를 감수하면서까지. 이건 연구자의 **지적 정직성(intellectual honesty)**을 보여주는 부분이다.

---

> "In real world implementations, data mining worries may be weighed against the potential improvements from having multiple (and perhaps better) measures of value and momentum, if for no other reason than to diversify away measurement error or noise across variables."

### 뜯기

현실 투자에서는 이 트레이드오프가 달라진다. 학술 논문에서는 보수적 접근이 미덕이지만, 실제 펀드에서는 더 나은 시그널을 쓰는 것이 합리적.

---

> "Israel and Moskowitz (2012) show, for instance, how other measures of value and momentum can improve the stability of returns to these styles in equities."

### 뜯기

**Israel & Moskowitz (2012)**가 주식에서 다양한 측정치가 수익의 안정성을 개선함을 보여준다. 이건 AQR이 실제 운용에서 **복합 시그널**을 쓴다는 간접적 시사점이기도 하다.

---

> "Most practical implementations use a variety of measures for a given style. In fact, we set out to examine value and momentum in eight different markets and asset classes using a single uniform measure for each. Although we find positive returns to value and momentum in each asset class, these returns are not always significant. In particular, our weakest results using the current measures of value and momentum pertain to bonds, which do not produce statistically significant premia."

### 뜯기

요약: 실무에서는 다양한 측정치를 복합적으로 사용. 이 논문은 의도적으로 단일 측정치만 사용. 그 결과 채권이 가장 약하다.

---

> "However, as shown in Table I, Panel C, the returns can be vastly improved using other measures of value and momentum, and taking a composite average index of measures for value and momentum produces even more stable and reliable results."

### 뜯기

Table I Panel C의 결과를 다시 상기시킨다. 단일 → 복합으로 가면 결과가 "vastly improved" -- **크게 개선**된다.

---

> "Hence, our use of simple, uniform value and momentum measures may understate the true returns to these strategies."

### 뜯기

다시 한번 핵심: **과소추정일 가능성**. 반복은 의도적이다. 독자에게 이 점을 확실히 각인시키려는 것.

---

> "The literature on realistic implementation of these strategies is still young, and the list of choices to make when moving from an academic study like ours to implementing these strategies in practice is long."

### 뜯기

학술 연구 → 실전 구현 사이의 간극을 인정한다. 이 분야의 연구가 아직 초기 단계라는 솔직한 평가.

---

> "But current evidence, research, and practical experience point to the effects we study being highly applicable to real world portfolios."

### 뜯기

하지만 현재까지의 증거, 연구, 실무 경험 모두 **현실 세계에 적용 가능하다**고 가리킨다. "현재 증거", "연구", "실무 경험" -- 세 가지 출처를 모두 동원한 주장.

---

> "Consistent with this conjecture, as shown in Table VI, our simple value and momentum global factors capture a sizeable fraction of the returns to hedge fund indices, which suggests that hedge funds are engaged in similar or highly correlated strategies globally."

### 뜯기

**이 문단의 마지막이자 Section V.F의 클라이맥스 문장이다.**

Table VI에서 보여준 것: 이 논문의 단순한 글로벌 가치/모멘텀 팩터가 **헤지펀드 인덱스 수익률의 상당 부분을 설명**한다. 

이것이 뜻하는 바: 실제 헤지펀드들이 **이 논문과 비슷한 전략**(또는 높은 상관이 있는 전략)을 전 세계적으로 운용하고 있다. 학술 논문의 "종이 위 포트폴리오"가 현실의 펀드와 닮았다는 것은, **이 전략이 현실에서 작동한다는 간접 증거**다.

동시에 위험한 시사점도 있다: 많은 헤지펀드가 비슷한 전략을 쓴다면, **혼잡(crowding)** 위험이 있다. 모두 같은 방향으로 움직이면, 한쪽이 무너질 때 연쇄 붕괴가 일어날 수 있다 -- 1998년 LTCM 사태처럼.

> 📚 **더 깊이**: [ch13 거래 비용과 실행](../chapters/ch13-transaction-costs.md) -- 실전 구현의 모든 선택지

---

## G. Evolution over Time (시간에 따른 변화, p.979~981)

> "As the hedge fund industry has grown and more capital has been devoted to these strategies, it is interesting to consider what effect, if any, such activity has on the efficacy of value and momentum strategies."

### 뜯기

새로운 질문이 등장한다: **헤지펀드가 커지면서 가치/모멘텀의 효과가 약해졌는가?**

이건 금융학의 근본 질문이다. 시장 이상현상(anomaly)이 발견되면:
1. 많은 투자자가 그 전략을 따라한다
2. 돈이 몰리면 기회가 줄어든다
3. 결국 이상현상이 사라진다

이걸 **차익거래의 역설**이라고 한다: 이상현상을 발견하고 알리면, 바로 그 행위가 이상현상을 없앤다.

---

> "While a complete analysis of this question is beyond the scope of this paper, we offer a couple of results perhaps worthy of future investigation."

### 뜯기

다시 면책 조항. 완전한 분석은 아니고, 향후 연구를 위한 예비 결과만 제시한다.

---

> "Table VII reports the Sharpe ratios and correlations among the value and momentum strategies over the first and second halves of the sample period -- 1972 to 1991 and 1992 to 2011."

### 뜯기

표본을 반으로 나눠서 비교한다. 1972~1991 (전반) vs 1992~2010 (후반). 약 20년씩.

---

### Table VII, Panel A: 시간에 따른 샤프 비율과 상관 변화

이 표가 Section V의 핵심이다. 모든 숫자를 하나하나 뜯는다.

#### 표 구조

Panel A는 6개 열:
- **앞 3열**: 샤프 비율 (Value, Momentum, 50/50 Combination)
- **뒤 3열**: 상관 (ρ(Val,Val), ρ(Mom,Mom), ρ(Val,Mom))

여기서:
- **ρ(Val,Val)**: 가치 전략들 간의 자산군 간 평균 상관. "미국 주식 가치와 일본 주식 가치가 얼마나 같이 움직이나"
- **ρ(Mom,Mom)**: 모멘텀 전략들 간의 자산군 간 평균 상관
- **ρ(Val,Mom)**: 가치와 모멘텀 간의 평균 상관 (음수가 예상됨)

#### 전반 vs 후반

|  | Value SR | Mom SR | Combo SR | ρ(Val,Val) | ρ(Mom,Mom) | ρ(Val,Mom) |
|--|---------|--------|----------|-----------|-----------|-----------|
| **1st half (1972-1991)** | 0.78 | 0.90 | 1.40 | 0.31 | 0.46 | -0.44 |
| **2nd half (1992-2010)** | 0.68 | 0.71 | 1.43 | 0.71 | 0.77 | -0.63 |

**숫자별 해석**:

**샤프 비율 변화**:
- 가치: 0.78 → 0.68. 약간 하락했지만 여전히 높다. 0.68이면 대부분의 액티브 펀드보다 낫다.
- 모멘텀: 0.90 → 0.71. 역시 하락. 모멘텀이 가치보다 더 많이 떨어졌다.
- **조합: 1.40 → 1.43**. 거의 **변하지 않았다!** 이건 놀라운 결과다.

**왜 조합은 안 변했나?** 개별 전략의 샤프가 떨어진 만큼, 음의 상관이 **더 강해져서** 분산 효과가 커졌기 때문이다.

**상관 변화**:
- ρ(Val,Val): 0.31 → 0.71. **두 배 이상 증가**. 전 세계 가치 전략들이 후반부에 훨씬 더 같이 움직인다.
- ρ(Mom,Mom): 0.46 → 0.77. 모멘텀도 마찬가지로 상관 급증.
- ρ(Val,Mom): -0.44 → -0.63. 음의 상관이 **더 강해졌다**. 가치와 모멘텀이 후반부에 더 반대로 움직인다.

**이 패턴이 의미하는 것**:

```
전반(1972-1991): 각 시장이 비교적 독립적, 가치/모멘텀 상관 보통
후반(1992-2010): 전 세계가 하나로 연결, 가치/모멘텀 상관 급증
────────────────────────────────────────────────────────
해석: 글로벌 차익거래자(헤지펀드)의 참여 증가?
```

---

> "As the first row of Table VII, Panel A shows, the Sharpe ratios to both value and momentum have declined slightly over time."

### 뜯기

원문이 "declined slightly"라고 표현한다. 0.78→0.68, 0.90→0.71. 이걸 "약간 하락"이라고 할 수 있는 건, 여전히 경제적으로 의미 있는 수준이기 때문이다.

---

> "In addition, their correlations across markets have increased over time -- the average correlation among value strategies has risen from 0.31 to 0.71 and among momentum strategies has risen from 0.46 to 0.77."

### 뜯기

상관의 급증이 가치와 모멘텀 모두에서 나타난다. 0.31→0.71은 **2.3배 증가**, 0.46→0.77은 **1.7배 증가**. 이건 "약간 증가"가 아니라 **구조적 변화**다.

**왜 상관이 증가했을까?**
1. **세계화**: 자본 이동이 자유로워지면서 시장 간 연결 강화
2. **동일 플레이어**: 같은 글로벌 헤지펀드들이 여러 시장에서 동시에 같은 전략 실행
3. **정보 확산**: 학술 연구 결과가 알려지면서 더 많은 투자자가 같은 전략 채택

---

> "However, the correlation between value and momentum has declined from -0.44 to -0.63, and, as a result, the Sharpe ratio of the combination of value and momentum has not changed much over time, since the increased correlation across markets is being offset by the more negative correlation between value and momentum."

### 뜯기

이것이 **이 섹션의 핵심 통찰**이다:

| 변화 | 효과 | 조합 SR에 미치는 영향 |
|------|------|---------------------|
| 개별 SR 하락 (0.78→0.68 등) | 나쁨 | ↓ |
| 같은 스타일 간 상관 증가 (0.31→0.71 등) | 나쁨 (분산 효과 감소) | ↓ |
| 가치-모멘텀 간 음의 상관 강화 (-0.44→-0.63) | 좋음 (분산 효과 증가) | ↑ |
| **순 효과** | | **1.40 → 1.43 (불변)** |

세 가지 변화가 정확히 상쇄된다. 이건 우연의 일치인가, 아니면 구조적 이유가 있는가?

구조적 해석: 차익거래자가 참여하면 → 같은 전략을 쓰는 사람이 늘어나면서 자산군 간 상관 증가 → 동시에 같은 투자자가 가치와 모멘텀을 동시에 운용하면서 둘의 음의 상관도 강화 → 개별 전략의 수익은 줄지만 조합 효과는 유지.

---

> "These results may be consistent with increased participation of arbitrageurs driving up correlations among value and momentum strategies globally."

### 뜯기

저자들은 **신중하게** 해석한다. "may be consistent with" -- "~와 일치할 수 있다". 단정하지 않는다.

차익거래자 참여 증가 → 상관 증가라는 가설은 직관적이다. 같은 신호(가치, 모멘텀)에 반응하는 투자자가 전 세계적으로 늘어나면, 그들의 거래가 시장 간 공변동을 만들어낸다.

---

#### LTCM 분기점: Pre/Post 08/1998

> "The next row of Table VII, Panel A repeats the same analysis, splitting the sample prior to and after August 1998, which is roughly when the funding crisis peaked following the collapse of Long Term Capital Management (LTCM)."

### 뜯기

이번에는 1998년 8월을 기준으로 나눈다. 왜 이 시점인가?

**1998년 8월 -- LTCM 위기**:
- Long-Term Capital Management(LTCM)은 노벨상 수상자 두 명(Merton, Scholes)이 참여한 헤지펀드
- 러시아 디폴트를 계기로 전 세계 유동성이 급격히 경색
- LTCM이 거대한 손실을 입고 붕괴 직전까지 감
- 미 연방준비제도가 월스트리트 주요 은행들을 모아 긴급 구제
- 이 사건이 **글로벌 유동성 위기의 원형**이 됨

|  | Value SR | Mom SR | Combo SR | ρ(Val,Val) | ρ(Mom,Mom) | ρ(Val,Mom) |
|--|---------|--------|----------|-----------|-----------|-----------|
| **Pre-08/1998** | 0.68 | 1.02 | 1.49 | 0.16 | 0.43 | -0.51 |
| **Post-08/1998** | 0.75 | 0.72 | 1.39 | 0.64 | 0.71 | -0.55 |

**숫자별 해석**:

**상관의 급변이 가장 눈에 띈다**:
- ρ(Val,Val): 0.16 → 0.64. **4배 증가**. 1998년 이전에는 전 세계 가치 전략들이 거의 독립적이었다(0.16). 이후에는 강하게 연결(0.64).
- ρ(Mom,Mom): 0.43 → 0.71. 역시 큰 증가.
- ρ(Val,Mom): -0.51 → -0.55. 약간만 변화.

**해석**: 1998년 LTCM 위기가 **구조적 전환점**이었다. 이 사건 이후:
1. 레버리지 사용에 대한 규제/인식 변화
2. 리스크 관리 시스템 도입 확산
3. 글로벌 펀드의 참여 증가로 시장 간 연결 강화

---

> "The correlation among value strategies is much higher after August 1998 (0.16 pre-1998 vs. 0.64 post-1998), and the correlation among momentum strategies is also higher after 1998 (0.43 vs. 0.71)."

### 뜯기

원문이 숫자를 직접 반복한다. 이 변화의 크기가 중요하다는 저자들의 판단.

---

#### 유동성 환경별 분석

> "The next three rows of Table VII, Panel A report the same statistics for periods of worsening and improving funding liquidity, defined as negative and positive funding liquidity shocks, and are split separately into pre- and post-1998."

### 뜯기

Table III에서 정의한 유동성 충격을 사용해 표본을 나눈다:
- **유동성 악화(Worsening)**: 펀딩 유동성 충격이 음(-)인 시기
- **유동성 개선(Improving)**: 펀딩 유동성 충격이 양(+)인 시기

|  | Value SR | Mom SR | Combo SR | ρ(Val,Val) | ρ(Mom,Mom) | ρ(Val,Mom) |
|--|---------|--------|----------|-----------|-----------|-----------|
| **Worsening liquidity** | 0.95 | 0.57 | 1.36 | 0.54 | 0.72 | -0.53 |
| **Improving liquidity** | 0.59 | 0.87 | 1.45 | 0.77 | 0.79 | -0.56 |

**가치와 모멘텀의 대칭적 반응**:

- 유동성 악화 시: **가치 강(0.95)**, 모멘텀 약(0.57)
- 유동성 개선 시: 가치 약(0.59), **모멘텀 강(0.87)**

이건 Section III의 유동성 리스크 분석과 정확히 일치한다. 유동성이 나빠지면 가치주(싼 주식, 유동성 프리미엄이 높은 주식)가 더 높은 보상을 받고, 모멘텀(혼잡한 포지션)은 청산 압력을 받아 성과가 떨어진다.

**조합의 면역성**: 1.36 vs 1.45. 유동성 환경에 관계없이 조합 샤프가 높게 유지된다. 가치와 모멘텀이 유동성 충격에 **반대 방향**으로 반응하기 때문이다.

---

#### 1998년 전후 x 유동성 환경 (4분할)

|  | Value SR | Mom SR | Combo SR | ρ(Val,Val) | ρ(Mom,Mom) | ρ(Val,Mom) |
|--|---------|--------|----------|-----------|-----------|-----------|
| **Worsening liq (pre-1998)** | 1.10 | 1.00 | 1.76 | 0.40 | 0.59 | -0.30 |
| **Improving liq (pre-1998)** | 1.09 | 1.27 | 2.04 | 0.36 | 0.49 | -0.29 |
| **Worsening liq (post-1998)** | 0.85 | 0.19 | 0.88 | 0.65 | 0.81 | -0.71 |
| **Improving liq (post-1998)** | 0.28 | 0.77 | 1.07 | 0.87 | 0.87 | -0.65 |

이 4분할 표가 **Section V에서 가장 풍부한 이야기**를 담고 있다.

**1998년 이전**:
- 유동성 환경에 **거의 무관**: 가치 1.10 vs 1.09, 모멘텀 1.00 vs 1.27
- 상관도 낮고 안정적: ρ(Val,Val) 0.40 vs 0.36
- 조합 샤프가 극히 높음: 1.76, **2.04**

1998년 이전에는 "유동성이 좋든 나쁘든, 가치도 모멘텀도 잘 된다." 시장이 아직 덜 연결되어 있고, 차익거래자가 적어서 유동성 환경의 영향이 미미했다.

**1998년 이후 -- 극적 변화**:
- 유동성 환경에 **극도로 민감**:
  - 가치: 유동성 악화 시 **0.85** vs 개선 시 **0.28** (3배 차이!)
  - 모멘텀: 유동성 악화 시 **0.19** vs 개선 시 **0.77** (4배 차이!)
- 상관이 전반적으로 높음: ρ(Val,Val) 0.65~0.87

**왜 1998년 이후에 유동성 민감도가 폭발했는가?**

이건 Section III의 이론적 프레임워크와 직결된다:
1. LTCM 이후 글로벌 헤지펀드가 급성장
2. 이들이 레버리지를 사용해 가치/모멘텀 전략 운용
3. 유동성이 풍부할 때: 레버리지 ↑ → 포지션 확대 → 수익 정상
4. 유동성이 경색될 때: 레버리지 ↓ → 강제 청산 → 모멘텀 붕괴, 가치 급등(평균 회귀 가속)

**모멘텀의 0.19 (post-1998, worsening)** -- 이건 거의 제로에 가까운 샤프다. 유동성 위기 시 모멘텀 전략이 사실상 **무력화**된다는 뜻이다. 2008년 금융위기 때 모멘텀 전략이 참담한 손실을 기록한 것과 일치한다.

**가치의 0.28 (post-1998, improving)** -- 유동성이 좋을 때 가치 전략이 부진한 이유: 유동성이 풍부하면 위험 자산 선호(risk-on) → 비싼 성장주가 더 잘 나감 → 가치주 상대적 부진.

---

> "Consistent with our previous regression results in Table IV, value strategies do worse when liquidity improves and momentum strategies do worse when liquidity declines, but these patterns appear only after 1998."

### 뜯기

Table IV의 회귀 결과를 확인: 가치↔유동성 악화, 모멘텀↔유동성 개선. 하지만 이 패턴은 **1998년 이후에만** 나타난다. 1998년 이전에는 유동성과 전략 성과의 관계가 거의 없다.

---

> "Prior to the financial crisis of 1998, funding liquidity shocks seem to have little impact on value or momentum strategies."

### 뜯기

1998년 이전: 유동성 충격의 영향이 미미. 위 표에서 확인 -- pre-1998 시기에는 유동성 악화/개선에 따른 차이가 거의 없다.

---

> "After 1998, however, value generates a Sharpe ratio of 0.85 during periods of worsening liquidity, but only 0.28 when liquidity improves. Conversely, momentum produces a Sharpe ratio of 0.19 when liquidity worsens, but a Sharpe ratio of 0.99 when liquidity improves."

### 뜯기

원문이 핵심 숫자를 직접 나열한다:

| 전략 | 유동성 악화 | 유동성 개선 | 차이 |
|------|-----------|-----------|------|
| **가치** | **0.85** | 0.28 | 가치는 위기에 강하다 |
| **모멘텀** | 0.19 | **0.99** | 모멘텀은 호황에 강하다 |

(주: 원문에서 모멘텀 유동성 개선 시 숫자를 0.99로 언급하는데, Table의 Improving liquidity (post-1998) 행에서 Mom SR은 0.77이다. 원문 본문의 0.99는 추가 조정이나 반올림 차이일 수 있으나, Table VII의 공식 숫자는 0.77이다.)

가치와 모멘텀이 **정확히 반대** 방향으로 유동성에 반응한다. 이것이 둘의 **상보성(complementarity)**의 근원이다.

---

> "The 50/50 value/momentum combination is immune to liquidity risk, even after 1998."

### 뜯기

**"immune"** -- 면역. 강한 표현이다. 50:50 조합의 샤프:
- Post-1998 유동성 악화: 0.88
- Post-1998 유동성 개선: 1.07

완벽한 면역은 아니지만(0.88 vs 1.07), 개별 전략의 극단적 차이(0.19 vs 0.77)에 비하면 **대단히 안정적**이다.

이건 포트폴리오 이론의 교과서적 예시: 음의 상관이 있는 두 양의 수익 자산을 조합하면 위험이 극적으로 줄어든다.

> 📚 **더 깊이**: [ch06 1998 LTCM 위기](../chapters/ch06-crisis-1998.md) -- LTCM이 왜 구조적 전환점인지

---

### Table VII, Panel B: 조건부 상관 회귀 분석

> "Panel B of Table VII examines more formally how value and momentum correlations change over time and with liquidity shocks by running time-series regressions in which the dependent variable is the cross product of monthly returns on the various strategies to proxy for time-varying correlations."

### 뜯기

Panel B는 Panel A의 직관을 **회귀 분석**으로 공식화한다.

**방법론**: 시계열 회귀에서 종속변수 = 각 전략 수익률의 **교차곱(cross product)**. 예를 들어 ρ(Val,Val)_t를 추정하려면, 시점 t에서 i번째 시장의 가치 수익률과 k번째 시장의 가치 수익률을 곱한다: r^{Val}_{i,t} × r^{Val}_{k,t}. 이 곱의 평균이 그 시점의 **조건부 상관**을 대리(proxy)한다.

**독립변수**:
- 시간 트렌드(time trend)
- 경기침체 더미(recession)
- 유동성 충격(liquidity shocks)
- (추가 분석) Post-1998 더미, 유동성×Post-1998 교호작용

---

#### Panel B 결과: Post-1998 미포함 (처음 3열)

| 독립변수 | ρ(Val,Val) | ρ(Mom,Mom) | ρ(Val,Mom) |
|----------|-----------|-----------|-----------|
| **Time trend** | 0.0067 (2.21) | 0.0181 (3.26) | -0.0320 (-4.22) |
| **Recession** | 0.0828 (1.88) | 0.0971 (2.31) | 0.0195 (0.31) |
| **Liquidity shocks** | 0.0131 (0.98) | 0.0519 (2.58) | -0.0303 (-1.62) |

괄호 안은 **t-통계량**. 절대값 2.0 이상이면 5% 수준에서 통계적으로 유의.

**해석**:

**시간 트렌드**: 
- ρ(Val,Val)에서 0.0067 (t=2.21) -- 유의. 매 시점마다 가치 전략 간 상관이 0.0067씩 증가.
- ρ(Mom,Mom)에서 0.0181 (t=3.26) -- 매우 유의. 모멘텀 전략 간 상관의 시간 추세가 가치보다 가파르다.
- ρ(Val,Mom)에서 -0.0320 (t=-4.22) -- 매우 유의. 가치-모멘텀 간 음의 상관이 시간이 갈수록 **더 음**으로 간다.

→ 시간이 흐르면서 같은 스타일 내 상관은 증가, 스타일 간 음의 상관은 강화. Panel A에서 본 패턴의 공식적 확인.

**경기침체**:
- ρ(Val,Val)에서 0.0828 (t=1.88) -- 경계 수준. 경기침체 시 가치 전략 간 상관이 증가하는 경향.
- ρ(Mom,Mom)에서 0.0971 (t=2.31) -- 유의. 경기침체 시 모멘텀 전략 간 상관 증가.
- ρ(Val,Mom)에서 0.0195 (t=0.31) -- 비유의. 경기침체가 가치-모멘텀 간 상관에는 영향 없음.

→ 경기침체는 같은 스타일 내 상관만 높인다. 위기 시 "동조화" 현상.

**유동성 충격**:
- ρ(Val,Val)에서 0.0131 (t=0.98) -- 비유의.
- ρ(Mom,Mom)에서 0.0519 (t=2.58) -- 유의! 유동성 충격이 모멘텀 전략 간 상관을 높인다.
- ρ(Val,Mom)에서 -0.0303 (t=-1.62) -- 경계 수준. 유동성 충격이 가치-모멘텀 간 음의 상관을 강화하는 경향.

→ 유동성 충격이 특히 **모멘텀 전략들의 동조화**에 영향. 이건 유동성 경색 시 모멘텀 전략들이 동시에 강제 청산되는 메커니즘과 일치.

---

> "The first three columns of Table VII, Panel B show that the average correlation among value and momentum strategies across markets and asset classes has been significantly increasing over time and the correlation between value and momentum is significantly more negative over time."

### 뜯기

원문의 요약: 시간 트렌드 계수가 유의하다. 같은 스타일 내 상관 ↑, 스타일 간 음의 상관 ↓(더 음으로).

---

> "Recessions increase the correlation among both value and momentum strategies globally, controlling for the time trend."

### 뜯기

경기침체 더미가 유의: 시간 트렌드를 통제한 후에도, 경기침체 시 상관이 추가적으로 증가.

---

> "Liquidity shocks also appear to significantly increase correlations among momentum strategies, controlling for the time trend and recessions."

### 뜯기

유동성 충격 → 모멘텀 상관 증가. 시간 트렌드와 경기침체를 통제한 후에도. 이건 유동성이 모멘텀 전략의 공변동을 설명하는 **독립적 요인**이라는 증거.

---

#### Panel B 결과: Post-1998 포함 (마지막 3열)

| 독립변수 | ρ(Val,Val) | ρ(Mom,Mom) | ρ(Val,Mom) |
|----------|-----------|-----------|-----------|
| **Time trend** | -0.0011 (0.20) | 0.0045 (0.52) | -0.0197 (-1.37) |
| **Recession** | 0.0823 (2.05) | 0.0938 (2.30) | 0.0206 (0.34) |
| **Liquidity shocks** | 0.0458 (1.80) | -0.0048 (-0.11) | -0.0717 (-1.64) |
| **Post-08/1998** | 0.1212 (1.70) | 0.2136 (1.82) | -0.1928 (-0.99) |
| **Liquidity × Post-1998** | -0.0379 (-1.20) | 0.0929 (2.11) | 0.0161 (0.34) |

**이 열들이 핵심적으로 중요한 이유**:

**시간 트렌드가 사라진다!**
- ρ(Val,Val): 0.0067 (t=2.21) → **-0.0011 (t=0.20)**. 완전히 비유의.
- ρ(Mom,Mom): 0.0181 (t=3.26) → **0.0045 (t=0.52)**. 완전히 비유의.
- ρ(Val,Mom): -0.0320 (t=-4.22) → **-0.0197 (t=-1.37)**. 비유의.

**의미**: Post-1998 더미를 넣으면 시간 트렌드가 사라진다. 즉, 앞선 분석에서 "시간이 갈수록 상관이 증가한다"고 나온 것은 사실 **점진적 추세가 아니라 1998년의 구조적 단절(structural break)**이었다.

비유하면: 처음에는 "매년 기온이 조금씩 오르고 있다"고 생각했는데, 자세히 보니 "1998년에 갑자기 올랐고 그 이후로 높은 수준에서 유지"였던 것.

**Post-1998 더미의 계수**:
- ρ(Val,Val): 0.1212 (t=1.70) -- 경계 수준이지만, 방향은 명확. 1998년 이후 가치 상관이 0.12 점프.
- ρ(Mom,Mom): 0.2136 (t=1.82) -- 경계 수준. 모멘텀 상관이 0.21 점프. 더 큰 변화.
- ρ(Val,Mom): -0.1928 (t=-0.99) -- 비유의. 가치-모멘텀 음의 상관의 강화는 1998년과 무관할 수 있음.

**유동성 × Post-1998 교호작용**:
- ρ(Mom,Mom): **0.0929 (t=2.11)** -- 유의! 유동성 충격이 모멘텀 상관에 미치는 영향이 1998년 이후에 **더 강해졌다**.

이것은 "유동성 충격 → 모멘텀 동조화" 메커니즘이 1998년 이후의 현상임을 보여준다. LTCM 이후 레버리지와 유동성의 중요성이 구조적으로 달라진 것.

---

> "However, the last three columns repeat the regressions adding a post-1998 dummy variable and an interaction between the post-1998 dummy and liquidity shocks."

### 뜯기

분석 설계를 설명. Post-1998 더미와 교호작용항을 추가한 확장 회귀.

---

> "Rather than a time trend, the post-1998 dummy seems to be driving any correlation changes, and the impact of liquidity shocks on correlations also appears to be exclusively a post-1998 phenomenon."

### 뜯기

**이 문장이 Panel B 전체의 결론이다.** 두 가지 핵심 발견:

1. **시간 트렌드가 아니라 1998년 더미가 상관 변화를 설명** -- 점진적 변화가 아닌 구조적 단절
2. **유동성 충격의 영향도 1998년 이후에만 존재** -- 1998년 이전에는 유동성이 상관에 영향을 미치지 않았음

---

> "These results are consistent with an increase in the importance of liquidity risk on the efficacy of these strategies following the events of August 1998 that appear to be more important than any time trend on the increasing popularity of value and momentum strategies among leveraged arbitrageurs."

### 뜯기

해석: LTCM 사태가 **유동성 리스크의 중요성을 구조적으로 변화**시켰다. 레버리지를 사용하는 차익거래자들 사이에서 가치/모멘텀의 인기가 높아지는 추세보다, 1998년 사건 자체가 더 중요하다.

**"leveraged arbitrageurs"** -- 레버리지를 쓰는 차익거래자, 즉 헤지펀드. LTCM 사태는 이들의 행동 패턴을 영구적으로 바꿨다. 더 많은 리스크 관리, 더 빠른 포지션 청산, 그리고 역설적으로 더 높은 동조화.

---

> **각주 20**: "Israel and Moskowitz (2012) examine the relation between size, value, and momentum profitability and aggregate trading costs and institutional investment over time. They find little evidence that the returns to these strategies vary with either of these variables."

### 뜯기

Israel & Moskowitz (2012)는 다른 각도에서 접근: 시간에 따른 집계 거래 비용과 기관 투자 증가가 전략 수익에 영향을 미치는지 검토. 결과: **영향 없음**.

이건 "차익거래자가 늘어나면 이상현상이 사라진다"는 가설에 대한 **반론**이다. 최소한 전체 표본 수준에서는, 기관 투자 증가가 가치/모멘텀 수익을 잠식하지 않았다.

다만 이 논문의 Table VII Panel A에서 샤프 비율이 약간 하락한 것은 사실이므로, 두 결과 사이에 약간의 긴장이 있다.

---

> "Hence, funding liquidity risk and limits to arbitrage activity may be a progressively more crucial feature of these strategies and future work may consider these issues in understanding the returns to value and momentum."

### 뜯기

**Section V의 마지막 문장이자, Section V 전체의 결론:**

**펀딩 유동성 리스크**와 **차익거래의 한계(limits to arbitrage)**가 이 전략들의 **점점 더 중요한 특징**이 되고 있으며, 향후 연구는 이 이슈를 고려해야 한다.

"limits to arbitrage" -- 차익거래의 한계. 이론적으로 차익거래자가 시장을 효율적으로 만들어야 하지만, 현실에서는 레버리지 제약, 유동성 경색, 마진 콜 등으로 차익거래에 한계가 있다. Shleifer & Vishny (1997)의 핵심 아이디어이며, 이 논문의 결과가 그 이론을 지지한다.

> 📚 **더 깊이**: [ch06 1998 LTCM 위기](../chapters/ch06-crisis-1998.md) -- LTCM과 차익거래의 한계 | [ch11 유동성 리스크 이론](../chapters/ch11-liquidity-risk.md) -- Brunnermeier & Pedersen (2009)

---

## Section V에서 배운 것

| # | 강건성 검정 | 결론 |
|---|-----------|------|
| A | 거래 비용 | 실거래 데이터 기준 비용은 이론 모형의 수십~수백분의 1. 대형주+선물=낮은 비용 |
| B | 공매도 | 롱 온리로도 절반의 수익 유지. 선물은 롱/숏 대칭. 대형 기관의 공매도 비용≈매수 비용 |
| C | 포트폴리오 구성 | 3분위, 10분위, 시그널 가중, 시총/동일 가중 모두 유사 결과 |
| D | 변동성 스케일링 | 사후 vs 사전(3년 롤링, 연2%) 동일한 결론 |
| E | 달러 vs 베타 중립 | 시장 헤징 여부가 알파에 영향 없음 |
| F | 측정치 선택 | 단순 측정치가 과소추정. 복합 지표로 대폭 개선 가능. 헤지펀드 인덱스와 높은 상관 |
| G | 시간 변화 | 개별 SR 약간 하락, 상관 급증, **조합 SR 불변**. 1998년이 구조적 전환점 |

**핵심 메시지**: 이 논문의 결과는 실행 가능하고, 다양한 조건에서 강건하며, 오히려 **보수적 추정**일 가능성이 높다. 다만 1998년 이후 유동성 리스크가 전략의 핵심 특징이 되었으며, 이것은 향후 연구의 중요한 방향을 제시한다.

---

## 여기서 멈추고 생각하기

### 🤔 추론 연습
1. **1998년 구조적 전환과 프리미엄 불변의 역설** 1998년 전후로 상관이 급변한다 — 이건 LTCM 위기가 "구조적 전환점"이라는 증거다. 헤지펀드/퀀트 펀드의 가치/모멘텀 전략 채택이 전략 간 상관을 높였을 수 있다. 만약 더 많은 투자자가 이 전략을 쓰면, 프리미엄이 줄어들어야 하는데, 샤프 비율은 거의 불변(1.40→1.43)이다. 왜? 크라우딩이 상관만 높이고 수익은 보존한다면, 위험의 원천 자체가 변하지 않았다는 뜻일 수 있다.
2. **위기 시 가치 매수, 모멘텀 매도?** 유동성 악화 시 가치 SR=0.85, 모멘텀 SR=0.19 (post-1998). 이건 "위기 때 가치를 사고 모멘텀을 팔라"는 전략 시사점인가? → 문제: 위기가 언제인지 실시간으로 모른다. 사후적으로는 완벽하지만 실시간 실행은 타이밍 리스크가 크다.

### ⚡ 비판적 사고
1. **2011년 이후의 공백** "2011년 이후에도 작동하는가?"에 대한 답이 없다. 데이터가 2011년까지인 것은 어쩔 수 없지만, 이것이 이 논문의 가장 큰 한계다. 특히 2018~2020 가치 폭락(value drawdown)을 이 프레임워크가 예측하거나 설명할 수 있었는가?
2. **AQR 실거래 데이터 의존** 거래비용 분석을 AQR 실거래 데이터에 의존한다 — 저자 3명 모두 AQR 소속/관계자다. 독립적 검증이 부족하며, 이해충돌의 여지가 있다. 다른 기관의 거래비용 데이터로 재현했을 때도 같은 결론인가?

> **다음**: [dissect-08 Conclusion 해체](dissect-08-conclusion.md) -- 논문의 최종 결론. 저자들이 자신의 발견을 어떻게 종합하고, 어떤 질문을 남기는지.
