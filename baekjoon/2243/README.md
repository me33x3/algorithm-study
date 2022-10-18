# [사탕상자](https://www.acmicpc.net/problem/2243)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/16.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #27e2a4;">Platinum V</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|2 초 |128 MB|

</div>

### 문제

***

수정이는 어린 동생을 달래기 위해서 사탕을 사용한다. 수정이는 평소에 여러 개의 사탕을 사서 사탕상자에 넣어두고, 동생이 말을 잘 들을 때면 그 안에서 사탕을 꺼내서 주곤 한다.

각각의 사탕은 그 맛의 좋고 나쁨이 1부터 1,000,000까지의 정수로 구분된다. 1이 가장 맛있는 사탕을 의미하며, 1,000,000은 가장 맛없는 사탕을 의미한다. 수정이는 동생이 말을 잘 들은 정도에 따라서, 사탕상자 안에 있는 사탕들 중 몇 번째로 맛있는 사탕을 꺼내주곤 한다. 예를 들어 말을 매우 잘 들었을 때에는 사탕상자에서 가장 맛있는 사탕을 꺼내주고, 말을 조금 잘 들었을 때에는 사탕상자에서 여섯 번째로 맛있는 사탕을 꺼내주는 식이다.

수정이가 보관하고 있는 사탕은 매우 많기 때문에 매번 사탕상자를 뒤져서 꺼낼 사탕을 골라내는 일은 매우 어렵다. 수정이를 도와주는 프로그램을 작성하시오.

### 입력

***

첫째 줄에 수정이가 사탕상자에 손을 댄 횟수 n(1 ≤ n ≤ 100,000)이 주어진다. 다음 n개의 줄에는 두 정수 A, B, 혹은 세 정수 A, B, C가 주어진다. A가 1인 경우는 사탕상자에서 사탕을 꺼내는 경우이다. 이때에는 한 정수만 주어지며, B는 꺼낼 사탕의 순위를 의미한다. 이 경우 사탕상자에서 한 개의 사탕이 꺼내지게 된다. 또, A가 2인 경우는 사탕을 넣는 경우이다. 이때에는 두 정수가 주어지는데, B는 넣을 사탕의 맛을 나타내는 정수이고 C는 그러한 사탕의 개수이다. C가 양수일 경우에는 사탕을 넣는 경우이고, 음수일 경우에는 빼는 경우이다. 맨 처음에는 빈 사탕상자에서 시작한다고 가정하며, 사탕의 총 개수는 2,000,000,000을 넘지 않는다. 또한 없는 사탕을 꺼내는 경우와 같은 잘못된 입력은 주어지지 않는다.

### 출력

***

A가 1인 모든 입력에 대해서, 꺼낼 사탕의 맛의 번호를 출력한다.

### 예제 1

***

```
6
2 1 2
2 3 3
1 2
1 2
2 1 -1
1 2
```

```
1
3
3
```

### 알고리즘 분류

***

* 이분 탐색
* 세그먼트 트리
* 자료 구조
