# [트리의 부모 찾기](https://www.acmicpc.net/problem/11725)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver II</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 |256 MB|

</div>

### 문제

***

루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

### 입력

***

첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

### 출력

***

첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

### 예제

***

|입력|출력|
|:---|:---|
|7<br/>1 6<br/>6 3<br/>3 5<br/>4 1<br/>2 4<br/>4 7|4<br/>6<br/>1<br/>3<br/>1<br/>4|
|12<br/>1 2<br/>1 3<br/>2 4<br/>3 5<br/>3 6<br/>4 7<br/>4 8<br/>5 9<br/>5 10<br/>6 11<br/>6 12|1<br/>1<br/>2<br/>3<br/>3<br/>4<br/>4<br/>5<br/>5<br/>6<br/>6|

### 알고리즘 분류

***

* 너비 우선 탐색
* 깊이 우선 탐색
* 그래프 이론
* 그래프 탐색
* 트리

