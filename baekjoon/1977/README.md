# [완전제곱수](https://www.acmicpc.net/problem/1977)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/5.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #ad5600;">Bronze I</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|2 초 |128 MB|

</div>

### 문제

***

M과 N이 주어질 때 M이상 N이하의 자연수 중 완전제곱수인 것을 모두 골라 그 합을 구하고 그 중 최솟값을 찾는 프로그램을 작성하시오. 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 완전제곱수는 64, 81, 100 이렇게 총 3개가 있으므로 그 합은 245가 되고 이 중 최솟값은 64가 된다.

### 입력

***

첫째 줄에 M이, 둘째 줄에 N이 주어진다. M과 N은 10000이하의 자연수이며 M은 N보다 같거나 작다.

### 출력

***

M이상 N이하의 자연수 중 완전제곱수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 단, M이상 N이하의 자연수 중 완전제곱수가 없을 경우는 첫째 줄에 -1을 출력한다.

### 예제

***

|입력|출력|
|:---|:---|
|60<br/>100|245<br/>64|
|75<br/>80|-1|

### 알고리즘 분류

***

* 구현
* 수학
