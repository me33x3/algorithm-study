# [INFP 두람 ](https://www.acmicpc.net/problem/25186)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver II</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 |1024 MB|

</div>

### 문제

***

두람이의 MBTI는 INFP이다. 두람이는 친구들과 옷이 겹치는 것을 정말 싫어한다. 

어느 날 기분이 좋지 않은 두람이는 친구들과 우정 여행을 가기로 했다. 여행을 가서 두람이는 친구들과 $N$ 종류의 옷을 각자 골라 입고 다 같이 원형으로 서서 사진을 찍기로 했다. 사진을 찍는 총인원수는 옷의 총개수와 같다. 오지랖이 넓은 두람이는 사진을 찍는 모두가 이웃한 두 사람과 옷이 겹치지 않으면 행복해지기로 했다. 

과연 두람이는 행복할 수 있을까?

### 입력

***

첫째 줄에 두람이와 친구들이 입고 있는 옷의 종류의 수 $N$ ($1 \le N \le 10^5$)이 주어진다.

둘째 줄에는 종류별 옷 개수 $d_1,  d_2,  \cdots,  d_N$ ($1 \le d_i \le 10^5$)이 공백으로 구분되어 주어진다.

### 출력

***

두람이가 행복할 수 있으면<strong> </strong><span style="color:#e74c3c;"><code>Happy</code></span>를 출력하고, 행복할 수 없다면 <span style="color:#e74c3c;"><code>Unhappy</code></span>를 출력한다.

### 예제 1

***

```
5
1 5 4 1 2
```

```
Happy
```

### 예제 2

***

```
5
7 1 5 7 4
```

```
Happy
```

### 예제 3

***

```
7
1 13 2 4 1 1 1
```

```
Unhappy
```

### 노트

***

옷의 총개수는 C++의 32비트 int 자료형의 최댓값인 2,147,483,647을 초과할 수도 있다.

### 알고리즘 분류

***

* 애드 혹
* 수학
