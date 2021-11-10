# BrainScience
> 학부, 석사 과정 중 수업, 과제, 흥미 등으로 조사하거나 정리/작성 뇌과학, 인지신경과학, 뉴로마케팅 자료들입니다.


## FAA(Frontal Alpha Asymmetry), 전두비대칭뇌파
![FAA_introduce_image](https://user-images.githubusercontent.com/87905878/128627231-da57e602-6a16-435e-bd98-1f4d0d994d09.png)
Figure. Procedure of extracting FAA (Imotions, 2017)


### FAA 원리
- 인간의 좌측 전두엽의 피질과 우측 전두엽의 피질은 정서적 환경이나 반응, 조절에 따라 분리되어 개별적인 활성화 및 비활성화 양상을 보이기도 하는데, 이를 Laterality models of affect (Davidson, 1999)이라고 한다.
- 우축 전두피질의 활성화는 주로 회피동기(avoidance motivation) 혹은 부정정서와 연관되어 있으며, 좌측 전두피질의 활성화는 주로 접근동기(Approach motivation) 혹은 긍정정서와 밀접한 연관이 있다. 이러한 좌우 전두피질의 비대칭적 활성화를 통해 개인의 성향의 특징화가 가능하다고 보기도 한다(Harmon-Jones, Gable, Peterson, 2010). 
- 이러한 관점에서 뇌파 측정을 통해 좌우 전두피질의 비대칭적 활성화에 의한 좌우 전두피질에서의 alpha wave의 파워 간의 비율을 지표화 한 것을 FAA라고 부른다. 
- 이때 알파저지현상으로 인해 알파파의 파워는 해당 뇌 영역의 활성과 반비례하기 때문에(Coan, Allen, 2004), FAA는 그림에서의 식과 같이 좌뇌전두의 알파파파워 대비 우뇌전두의 알파파 파워의 비율에 자연로그를 취해 계산한다. FAA가 낮을수록 좌측전두의 활성이 더 낮거나 우측전두의 활성이 더 높음을 의미한다.

#### FAA 연구사례
- 신경생리학적 지표연구
   * [Nusslock et al., 2011](https://doi.org/10.1037/a0022940)
   * [Pössel et al., 2008](https://doi.org/10.1016/j.biopsycho.2008.02.004)
   * [Reznik, Allen, 2018](https://doi.org/10.1111/psyp.12965)
- 정서조절연구
   * [Chung, Yoon., 2008](https://doi.org/10.22172/cogbio.2008.20.4.001)
   * [Nash, Inzlicht, McGregor., 2012](https://doi.org/10.1016/j.biopsycho.2012.05.005)
- 광고마케팅연구
   * [Ohme et al., 2010]()
   * [Cartocci et al, 2016]()


## 신경과학적 방법론의 성격특질측정 활용 가능성
> 전두비대칭뇌파와 회복탄력성의 상관관계를 중심으로.
[Journal of The Korean Data Analysis Society(JKDAS)](https://doi.org/10.37727/jkdas.2021.23.3.1445) 2021 06 개제

### 실험
- 실험절차: 인적사항 및 자기보고 회복탄력성 측정도구 KRQ-53에 응답, 5분간 눈을 감고 명상하도록 지시받음, 이 기간동안의 뇌파를 측정해 휴지(rest)상태의 뇌파를 측정
- 전처리 및 분석: Brain Products GmbH의 BrainAnalyzer, Python 3.7.6, numpy 1.18.1, scipy 1.4.1, SPSS Statistics 25
- 참고
   - [FAA 처리 코드](https://github.com/BrainNim/BrainScience/blob/main/rest_fft_log.py)
   - [그래프 생성 코드](https://github.com/BrainNim/BrainScience/blob/main/mk_graph.py)


### 결과
![result_image](https://user-images.githubusercontent.com/87905878/128627246-9161aad7-15bf-479b-8914-b5ecfd225b52.png)

Fig. Correlation of FAA and resilience

![result_table](https://user-images.githubusercontent.com/87905878/128627262-bad67774-bcb9-415c-9aa4-fac5925e6d32.png)



## 브랜드충성도의 인지신경기제
> 광고시청시의 전두엽 비대칭 뇌파반응을 중심으로.
석사논문 주제

### 브랜드충성도(brand loyalty)
#### 개념
- 브랜드에 대한 호의적인 태도, 행동 반응 및 경향
- 소비자가 특정 브랜드에 집착하고 다른 브랜드에 비해 특정 브랜드가 차지하는 구매비율이 높으며 지속적으로 애요하려는 태도와 행동
(Engel&Blackwell, 1982 ; Jacoby, 1978)

#### 브랜드 충성도와 광고마케팅
- 기업은 브랜드 개성을 확립하고 브랜드 태도 및 애착을 개선하며 궁극적으로는 소비자들의 브랜드 충성도를 향상시키기 위해 마케팅에 상당한 노력과 자본을 투자함
- 다양성의 시장에서 세분화된 타겟을 공략하기 위해서는 브랜드 충성도가 광고태도에 미치는 영향 연구가 필요하지만 선행연구가 부족함
- 마케팅 대상을 세분화하고 그들에게 적합한 광고전략을 세우기 위해서는 광고시청시의 실시간 태도 변화를 관측할 수 있어야 함

### 뉴로마케팅(Neuro-Marketing)
#### 뉴로마케팅의 필요성
- 구매결정과정의 상당부분은 의식수준 이하의 정보처리 과정에 의해 좌우되며, 소비자의 니즈 95% 이상이 무의식적 영역에 의해 결정됨(Zaltman, 2003)
- 하지만 기존의 대다수 소비자 마케팅 조사에서는 조사참가자들의 의식을 기반으로 하는 방법론(설문조사, 인터뷰 등)을 주로 선택해옴
- 이와 같은 방법들은 소비자들이 스스로도 파악하지 못하는 무의식적 제품선호, 선택 등을 놓치기 쉬움

#### 뉴로마케팅의 정의
- 신경과학(neuro) + 마케팅(marketing)
- 시선추적, 뇌영상촬영 등의 신경과학적 방법론을 활용해 소비자의 인지신경적 반응을 측정
- 소비자 심리 및 행동의 매커니즘을 해명하고 이를 광고와 마케팅에 응용하려는 광고 마케팅 활동
(김병희, 2015)

### 실험
- 실험절차: 인적사항 및 브랜드 태도, 애착, 충성도 등을 측정하기 위한 측정도구에 응답. 각 세션의 광고Block에서 실험용 광고자극 1개와 더미 광고자극 9개를 무작위적인 순서로 시청, 이때의 뇌파를 측정. 스트룹Block에서는 직전 광고블럭에서의 영향을 환기하기 위해 스트룹과제(stroop task)를 진행. 세션은 충 2개.  
![procedure image](https://user-images.githubusercontent.com/87905878/131220928-23ba2608-4dc6-4dfb-89a9-100dc4d992f6.png)  
Fig. procedure  

- 전처리 및 분석: Brain Products GmbH의 BrainAnalyzer, Python 3.7.6, numpy 1.18.1, scipy 1.4.1, SPSS Statistics 25
- 참고
   - 실험용 광고자극: Galaxy S10, iPhone SE
   - [FAA 처리 코드](https://github.com/BrainNim/BrainScience/blob/main/rest_fft_log.py)
   - [그래프 생성 코드](https://github.com/BrainNim/BrainScience/blob/main/article_graph.ipynb)

### 결과
![result image](https://user-images.githubusercontent.com/87905878/141123899-ceb201c2-15c6-46f6-8e12-0b3f5e930518.png)  
Fig. 갤럭시에 대한 브랜드 충성도가 높은 집단 VS 낮은 집단의 갤럭시 광고 시청시 FAA  
- 14 ~ 16초 / 24 ~ 26초 / 26 ~ 28초 구간에서 집단간 차이가 유의함
  
![result image](https://user-images.githubusercontent.com/87905878/141124218-8a6121ab-6da6-4bc6-a338-6a4e5292eaf6.png)  
Fig. 갤럭시 광고시청 후 만족도 설문에서 높은점수로 응답한 집단 VS 낮은점수 집단의 갤럭시 광고 시청시 FAA
- 오히려 차이가 유의한 부분이 없음
