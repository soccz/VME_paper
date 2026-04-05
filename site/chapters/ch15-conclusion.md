# 결론: 이 논문이 남긴 것과 남은 퍼즐

> Section VI (p.981~982)를 해체한다. 결론은 짧다 — 3개 문단. 하지만 그 안에 논문 전체의 논리가 압축되어 있다. 이 챕터를 읽고 나면 논문의 5대 공헌, 남은 퍼즐, 그리고 후속 연구 방향을 모두 설명할 수 있다.

---

## 첫째 문단: 종합 요약 — "우리가 발견한 것"

원문은 이렇게 시작한다:

> "We provide comprehensive evidence on the return premia to value and momentum strategies globally across asset classes, and uncover strong common factor structure among their returns."

한 문장에 두 가지 주장이 들어 있다:

1. **수익 프리미엄의 체계적 문서화** — 가치와 모멘텀이 전 세계, 전 자산군에서 양(+)의 초과수익을 낸다. ch10에서 본 Table I의 결과다.
2. **공통 팩터 구조(common factor structure) 발견** — 이 수익들이 서로 독립적이 아니라 함께 움직인다. ch11에서 본 Table II와 Figure 1-2의 결과다.

왜 이 두 가지가 중요한가? 개별 시장에서 가치가 작동한다는 것은 이미 알려져 있었다(Fama-French 1993). 모멘텀도 마찬가지다(Jegadeesh-Titman 1993). 하지만 **8개 자산군에서 동시에** 작동하고, 그 수익들이 **공통 요인으로 묶인다**는 것은 이 논문이 처음 보인 것이다.

### 기존 이론에 대한 도전

원문이 이어서 던지는 공격은 세 방향이다:

**첫째, 행동재무학(behavioral finance)에 대한 도전:**

> "The strong correlation structure among value and momentum strategies across such diverse asset classes is difficult to reconcile under existing behavioral theories"

행동재무 이론(Barberis, Shleifer, Vishny 1998; Daniel, Hirshleifer, Subrahmanyam 1998)은 투자자의 심리적 편향으로 가치와 모멘텀을 설명한다. 과잉반응(overreaction)이 가치를, 지연반응(underreaction)이 모멘텀을 만든다는 논리다.

문제는 이렇다: 주식시장의 개인투자자가 과잉반응한다는 것은 그럴듯하다. 하지만 원자재 선물시장의 트레이더도, 국채시장의 기관투자자도, 외환시장의 은행도 **같은 방식으로** 과잉반응하는가? 그리고 그 과잉반응이 **동시에** 일어나는가? 기존 행동재무 모형은 이 질문에 답하지 못한다. 각 시장의 투자자 구성, 제도적 구조(institutional structures), 정보 환경(information environments)이 완전히 다르기 때문이다.

**둘째, 합리적 위험 모형(rational risk-based models)에 대한 도전:**

> "the high return premium and Sharpe ratio of a global across-asset-class diversified value and momentum portfolio presents an even more daunting hurdle for rational risk-based models"

합리적 모형은 높은 수익 = 높은 위험이라고 설명한다. 가치 프리미엄이 연 4.6%라면, 그에 상응하는 위험을 져야 한다. 하지만 글로벌 50/50 조합의 샤프 비율은 **1.59**다(ch10 참조). 미국 주식시장 전체의 샤프 비율(~0.4)의 약 4배. 이 정도의 위험-수익 비율을 정당화할 수 있는 합리적 위험 요인이 무엇인지, 기존 모형으로는 설명이 안 된다.

왜 "more daunting"이라고 했는가? 기존 연구는 가치만, 또는 모멘텀만, 또는 주식만 보았다. 그 경우 샤프 비율은 0.3~0.5 수준이다. 이 정도는 합리적 모형이 어떻게든 설명할 여지가 있었다. 하지만 전 자산군을 결합하면 샤프가 1.59로 뛰어오른다 — 이것은 합리적 모형에 "더 가혹한 장애물(more daunting hurdle)"이다.

**셋째, "더 일반적인 프레임워크(more general framework)" 요청:**

> "the existence of correlated value and momentum effects in other asset classes—with their different investors, institutional structures, and information environments—argues for a more general framework"

행동재무도 안 되고, 합리적 위험도 안 되면, 무엇이 필요한가? 저자들은 답을 주지 않는다. 대신 "더 일반적인 프레임워크가 필요하다"고만 말한다. 이것은 겸손한 표현이 아니다 — **기존 금융이론 전체에 대한 도전장**이다.

왜 "더 일반적"이어야 하는가? 주식에서만 작동하는 이론은 부족하다. 원자재, 채권, 통화까지 설명해야 한다. 투자자 심리만으로도 부족하고, 위험만으로도 부족하다. 둘 다 포함하면서, 서로 다른 자산군의 투자자, 제도, 정보 환경을 관통하는 무언가가 필요하다.

---

## 둘째 문단: 유동성의 역할 — "부분적 설명"

> "We further find that exposure to funding liquidity risk provides a partial explanation for this correlation structure, especially following the funding crisis of 1998, but leaves much to be explained."

이 문장에서 핵심 단어는 세 개다: **partial**, **especially following 1998**, **leaves much**.

### "Partial" — 왜 부분적인가

ch12에서 보았듯이, 펀딩 유동성 리스크(funding liquidity risk)에 대한 노출이 가치-모멘텀 상관구조를 **일부** 설명한다. TED 스프레드, 레버리지 변화, 유동성 충격이 가치와 모멘텀 수익에 영향을 미친다. 하지만 이것이 전부가 아니다. 유동성 변수를 통제한 후에도 상당한 공통 변동(comovement)이 남는다.

### "Especially following 1998" — 왜 1998년 이후인가

1998년은 LTCM 위기의 해다(ch06 참조). 이 위기 이후 가치와 모멘텀 수익 간 상관이 급격히 높아졌다. 논문의 해석: 1998년 위기가 차익거래자(arbitrageurs)의 활동 패턴을 바꿨다. 위기 전에는 가치와 모멘텀이 비교적 독립적으로 움직였지만, 위기 후에는 같은 자금원(funding source)에 의존하는 차익거래자들이 두 전략을 동시에 운용하면서 공통 움직임이 강해졌다.

### "Leaves much to be explained" — 무엇이 남았는가

원문은 계속한다:

> "While the relation to funding liquidity risk could imply that limited arbitrage activity may contribute to the prevalence and dynamics of these phenomena, we leave the ubiquitous evidence on the efficacy of value and momentum across the diverse asset classes we study, its strong correlation structure, and intriguing dynamics related to funding risk as a challenge for future theory and empirical work to address."

이 문장은 논문에서 가장 긴 문장 중 하나다. 분해하면:

1. **유동성 리스크와의 관계** → 차익거래 활동의 제한(limited arbitrage activity)이 현상의 **지속성(prevalence)**과 **역학(dynamics)**에 기여할 수 있다
2. 하지만 세 가지를 미래 연구에 남긴다:
   - 전 자산군에서의 보편적 효과(ubiquitous evidence)
   - 강한 상관구조(strong correlation structure)
   - 펀딩 리스크와 관련된 흥미로운 역학(intriguing dynamics)

"차익거래의 한계(limits to arbitrage)"라는 개념이 여기서 핵심이다. 가치와 모멘텀이 비효율(mispricing)이라면, 차익거래자들이 이를 이용해 수익을 올리면서 비효율이 사라져야 한다. 하지만 차익거래에는 비용과 위험이 있다 — 특히 펀딩이 막히면 포지션을 유지할 수 없다. 1998년 LTCM 위기가 그 예다. 차익거래자가 포지션을 청산당하면, 비효율이 오히려 **확대**된다. 이 메커니즘이 가치와 모멘텀 프리미엄의 **지속**을 설명할 수 있다.

하지만 이것으로도 "왜 8개 자산군 전부에서 작동하는가?"는 설명되지 않는다.

---

## 셋째 문단: 글로벌 3팩터 모형 — "실용적 도구"

> "Finally, we provide a simple global three-factor model that describes a new set of 48 global across-asset-class test assets, the Fama–French portfolios, and a variety of hedge fund indices."

ch13에서 해체한 글로벌 3팩터 모형(global three-factor model)이다. 세 팩터는:

| 팩터 | 정체 |
|------|------|
| **MGKT** | 글로벌 시장 포트폴리오 |
| **MVAL** | 글로벌 가치 팩터 (전 자산군 결합) |
| **MMOM** | 글로벌 모멘텀 팩터 (전 자산군 결합) |

이 모형이 설명하는 것:
- **48개 글로벌 자산군 테스트 포트폴리오** — 이 논문이 새로 만든 자산
- **Fama-French 포트폴리오** — 기존 자산가격결정 문헌의 표준 벤치마크
- **헤지펀드 인덱스** — 실무 투자의 벤치마크

왜 "simple"이라고 강조했는가? 3개 팩터만으로 이 모든 것을 설명한다는 것이 놀랍기 때문이다. Fama-French 모형도 3팩터(시장, 가치, 규모)지만, 주식에만 적용된다. 이 논문의 3팩터는 **전 자산군**에 적용된다.

원문이 마무리하는 방향:

> "In further investigating the underlying economic sources driving value and momentum returns, we hope this simple three-factor framework can be useful for future research that is becoming increasingly concerned with pricing global assets across markets."

두 가지 메시지:

1. **근본 경제적 원천(underlying economic sources)** — 가치와 모멘텀을 만드는 근본적인 경제적 힘이 무엇인지는 아직 모른다. 유동성이 일부를 설명하지만, 더 깊은 원인이 있을 것이다.
2. **실용적 유용성** — 원인을 모르더라도, 이 3팩터 모형은 실용적으로 유용하다. 글로벌 자산의 가격결정에 관심이 늘어나는 학계에서 도구로 쓸 수 있다.

이것은 논문의 전형적인 마무리 전략이다: 이론적 답을 주지 못하더라도, **실용적 도구**를 남긴다.

---

## 이 논문의 5대 공헌

저자들이 명시적으로 정리하지는 않지만, 논문 전체와 결론을 종합하면 다섯 가지 핵심 공헌이 드러난다:

### 1. 전 자산군 수익 프리미엄의 체계적 문서화

가치 프리미엄은 Fama-French(1993)가, 모멘텀 프리미엄은 Jegadeesh-Titman(1993)이 문서화했다. 하지만 둘 다 미국 주식에 한정되었다. 이 논문은 **4개국 주식 + 국가지수 + 통화 + 채권 + 원자재**, 총 8개 자산군에서 동일한 방법론으로 체계적으로 문서화했다. "everywhere"가 논문 제목에 들어간 이유다.

### 2. 자산군 간 공동 움직임(comovement) 발견

미국 가치주가 오르는 달에 영국 가치주도, 원자재 가치 전략도, 통화 가치 전략도 같이 오른다. 이 공통 움직임은 우연이 아니다 — 통계적으로 강하고 안정적이다. 이것은 "각 시장에 독립적인 비효율이 있다"는 단순한 설명을 기각한다. 무언가 **글로벌하게 공통된 원인**이 있어야 한다.

### 3. 유동성 리스크와의 연결 (부분적)

펀딩 유동성 리스크(TED 스프레드로 측정)가 가치-모멘텀 상관구조의 일부를 설명한다. 특히 1998년 LTCM 위기 이후에 이 관계가 강해진다. 완전한 설명은 아니지만, **첫 번째 실마리**를 제공한다.

### 4. 글로벌 3팩터 모형 제안

시장, 가치, 모멘텀의 세 팩터만으로 48개 글로벌 테스트 자산의 수익률을 설명하는 간결한 모형을 제안했다. Fama-French의 주식 전용 모형을 전 자산군으로 확장한 것이다.

### 5. 기존 이론 전부에 도전

행동재무학에도, 합리적 위험 모형에도, 효율적 시장가설(EMH)에도 동시에 도전한다. 행동재무학은 자산군 간 상관을 설명 못 하고, 합리적 모형은 샤프 1.59를 정당화 못 하고, EMH는 40년간 지속되는 프리미엄 자체를 설명 못 한다.

---

## 남은 퍼즐

논문이 답을 주지 못한 질문들이 있다. 이것이 이 분야가 아직 살아있는 이유다.

### 퍼즐 1: 유동성으로 일부만 설명된다 — 나머지는?

유동성 리스크 노출을 통제한 후에도 가치-모멘텀 공통 팩터의 상당 부분이 남는다. 이 "남는 부분"이 무엇인지 모른다. 후보로는 거시경제 위험(macro risk), 감정 전염(sentiment contagion), 구조적 차익거래 한계(structural limits to arbitrage) 등이 있지만, 아직 검증되지 않았다.

### 퍼즐 2: 50/50 조합의 면역성

가치와 모멘텀을 50/50으로 결합하면 시장 위험에 대한 노출이 거의 0이 되고, 유동성 리스크 노출도 사라진다. 왜? 가치는 유동성 위기에 양(+)의 노출(위기 때 손실), 모멘텀은 음(-)의 노출이므로 상쇄된다. 하지만 **수익은 남는다**. 위험이 없는데 수익이 있다? 이것은 효율적 시장가설에 정면으로 반한다. 논문은 이 면역성을 보고하지만, 왜 이것이 가능한지 설명하지 않는다.

### 퍼즐 3: 가치의 보험 역할

가치 전략은 유동성 위기에 음(-)의 로딩을 가진다 — 유동성이 악화되면 가치 전략이 손실을 본다. 이것은 가치가 일종의 "안 좋은 시기에 돈을 잃는" 전략이라는 뜻이다. 합리적 관점에서, 나쁜 시기에 손실을 주는 자산은 **보상**(양의 프리미엄)을 받아야 한다. 그렇다면 가치 프리미엄은 유동성 위험에 대한 합리적 보상인가?

문제는 모멘텀이다. 모멘텀은 유동성에 양(+)의 로딩 — 유동성이 악화되면 모멘텀이 **이득**을 본다(일종의 보험). 보험이면 프리미엄이 음(-)이어야 한다. 하지만 모멘텀 프리미엄은 양(+)이다. 가치의 위험 프리미엄 논리와 모멘텀의 위험 프리미엄 논리가 서로 모순된다.

### 퍼즐 4: 1998년 이후 상관 급증의 원인

가치-모멘텀 상관이 1998년 LTCM 위기 이후 급격히 높아졌다. 논문의 가설: 차익거래 참여자가 늘면서 공통 자금원에 대한 의존도가 높아졌다. 하지만 이것은 **가설**일 뿐이다. 차익거래 참여 증가를 직접 측정하기 어렵고, 다른 설명(글로벌화, 정보기술 발전, 규제 변화 등)도 가능하다.

---

## 후속 연구 방향

논문이 시사하는(그리고 실제로 후속 연구가 진행된) 방향들:

### 1. 가치/모멘텀의 근본 경제적 원천

결론에서 직접 언급한 과제다: "the underlying economic sources driving value and momentum returns." 가치와 모멘텀이 왜 존재하는지에 대한 근본적 이해. 후보 이론으로는 장기 소비 위험(long-run consumption risk, Bansal-Yaron 2004), 이질적 에이전트 모형(heterogeneous agent models), 정보 비대칭(information asymmetry) 등이 있다.

### 2. 유동성과 차익거래 한계의 더 깊은 연결

유동성이 "부분적 설명"이라면, 차익거래의 한계(limits to arbitrage)가 더 정교하게 모형화되어야 한다. Brunnermeier-Pedersen(2009)의 마진 스파이럴(margin spiral) 모형이 출발점이지만, 전 자산군으로 확장해야 한다.

### 3. 시간 변화하는 리스크 프리미엄 모형

가치-모멘텀 상관이 시간에 따라 변한다(1998년 전후로 급변). 이것은 정적 모형(static model)으로는 포착 불가능하다. 리스크 프리미엄이 시간에 따라 변하는(time-varying) 동적 모형이 필요하다.

### 4. 글로벌 3팩터의 이론적 근거

논문은 경험적으로 3팩터 모형이 잘 작동한다는 것을 보였다. 하지만 **왜** 시장, 가치, 모멘텀이 세 개의 가격결정 팩터인지에 대한 이론적 근거는 없다. Fama-French 3팩터(시장, 가치, 규모)도 비슷한 비판을 받았다 — "경험적으로 작동하지만 이론적 기반이 약하다."

### 5. 다른 팩터와의 통합

이 논문은 가치와 모멘텀만 다룬다. 하지만 실무에서는 캐리(carry), 품질(quality), 저변동성(low-volatility), 규모(size) 등 다른 팩터도 사용한다. 이 팩터들도 전 자산군에서 작동하는가? 가치, 모멘텀과 어떤 관계인가? Asness 자신이 후속 연구(Asness, Frazzini, Israel, Moskowitz 2015 등)에서 이 방향을 추구한다.

---

## 이 문서 전체를 되돌아보며

### Part 0에서 배운 것이 Part 1에서 어떻게 쓰였는가

| Part 0 챕터 | 배운 것 | Part 1에서 쓰인 곳 |
|-------------|---------|-------------------|
| [ch02. 금융 기초](ch02-finance-basics.md) | 초과수익, 샤프 비율, t-통계량 | ch10의 Table I 모든 숫자를 읽는 데 |
| [ch03. 이론 전쟁](ch03-theory-wars.md) | EMH, 행동재무, 합리적 위험 | ch15(이 챕터)에서 "세 이론 모두에 도전" 이해 |
| [ch04. 가치/모멘텀 직관](ch04-val-mom-intuition.md) | 왜 싼 게 좋고, 오른 게 더 오르는가 | ch10에서 P3-P1 스프레드의 의미 |
| [ch05. 통계 도구상자](ch05-statistics-toolbox.md) | 회귀, 알파, 베타, GRS 검정 | ch11 상관분석, ch12 유동성 회귀, ch13 GRS 검정 |
| [ch06. 1998년 위기](ch06-crisis-1998.md) | LTCM 붕괴, 유동성 위기 | ch12 유동성 분석의 핵심 사건 |
| [ch07. 저자 맥락](ch07-authors-context.md) | AQR, 학계-실무 이중 정체성 | 왜 이 논문이 전 자산군을 다루는지 |

Part 0 없이 Part 1을 읽었다면, Table I의 숫자는 숫자일 뿐이다. Part 0가 있기에 **왜 그 숫자가 놀라운지**, **왜 기존 이론으로 설명이 안 되는지** 이해할 수 있다.

### 이 논문을 읽은 사람이 할 수 있는 것

1. **팩터 투자의 기본 구조를 설명**할 수 있다 — 가치, 모멘텀이 무엇이고, 왜 전 자산군에서 작동하는지
2. **포트폴리오 결합의 힘을 이해**할 수 있다 — 음의 상관을 가진 전략을 결합하면 왜 샤프가 급등하는지
3. **유동성 리스크의 역할을 설명**할 수 있다 — 펀딩 유동성이 팩터 수익에 어떻게 영향을 미치는지
4. **글로벌 자산가격결정 모형을 이해**할 수 있다 — 3팩터 모형이 무엇이고, 왜 작동하는지
5. **학술 논문의 구조를 읽을 수** 있다 — 가설, 검증, 강건성, 결론의 흐름
6. **"왜 아직 답이 없는가"를 설명**할 수 있다 — 행동재무도, 합리적 위험도, EMH도 완전한 답을 주지 못하는 이유
7. **후속 연구의 방향을 파악**할 수 있다 — 유동성, 시간 변화 프리미엄, 팩터 통합 등

---

## 다음 단계: Part 2 (부록)

Part 1의 본문 해체는 여기서 끝난다. 하지만 논문에는 부록(Appendix)과 추가 테이블이 있다. Part 2에서는:

- **Appendix의 데이터 세부사항** — 각 자산군의 정확한 데이터 출처와 구성
- **강건성 검정(robustness checks)** — 다른 기간, 다른 측정치, 다른 방법론으로도 결과가 유지되는가
- **논문 이후의 발전** — 2013년 출판 이후 가치와 모멘텀 연구가 어떻게 발전했는가

Part 1만으로도 논문의 핵심을 완전히 이해할 수 있다. Part 2는 더 깊이 들어가고 싶은 독자를 위한 것이다.
