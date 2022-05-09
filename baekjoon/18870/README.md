# [좌표 압축](https://www.acmicpc.net/problem/18870)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver II</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|2 초 |512 MB|

</div>

### 문제

***

수직선 위에 N개의 좌표 X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

X<sub>i</sub>를 좌표 압축한 결과 X'<sub>i</sub>의 값은 X<sub>i</sub> &gt; X<sub>j</sub>를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>에 좌표 압축을 적용한 결과 X'<sub>1</sub>, X'<sub>2</sub>, ..., X'<sub>N</sub>를 출력해보자.

### 입력

***

첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>이 주어진다.

### 출력

***

첫째 줄에 X'<sub>1</sub>, X'<sub>2</sub>, ..., X'<sub>N</sub>을 공백 한 칸으로 구분해서 출력한다.

### 제한

***

* 1 ≤ N ≤ 1,000,000  
* -10<sup>9</sup> ≤ X<sub>i</sub> ≤ 10<sup>9</sup>

### 예제 1

***

```
5
2 4 -10 4 -9
```

```
2 3 0 3 1
```

### 예제 2

***

```
6
1000 999 1000 999 1000 999
```

```
1 0 1 0 1 0
```

### 알고리즘 분류

***

* 값 / 좌표 압축
* 정렬

