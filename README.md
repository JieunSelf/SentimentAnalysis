# Sentiment Analysis
## 1. 실습 소개
- 만 6~18세의 아동 및 청소년 저자의 생활문 텍스트를 대상으로 <b>긍부정 감성 분석(Sentiment Analysis)</b>을 진행함.
- 사전 기반의 감성 분석을 위해 'KNU 한국어 감성 사전(박상민 외, 2018)'을 활용함. 


## 2. corpus
- 실험 데이터 : 국립국어원 모두의 말뭉치에서 제공되는 '국립국어원 비출판물 말뭉치' 중 만 6~18세 저자의 일기와 수필글
- https://corpus.korean.go.kr/request/reausetMain.do?lang=ko
  
  
- 예시
   
```xml
<?xml version="1.0" encoding="UTF-8"?>
<SJML>
    <header>
        <fileInfo>
            <fileId>WDRW1900102137</fileId>
            <annoLevel>원시</annoLevel>
            <category>비출판물 > 일기</category>
        </fileInfo>
        <sourceInfo>
            <title>초코파이</title>
            <author id="P02137" age="6" occupation="고등학생" sex="F" submission="온라인" handwriting="No">개인글작성자</author>
        </sourceInfo>
    </header>
    <text date="20090000" subclass="null_게임">
        <p>엄마가 어제 초코파이를 사주셨다. 그래서 하나 먹으려고 했지만 엄마가 안 된다고 했다. 그 전에는 오빠 머리를 깎고 왔었다. 그 전에는 마다가스카 2를 보고 있었다. 애니메이션이 다 끝나서 집에 갔어. 그런데 오빠가 게임을 해서 내가 보고있는데 오빠가 남자캐릭터를 새로 골랐길래 내가 마법사 캐릭터도 하라고 했어. 마법사 이름을 정하고 게임을 계속하다가 나는 씻었다.</p>
    </text>
</SJML>
```

## 3. 전처리
- KSS(Korean Sentence Splitter) 라이브러리를 사용하여 문장 단위로 텍스트 분리함.
- 문장의 길이가 10글자 이하 또는 300자 이상의 문장은 제외함.
- 총 3,626개의 글에 대해 47,775개의 문장으로 분리됨.
- 형태소 분석기 <b>Mecab</b>을 활용한 토큰화(tokenization) 작업
- 토큰화된 단어 중 불용어(조사, 구두점, 감탄사 등)는 제거함.
## 4. 결과
- <b>[KNU 한국어 감성 사전](http://dilab.kunsan.ac.kr/knusl.html)</b>을 활용하여 토큰화된 단어의 감성 점수 계산함.
- 감성 어휘가 없는 경우에는 감성 점수를 0점으로 출력함.
- 만6-11세와 만12-18세의 저자로 나누어 감성 점수를 분석함.
- 분석 결과, 만6-11세의 저자는 평균 0.089점, 만12-18세의 저자는 평균 -0.066점으로 나타남(p<.05).

 | 분류 | 평균(M)    | 표준편차(SD)    |
| :---:   | :---: | :---: |
| 만 6~11세 | 0.089   | 1.007   |
| 만 12~18세 | -0.066   | 1.002   |


