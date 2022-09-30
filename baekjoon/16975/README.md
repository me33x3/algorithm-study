# [수열과 쿼리 21](https://www.acmicpc.net/problem/16975)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/17.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #27e2a4;">Platinum IV</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|2 초 |512 MB|

</div>

### 문제

***

길이가 N인 수열 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다. 이때, 다음 쿼리를 수행하는 프로그램을 작성하시오.

* <code>1 i j k</code>: A<sub>i</sub>, A<sub>i+1</sub>, ..., A<sub>j</sub>에 k를 더한다.  
* <code>2 x</code>: A<sub>x</sub> 를 출력한다.

### 입력

***

첫째 줄에 수열의 크기 N (1 ≤ N ≤ 100,000)이 주어진다.

둘째 줄에는 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다. (1 ≤ A<sub>i</sub> ≤ 1,000,000)

셋째 줄에는 쿼리의 개수 M (1 ≤ M ≤ 100,000)이 주어진다.

넷째 줄부터 M개의 줄에는 쿼리가 한 줄에 하나씩 주어진다. 1번 쿼리의 경우 1 ≤ i ≤ j ≤ N, -1,000,000 ≤ k ≤ 1,000,000 이고, 2번 쿼리의 경우 1 ≤ x ≤ N이다. 2번 쿼리는 하나 이상 주어진다.

### 출력

***

2번 쿼리가 주어질 때마다 출력한다.

### 예제 1

***

```
5
1 2 3 4 5
4
1 3 4 6
2 3
1 1 3 -2
2 3
```

```
9
7
```

### 알고리즘 분류

***

* 자료 구조
* 느리게 갱신되는 세그먼트 트리
* 세그먼트 트리

