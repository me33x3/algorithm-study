# [부분배열 고르기](https://www.acmicpc.net/problem/2104)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/16.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #27e2a4;">Platinum V</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|2 초 |128 MB|

</div>

### 문제

***

크기가 N(1 ≤ N ≤ 100,000)인 1차원 배열 A[1], …, A[N]이 있다. 어떤 i, j(1 ≤ i ≤ j ≤ N)에 대한 점수는, (A[i] + … + A[j]) × min{A[i], …, A[j]}가 된다. 즉, i부터 j까지의 합에 i부터 j까지의 최솟값을 곱한 것이 점수가 된다.

배열이 주어졌을 때, 최대의 점수를 갖는 부분배열을 골라내는 프로그램을 작성하시오.

### 입력

***

첫째 줄에 정수 N이 주어진다. 다음 줄에는 A[1], …, A[N]을 나타내는 정수들이 주어진다. 각각의 정수들은 음이 아닌 값을 가지며, 1,000,000을 넘지 않는다.

### 출력

***

첫째 줄에 최대 점수를 출력한다.

### 예제 1

***

```
6
3 1 6 4 5 2
```

```
60
```

### 힌트

***

i = 3, j = 5일 때, 점수는 (6 + 4 + 5) × 4 = 60이 된다.

### 알고리즘 분류

***

* 자료 구조
* 분할 정복
* 세그먼트 트리
* 스택
