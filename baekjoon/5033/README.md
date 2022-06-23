# [Money Matters](https://www.acmicpc.net/problem/5033)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/10.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver I</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 |128 MB|

</div>

### 문제

***

Our sad tale begins with a tight clique of friends. Together they went on a trip to the picturesque country of Molvania. During their stay, various events which are too horrible to mention occurred. The net result was that the last evening of the trip ended with a momentous exchange of “I never want to see you again!”s. A quick calculation tells you it may have been said almost 50 million times!

Back home in Scandinavia, our group of ex-friends realize that they haven’t split the costs incurred during the trip evenly. Some people may be out several thousand crowns. Settling the debts turns out to be a bit more problematic than it ought to be, as many in the group no longer wish to speak to one another, and even less to give each other money.

Naturally, you want to help out, so you ask each person to tell you how much money she owes or is owed, and whom she is still friends with. Given this information, you’re sure you can figure out if it’s possible for everyone to get even, and with money only being given between persons who are still friends.

### 입력

***

The first line contains two integers, n (2 ≤ n ≤ 10000), and m (0 ≤ m ≤ 50000), the number of friends and the number of remaining friendships. Then n lines follow, each containing an integer o (−10000 ≤ o ≤ 10000) indicating how much each person owes (or is owed if o &lt; 0). The sum of these values is zero. After this comes m lines giving the remaining friendships, each line containing two integers x, y (0 ≤ x &lt; y ≤ n − 1) indicating that persons x and y are still friends.

### 출력

***

Your output should consist of a single line saying “POSSIBLE” or “IMPOSSIBLE”.

### 예제 1

***

```
5 3
100
-75
-25
-42
42
0 1
1 2
3 4
```

```
POSSIBLE
```

### 예제 2

***

```
4 2
15
20
-10
-25
0 2
1 3
```

```
IMPOSSIBLE
```

### 알고리즘 분류

***

* 너비 우선 탐색
* 자료 구조
* 깊이 우선 탐색
* 분리 집합
* 그래프 이론
* 그래프 탐색

