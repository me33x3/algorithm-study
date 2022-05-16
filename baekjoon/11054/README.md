# [가장 긴 바이토닉 부분 수열](https://www.acmicpc.net/problem/11054)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/13.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #ec9a00;">Gold III</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 |256 MB|

</div>

### 문제

***

수열 S가 어떤 수 S<sub>k</sub>를 기준으로 S<sub>1</sub> &lt; S<sub>2</sub> &lt; ... S<sub>k-1</sub> &lt; S<sub>k</sub> &gt; S<sub>k+1</sub> &gt; ... S<sub>N-1</sub> &gt; S<sub>N</sub>을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10, 20, <strong>30</strong>, 25, 20}과 {10, 20, 30, <strong>40</strong>}, {<strong>50</strong>, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

### 입력

***

첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 A<sub>i</sub>가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ A<sub>i</sub> ≤ 1,000)

### 출력

***

첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.

### 예제 1

***

```
10
1 5 2 1 4 3 4 5 2 1
```

```
7
```

### 힌트

***

예제의 경우 {<strong>1</strong> 5 <strong>2</strong> 1 4 <strong>3</strong> <strong>4</strong> <strong>5</strong> <strong>2</strong> <strong>1</strong>}이 가장 긴 바이토닉 부분 수열이다.

### 알고리즘 분류

***

* 다이나믹 프로그래밍

