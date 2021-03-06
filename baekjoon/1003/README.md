# [피보나치 함수](https://www.acmicpc.net/problem/1003)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver III</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|0.25 초 (추가 시간 없음) |128 MB|

</div>

### 문제

***

다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

```
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
```

<code>fibonacci(3)</code>을 호출하면 다음과 같은 일이 일어난다.

* <code>fibonacci(3)</code>은 <code>fibonacci(2)</code>와 <code>fibonacci(1)</code> (첫 번째 호출)을 호출한다.  
* <code>fibonacci(2)</code>는 <code>fibonacci(1)</code> (두 번째 호출)과 <code>fibonacci(0)</code>을 호출한다.  
* 두 번째 호출한 <code>fibonacci(1)</code>은 1을 출력하고 1을 리턴한다.  
* <code>fibonacci(0)</code>은 0을 출력하고, 0을 리턴한다.  
* <code>fibonacci(2)</code>는 <code>fibonacci(1)</code>과 <code>fibonacci(0)</code>의 결과를 얻고, 1을 리턴한다.  
* 첫 번째 호출한 <code>fibonacci(1)</code>은 1을 출력하고, 1을 리턴한다.  
* <code>fibonacci(3)</code>은 <code>fibonacci(2)</code>와 <code>fibonacci(1)</code>의 결과를 얻고, 2를 리턴한다.

1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, <code>fibonacci(N)</code>을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

### 입력

***

첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

### 출력

***

각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

### 예제 1

***

```
3
0
1
3
```

```
1 0
0 1
1 2
```

### 예제 2

***

```
2
6
22
```

```
5 8
10946 17711
```

### 알고리즘 분류

***

* 다이나믹 프로그래밍

