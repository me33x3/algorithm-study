# [부분 문자열](https://www.acmicpc.net/problem/16916)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/11.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #ec9a00;">Gold V</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 |512 MB|

</div>

### 문제

***

문자열 S의 부분 문자열이란, 문자열의 연속된 일부를 의미한다.

예를 들어, "aek", "joo", "ekj"는 "baekjoon"의 부분 문자열이고, "bak", "p", "oone"는 부분 문자열이 아니다.

문자열 S와 P가 주어졌을 때, P가 S의 부분 문자열인지 아닌지 알아보자.

### 입력

***

첫째 줄에 문자열 S, 둘째 줄에 문자열 P가 주어진다. 두 문자열은 빈 문자열이 아니며, 길이는 100만을 넘지 않는다. 또, 알파벳 소문자로만 이루어져 있다.

### 출력

***

P가 S의 부분 문자열이면 1, 아니면 0을 출력한다.

### 예제 1

***

```
baekjoon
aek
```

```
1
```

### 예제 2

***

```
baekjoon
bak
```

```
0
```

### 예제 3

***

```
baekjoon
joo
```

```
1
```

### 예제 4

***

```
baekjoon
oone
```

```
0
```

### 예제 5

***

```
baekjoon
online
```

```
0
```

### 예제 6

***

```
baekjoon
baekjoon
```

```
1
```

### 알고리즘 분류

***

* KMP
* 문자열

