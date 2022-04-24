# [보물섬](https://www.acmicpc.net/problem/2589)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/11.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #ec9a00;">Gold V</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 |512 MB|

</div>

### 문제

***

보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다. 보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 각 칸은 육지(L)나 바다(W)로 표시되어 있다. 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다. 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.

<div align="center"><img alt="" src="https://www.acmicpc.net/upload/images/c1bYIsKpI6m317EAx.jpg" style="width: 238px; height: 144px; "/></div>

예를 들어 위와 같이 지도가 주어졌다면 보물은 아래 표시된 두 곳에 묻혀 있게 되고, 이 둘 사이의 최단 거리로 이동하는 시간은 8시간이 된다.

<div align="center"><img alt="" src="https://www.acmicpc.net/upload/images/XqDkWCRUWbzZ.jpg" style="width: 238px; height: 144px; "/></div>

보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.

### 입력

***

첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어진다. 이어 L과 W로 표시된 보물 지도가 아래의 예와 같이 주어지며, 각 문자 사이에는 빈 칸이 없다. 보물 지도의 가로, 세로의 크기는 각각 50이하이다.

### 출력

***

첫째 줄에 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력한다.

### 예제

***

|입력|출력|
|:---|:---|
|5 7<br/>WLLWWWL<br/>LLLWLLL<br/>LWLWLWW<br/>LWLWLLL<br/>WLLWLWW|8|

### 알고리즘 분류

***

* 너비 우선 탐색
* 브루트포스 알고리즘
* 그래프 이론
* 그래프 탐색
