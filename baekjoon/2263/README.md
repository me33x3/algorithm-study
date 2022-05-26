# [트리의 순회](https://www.acmicpc.net/problem/2263)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/14.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #ec9a00;">Gold II</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|5 초 |128 MB|

</div>

### 문제

***

n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다. 이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성하시오.

### 입력

***

첫째 줄에 n(1 ≤ n ≤ 100,000)이 주어진다. 다음 줄에는 인오더를 나타내는 n개의 자연수가 주어지고, 그 다음 줄에는 같은 식으로 포스트오더가 주어진다.

### 출력

***

첫째 줄에 프리오더를 출력한다.

### 예제 1

***

```
3
1 2 3
1 3 2
```

```
2 1 3
```

### 알고리즘 분류

***

* 분할 정복
* 재귀
* 트리

