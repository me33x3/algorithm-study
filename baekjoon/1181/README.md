# [단어 정렬](https://www.acmicpc.net/problem/1181)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/6.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver V</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|2 초 |256 MB|

</div>

### 문제

***

알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로

### 입력

***

첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

### 출력

***

조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

### 예제

***

|입력|출력|
|:---|:---|
|13<br/>but<br/>i<br/>wont<br/>hesitate<br/>no<br/>more<br/>no<br/>more<br/>it<br/>cannot<br/>wait<br/>im<br/>yours|i<br/>im<br/>it<br/>no<br/>but<br/>more<br/>wait<br/>wont<br/>yours<br/>cannot<br/>hesitate|

### 알고리즘 분류

***

* 정렬
* 문자열
