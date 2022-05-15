# [서로 다른 부분 문자열의 개수](https://www.acmicpc.net/problem/11478)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver III</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 |512 MB|

</div>

### 문제

***

문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.

부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.

예를 들어, ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고, 서로 다른것의 개수는 12개이다.

### 입력

***

첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000 이하이다.

### 출력

***

첫째 줄에 S의 서로 다른 부분 문자열의 개수를 출력한다.

### 예제 1

***

```
ababc
```

```
12
```

### 알고리즘 분류

***

* 자료 구조
* 해시를 사용한 집합과 맵
* 문자열
* 트리를 사용한 집합과 맵
