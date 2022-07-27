# [강의실 배정](https://www.acmicpc.net/problem/11000)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/11.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #ec9a00;">Gold V</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 |256 MB|

</div>

### 문제

***

수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

김종혜 선생님한테는 S<sub>i</sub>에 시작해서 T<sub>i</sub>에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, T<sub>i</sub> ≤ S<sub>j</sub> 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

수강신청 대충한 게 찔리면, 선생님을 도와드리자!

### 입력

***

첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)

이후 N개의 줄에 S<sub>i</sub>, T<sub>i</sub>가 주어진다. (0 ≤ S<sub>i</sub> &lt; T<sub>i</sub> ≤ 10<sup>9</sup>)

### 출력

***

강의실의 개수를 출력하라.

### 예제 1

***

```
3
1 3
2 4
3 5
```

```
2
```

### 알고리즘 분류

***

* 자료 구조
* 그리디 알고리즘
* 우선순위 큐
* 정렬

