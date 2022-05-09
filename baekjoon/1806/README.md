# [부분합](https://www.acmicpc.net/problem/1806)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/12.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #ec9a00;">Gold IV</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|0.5 초  (하단 참고)|128 MB|

</div>

### 문제

***

10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

### 입력

***

첫째 줄에 N (10 ≤ N &lt; 100,000)과 S (0 &lt; S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

### 출력

***

첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.

### 예제 1

***

```
10 15
5 1 3 5 10 7 4 9 2 8
```

```
2
```

### 알고리즘 분류

***

* 두 포인터

### 시간 제한

***

* Java 8: 1 초  
* Java 8 (OpenJDK): 1 초  
* Java 11: 1 초  
* Kotlin (JVM): 1 초  
* Java 15: 1 초

