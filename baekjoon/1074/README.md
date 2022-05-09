# [Z](https://www.acmicpc.net/problem/1074)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/10.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver I</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|0.5 초 (추가 시간 없음) |512 MB|

</div>

### 문제

***

한수는 크기가 2<sup>N</sup> × 2<sup>N</sup>인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.

<div align="center"><img alt="" src="https://upload.acmicpc.net/21c73b56-5a91-43aa-b71f-9b74925c0adc/-/preview/" style="width: 100px; height: 99px;"/></div>

N &gt; 1인 경우, 배열을 크기가 2<sup>N-1</sup> × 2<sup>N-1</sup>로 4등분 한 후에 재귀적으로 순서대로 방문한다.

다음 예는 2<sup>2</sup> × 2<sup>2</sup> 크기의 배열을 방문한 순서이다.

<div align="center"><img alt="" src="https://upload.acmicpc.net/adc7cfae-e84d-4d5c-af8e-ee011f8fff8f/-/preview/" style="width: 250px; height: 252px;"/></div>

N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

다음은 N=3일 때의 예이다.

<div align="center"><img alt="" src="https://upload.acmicpc.net/d3e84bb7-9424-4764-ad3a-811e7fcbd53f/-/preview/" style="width: 533px; height: 535px;"/></div>

### 입력

***

첫째 줄에 정수 N, r, c가 주어진다.

### 출력

***

r행 c열을 몇 번째로 방문했는지 출력한다.

### 제한

***

* 1 ≤ N ≤ 15  
* 0 ≤ r, c &lt; 2<sup>N</sup>

### 예제 1

***

```
2 3 1
```

```
11
```

### 예제 2

***

```
3 7 7
```

```
63
```

### 예제 3

***

```
1 0 0
```

```
0
```

### 예제 4

***

```
4 7 7
```

```
63
```

### 예제 5

***

```
10 511 511
```

```
262143
```

### 예제 6

***

```
10 512 512
```

```
786432
```

### 알고리즘 분류

***

* 분할 정복
* 재귀

