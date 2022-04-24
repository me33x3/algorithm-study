# [N번째 큰 수](https://www.acmicpc.net/problem/2693)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/6.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver V</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 |32 MB|

</div>

### 문제

***

배열 A가 주어졌을 때, N번째 큰 값을 출력하는 프로그램을 작성하시오.

배열 A의 크기는 항상 10이고, 자연수만 가지고 있다. N은 항상 3이다.

### 입력

***

첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 배열 A의 원소 10개가 공백으로 구분되어 주어진다. 이 원소는 1보다 크거나 같고, 1,000보다 작거나 같은 자연수이다.

### 출력

***

각 테스트 케이스에 대해 한 줄에 하나씩 배열 A에서 3번째 큰 값을 출력한다.

### 예제

***

|입력|출력|
|:---|:---|
|4<br/>1 2 3 4 5 6 7 8 9 1000<br/>338 304 619 95 343 496 489 116 98 127<br/>931 240 986 894 826 640 965 833 136 138<br/>940 955 364 188 133 254 501 122 768 408|8<br/>489<br/>931<br/>768|

### 알고리즘 분류

***

* 정렬
