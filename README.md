# BrainScience
> 학부, 석사 과정 중 수업, 과제, 흥미 등으로 조사하거나 정리/작성 뇌과학, 인지신경과학, 뉴로마케팅 자료들입니다.


## 신경과학적 방법론의 성격특질측정 활용 가능성
> 전두비대칭뇌파와 회복탄력성의 상관관계를 중심으로.

[Journal of The Korean Data Analysis Society(JKDAS)](http://www.kdas.or.kr/index.ink) 2021 08 개제 확정

### FAA(Frontal Alpha Asymmetry), 전두비대칭뇌파

![FAA_introduce_image](https://user-images.githubusercontent.com/87905878/128627231-da57e602-6a16-435e-bd98-1f4d0d994d09.png)

Figure. Procedure of extracting FAA (Imotions, 2017)


#### FAA 원리
- 인간의 좌측 전두엽의 피질과 우측 전두엽의 피질은 정서적 환경이나 반응, 조절에 따라 분리되어 개별적인 활성화 및 비활성화 양상을 보이기도 하는데, 이를 Laterality models of affect (Davidson, 1999)이라고 한다.
- 우축 전두피질의 활성화는 주로 회피동기(avoidance motivation) 혹은 부정정서와 연관되어 있으며, 좌측 전두피질의 활성화는 주로 접근동기(Approach motivation) 혹은 긍정정서와 밀접한 연관이 있다. 이러한 좌우 전두피질의 비대칭적 활성화를 통해 개인의 성향의 특징화가 가능하다고 보기도 한다(Harmon-Jones, Gable, Peterson, 2010). 
- 이러한 관점에서 뇌파 측정을 통해 좌우 전두피질의 비대칭적 활성화에 의한 좌우 전두피질에서의 alpha wave의 파워 간의 비율을 지표화 한 것을 FAA라고 부른다. 
- 이때 알파저지현상으로 인해 알파파의 파워는 해당 뇌 영역의 활성과 반비례하기 때문에(Coan, Allen, 2004), FAA는 아래의 식(1)과 같이 좌뇌전두의 알파파파워 대비 우뇌전두의 알파파 파워의 비율에 자연로그를 취해 계산한다. FAA가 낮을수록 좌측전두의 활성이 더 낮거나 우측전두의 활성이 더 높음을 의미한다.

#### FAA 연구사례
- 신경생리학적 지표연구
   * [Nusslock et al., 2011](https://doi.org/10.1037/a0022940)
   * [Pössel et al., 2008](https://doi.org/10.1016/j.biopsycho.2008.02.004)
   * [Reznik, Allen, 2018](https://doi.org/10.1111/psyp.12965)
- 정서조절연구
   * [Chung, Yoon., 2008](https://doi.org/10.22172/cogbio.2008.20.4.001)
   * [Nash, Inzlicht, McGregor., 2012](https://doi.org/10.1016/j.biopsycho.2012.05.005)


### 실험
- 실험절차: 인적사항 및 자기보고 회복탄력성 측정도구 KRQ-53에 응답, 5분간 눈을 감고 명상하도록 지시받음, 이 기간동안의 뇌파를 측정해 휴지(rest)상태의 뇌파를 측정
- 전처리 및 분석: Brain Products GmbH의 BrainAnalyzer, Python 3.7.6, numpy 1.18.1, scipy 1.4.1, SPSS Statistics 25
- 참고
   - FAA 처리 코드
   - 그래프 생성 코드


### 결과
![result_image](https://user-images.githubusercontent.com/87905878/128627246-9161aad7-15bf-479b-8914-b5ecfd225b52.png)

Fig. Correlation of FAA and resilience

![result_table](https://user-images.githubusercontent.com/87905878/128627262-bad67774-bcb9-415c-9aa4-fac5925e6d32.png)


