# [배달](https://www.acmicpc.net/problem/1175)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/15.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #ec9a00;">Gold I</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|2 초 |128 MB|

</div>

### 문제

***

어제 선물을 모두 포장한 민식이는 이제 선물을 배달하려고 한다. 민식이가 선물을 배달할 곳은 이 문제를 읽는 사람들이 앉아 있는 교실이다. 교실은 직사각형모양이고, 모두 같은 크기의 정사각형 블록으로 나누어져 있다.

입력으로 교실의 지도가 주어진다. 각각의 정사각형 블록은 다음과 같이 4가지 종류가 있다.

* S: 지금 민식이가 있는 곳이다. 이곳이 민식이가 배달을 시작하는 곳이고 1개만 있다.  
* C: 민식이가 반드시 선물을 배달해야 하는 곳이다. 이러한 블록은 정확하게 2개 있다.  
* #: 민식이가 갈 수 없는 곳이다.  
* .: 민식이가 자유롭게 지나갈 수 있는 곳이다.

민식이가 한 블록 동서남북으로 이동하는데는 1분이 걸린다. 민식이는 네가지 방향 중 하나로 이동할 수 있으며, 교실을 벗어날 수 없다. 민식이가 선물을 배달해야 하는 곳에 들어갈 때, 민식이는 그 곳에 있는 사람 모두에게 선물을 전달해야 한다. 이 상황은 동시에 일어나며, 추가적인 시간이 소요되지 않는다.

민식이는 어느 누구도 자신을 보지 않았으면 하기 때문에, 멈추지 않고 매 시간마다 방향을 바꿔야 한다. 이 말은 같은 방향으로 두 번 연속으로 이동할 수 없다는 말이다. 민식이가 선물을 모두 배달하는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.

### 입력

***

첫째 줄에 교실의 세로 크기 N과 가로 크기 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 교실의 지도가 주어진다.

### 출력

***

첫째 줄에 민식이가 선물을 모두 배달하는데 걸리는 시간의 최솟값을 출력한다. 만약 불가능 할 때는 -1을 출력한다.

### 예제 1

***

```
2 3
SCC
...
```

```
4
```

### 예제 2

***

```
1 5
C.C.S
```

```
-1
```

### 예제 3

***

```
3 3
#.#
CSC
#.#
```

```
5
```

### 예제 4

***

```
10 7
#.#....
##...#.
C#...#.
.....#.
..#....
..#S.#.
.##..#.
###..##
..C.#.#
###.#..
```

```
24
```

### 예제 5

***

```
3 36
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#C
.................S..................
C#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
```

```
155
```

### 알고리즘 분류

***

* 너비 우선 탐색
* 그래프 이론
* 그래프 탐색
