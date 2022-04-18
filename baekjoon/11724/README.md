# [연결 요소의 개수](https://www.acmicpc.net/problem/11724)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver II</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|3 초 |512 MB|

</div>

### 문제

***

방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

### 입력

***

첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

### 출력

***

첫째 줄에 연결 요소의 개수를 출력한다.

### 예제

***

|입력|출력|
|:---|:---|
|6 5<br/>1 2<br/>2 5<br/>5 1<br/>3 4<br/>4 6|2|
|6 8<br/>1 2<br/>2 5<br/>5 1<br/>3 4<br/>4 6<br/>5 4<br/>2 4<br/>2 3|1|

### 알고리즘 분류

***

* 너비 우선 탐색
* 깊이 우선 탐색
* 그래프 이론
* 그래프 탐색

