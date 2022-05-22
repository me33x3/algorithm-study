# [친구](https://www.acmicpc.net/problem/1058)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver II</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|2 초 |128 MB|

</div>

### 문제

***

지민이는 세계에서 가장 유명한 사람이 누구인지 궁금해졌다. 가장 유명한 사람을 구하는 방법은 각 사람의 2-친구를 구하면 된다. 어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나, A와 친구이고, B와 친구인 C가 존재해야 된다. 여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다. 가장 유명한 사람의 2-친구의 수를 출력하는 프로그램을 작성하시오.

A와 B가 친구면, B와 A도 친구이고, A와 A는 친구가 아니다.

### 입력

***

첫째 줄에 사람의 수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 각 사람이 친구이면 Y, 아니면 N이 주어진다.

### 출력

***

첫째 줄에 가장 유명한 사람의 2-친구의 수를 출력한다.

### 예제 1

***

```
3
NYY
YNY
YYN
```

```
2
```

### 예제 2

***

```
3
NNN
NNN
NNN
```

```
0
```

### 예제 3

***

```
5
NYNNN
YNYNN
NYNYN
NNYNY
NNNYN
```

```
4
```

### 예제 4

***

```
10
NNNNYNNNNN
NNNNYNYYNN
NNNYYYNNNN
NNYNNNNNNN
YYYNNNNNNY
NNYNNNNNYN
NYNNNNNYNN
NYNNNNYNNN
NNNNNYNNNN
NNNNYNNNNN
```

```
8
```

### 예제 5

***

```
15
NNNNNNNNNNNNNNY
NNNNNNNNNNNNNNN
NNNNNNNYNNNNNNN
NNNNNNNYNNNNNNY
NNNNNNNNNNNNNNY
NNNNNNNNYNNNNNN
NNNNNNNNNNNNNNN
NNYYNNNNNNNNNNN
NNNNNYNNNNNYNNN
NNNNNNNNNNNNNNY
NNNNNNNNNNNNNNN
NNNNNNNNYNNNNNN
NNNNNNNNNNNNNNN
NNNNNNNNNNNNNNN
YNNYYNNNNYNNNNN
```

```
6
```

### 알고리즘 분류

***

* 브루트포스 알고리즘
* 플로이드–와샬
* 그래프 이론
* 그래프 탐색

