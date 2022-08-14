# [감소하는 수](https://www.acmicpc.net/problem/1038)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/11.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #ec9a00;">Gold V</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 |512 MB|

</div>

### 문제

***

음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

### 입력

***

첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

### 출력

***

첫째 줄에 N번째 감소하는 수를 출력한다.

### 예제 1

***

```
18
```

```
42
```

### 예제 2

***

```
0
```

```
0
```

### 예제 3

***

```
500000
```

```
-1
```

### 알고리즘 분류

***

* 백트래킹
* 브루트포스 알고리즘
