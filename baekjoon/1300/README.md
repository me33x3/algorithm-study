# [K번째 수](https://www.acmicpc.net/problem/1300)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/14.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #ec9a00;">Gold II</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|2 초 |128 MB|

</div>

### 문제

***

세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.

배열 A와 B의 인덱스는 1부터 시작한다.

### 입력

***

첫째 줄에 배열의 크기 N이 주어진다. N은 10<sup>5</sup>보다 작거나 같은 자연수이다. 둘째 줄에 k가 주어진다. k는 min(10<sup>9</sup>, N<sup>2</sup>)보다 작거나 같은 자연수이다.

### 출력

***

B[k]를 출력한다.

### 예제 1

***

```
3
7
```

```
6
```

### 알고리즘 분류

***

* 이분 탐색
* 매개 변수 탐색

