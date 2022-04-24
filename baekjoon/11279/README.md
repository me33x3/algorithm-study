# [최대 힙](https://www.acmicpc.net/problem/11279)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver II</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 (추가 시간 없음)  (하단 참고)|256 MB|

</div>

### 문제

***

널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

1. 배열에 자연수 x를 넣는다.
2. 배열에서 가장 큰 값을 출력하고, <span style="line-height:1.6em">그 값을 배열에서 제거한다. </span>

<span style="line-height:1.6em">프로그램은 처음에 비어있는 배열에서 시작하게 된다.</span>

### 입력

***

첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 자연수는 2<sup>31</sup>보다 작다.

### 출력

***

입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.

### 예제

***

|입력|출력|
|:---|:---|
|13<br/>0<br/>1<br/>2<br/>0<br/>0<br/>3<br/>2<br/>1<br/>0<br/>0<br/>0<br/>0<br/>0|0<br/>2<br/>1<br/>3<br/>2<br/>1<br/>0<br/>0|

### 알고리즘 분류

***

* 자료 구조
* 우선순위 큐

### 시간 제한

***

* Java 8: 2 초
* Java 8 (OpenJDK): 2 초
* Java 11: 2 초
* Kotlin (JVM): 2 초

