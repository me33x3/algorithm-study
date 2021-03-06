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

### 예제 1

***

```
7
1 6
6 3
3 5
4 1
2 4
4 7
```

```
4
6
1
3
1
4
```

### 예제 2

***

```
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
```

```
1
1
2
3
3
4
4
5
5
6
6
```

### 알고리즘 분류

***

* 너비 우선 탐색
* 깊이 우선 탐색
* 그래프 이론
* 그래프 탐색
* 트리

