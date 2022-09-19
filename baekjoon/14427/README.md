# [수열과 쿼리 15](https://www.acmicpc.net/problem/14427)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/14.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #ec9a00;">Gold II</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초  (하단 참고)|512 MB|

</div>

### 문제

***

길이가 N인 수열 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다. 이때, 다음 쿼리를 수행하는 프로그램을 작성하시오.

* <code>1 i v</code> : A<sub>i</sub>를 v로 바꾼다. (1 ≤ i ≤ N, 1 ≤ v ≤ 10<sup>9</sup>)  
* <code>2</code> : 수열에서 크기가 가장 작은 값의 인덱스를 출력한다. 그러한 값이 여러개인 경우에는 인덱스가 작은 것을 출력한다.

수열의 인덱스는 1부터 시작한다.

### 입력

***

첫째 줄에 수열의 크기 N이 주어진다. (1 ≤ N ≤ 100,000)

둘째 줄에는 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다. (1 ≤ A<sub>i</sub> ≤ 10<sup>9</sup>)

셋째 줄에는 쿼리의 개수 M이 주어진다. (1 ≤ M ≤ 100,000)

넷째 줄부터 M개의 줄에는 쿼리가 주어진다.

### 출력

***

2번 쿼리에 대해서 정답을 한 줄에 하나씩 순서대로 출력한다.

### 예제 1

***

```
5
5 4 3 2 1
5
2
1 5 3
2
1 4 3
2
```

```
5
4
3
```

### 알고리즘 분류

***

* 자료 구조
* 세그먼트 트리
* 트리를 사용한 집합과 맵

### 시간 제한

***

* PyPy3: 4.2 초  
* PyPy2: 4.2 초

