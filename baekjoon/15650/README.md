# [N과 M (2)](https://www.acmicpc.net/problem/15650)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver III</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 |512 MB|

</div>

### 문제

***

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

* 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
* 고른 수열은 오름차순이어야 한다.

### 입력

***

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

### 출력

***

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

### 예제

***

|입력|출력|
|:---|:---|
|3 1|1<br/>2<br/>3|
|4 2|1 2<br/>1 3<br/>1 4<br/>2 3<br/>2 4<br/>3 4|
|4 4|1 2 3 4|

### 알고리즘 분류

***

* 백트래킹
