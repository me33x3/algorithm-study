# [2×n 타일링 2](https://www.acmicpc.net/problem/11727)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver III</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 |256 MB|

</div>

### 문제

***

2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×17 직사각형을 채운 한가지 예이다.

<div align="center"><img alt="" src="https://www.acmicpc.net/upload/images/t2n2122.gif" style="height:59px; width:380px"/></div>

### 입력

***

첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

### 출력

***

첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

### 예제 1

***

```
2
```

```
3
```

### 예제 2

***

```
8
```

```
171
```

### 예제 3

***

```
12
```

```
2731
```

### 알고리즘 분류

***

* 다이나믹 프로그래밍

