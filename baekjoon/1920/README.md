# [수 찾기](https://www.acmicpc.net/problem/1920)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/7.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver IV</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 |128 MB|

</div>

### 문제

***

N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

### 입력

***

첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -2<sup>31</sup> 보다 크거나 같고 2<sup>31</sup>보다 작다.

### 출력

***

M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

### 예제 1

***

```
5
4 1 5 2 3
5
1 3 7 9 5
```

```
1
1
0
0
1
```

### 알고리즘 분류

***

* 이분 탐색
* 자료 구조

