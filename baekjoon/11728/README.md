# [배열 합치기](https://www.acmicpc.net/problem/11728)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/6.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver V</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1.5 초 |256 MB|

</div>

### 문제

***

정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.

### 입력

***

첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)

둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 배열에 들어있는 수는 절댓값이 10<sup>9</sup>보다 작거나 같은 정수이다.

### 출력

***

첫째 줄에 두 배열을 합친 후 정렬한 결과를 출력한다.

### 예제

***

|입력|출력|
|:---|:---|
|2 2<br/>3 5<br/>2 9|2 3 5 9|
|2 1<br/>4 7<br/>1|1 4 7|
|4 3<br/>2 3 5 9<br/>1 4 7|1 2 3 4 5 7 9|

### 알고리즘 분류

***

* 정렬
* 두 포인터
