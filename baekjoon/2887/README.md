# [행성 터널](https://www.acmicpc.net/problem/2887)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/16.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #27e2a4;">Platinum V</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 |128 MB|

</div>

### 문제

***

때는 2040년, 이민혁은 우주에 자신만의 왕국을 만들었다. 왕국은 N개의 행성으로 이루어져 있다. 민혁이는 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만들려고 한다.

행성은 3차원 좌표위의 한 점으로 생각하면 된다. 두 행성 A(x<sub>A</sub>, y<sub>A</sub>, z<sub>A</sub>)와 B(x<sub>B</sub>, y<sub>B</sub>, z<sub>B</sub>)를 터널로 연결할 때 드는 비용은 min(|x<sub>A</sub>-x<sub>B</sub>|, |y<sub>A</sub>-y<sub>B</sub>|, |z<sub>A</sub>-z<sub>B</sub>|)이다.

터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.

### 입력

***

첫째 줄에 행성의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 다음 N개 줄에는 각 행성의 x, y, z좌표가 주어진다. 좌표는 -10<sup>9</sup>보다 크거나 같고, 10<sup>9</sup>보다 작거나 같은 정수이다. 한 위치에 행성이 두 개 이상 있는 경우는 없다. 

### 출력

***

첫째 줄에 모든 행성을 터널로 연결하는데 필요한 최소 비용을 출력한다.

### 예제 1

***

```
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
```

```
4
```

### 알고리즘 분류

***

* 그래프 이론
* 최소 스패닝 트리
* 정렬

