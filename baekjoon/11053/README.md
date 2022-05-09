# [가장 긴 증가하는 부분 수열](https://www.acmicpc.net/problem/11053)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver II</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 |256 MB|

</div>

### 문제

***

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {<strong>10</strong>, <strong>20</strong>, 10, <strong>30</strong>, 20, <strong>50</strong>} 이고, 길이는 4이다.

### 입력

***

첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 A<sub>i</sub>가 주어진다. (1 ≤ A<sub>i</sub> ≤ 1,000)

### 출력

***

첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

### 예제 1

***

```
6
10 20 10 30 20 50
```

```
4
```

### 알고리즘 분류

***

* 다이나믹 프로그래밍

