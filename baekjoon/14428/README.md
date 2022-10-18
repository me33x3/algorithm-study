# [수열과 쿼리 16](https://www.acmicpc.net/problem/14428)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/15.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #ec9a00;">Gold I</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|2 초 |512 MB|

</div>

### 문제

***

길이가 N인 수열 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다. 이때, 다음 쿼리를 수행하는 프로그램을 작성하시오.

* <code>1 i v</code> : A<sub>i</sub>를 v로 바꾼다. (1 ≤ i ≤ N, 1 ≤ v ≤ 10<sup>9</sup>)  
* <code>2 i j</code> : A<sub>i</sub>, A<sub>i+1</sub>, ..., A<sub>j</sub>에서 크기가 가장 작은 값의 인덱스를 출력한다. 그러한 값이 여러개인 경우에는 인덱스가 작은 것을 출력한다. (1 ≤ i ≤ j <span style="display: none;"> </span>≤ N, 1 ≤ v ≤ 10<sup>9</sup>)

수열의 인덱스는 1부터 시작한다.<span style="display: none;"> </span>

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
6
2 1 3
2 1 4
1 5 3
2 3 5
1 4 3
2 3 5
```

```
3
4
4
3
```

### 알고리즘 분류

***

* 세그먼트 트리
* 자료 구조
