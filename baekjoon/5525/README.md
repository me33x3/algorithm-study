# [IOIOI](https://www.acmicpc.net/problem/5525)

> <img src="https://d2gd6pc034wcta.cloudfront.net/tier/10.svg" width="16" heigth="21" style = "vertical-align: middle;"/>&nbsp;<span style="font-size: 18px; color: #435f7a;">Silver I</span>

***

<div align="center">

|시간 제한|메모리 제한|
|:---:|:---:|
|1 초 |256 MB|

</div>

### 문제

***

N+1개의 <code>I</code>와 N개의 <code>O</code>로 이루어져 있으면, <code>I</code>와 <code>O</code>이 교대로 나오는 문자열을 P<sub>N</sub>이라고 한다.

* P<sub>1</sub> <code>IOI</code>  
* P<sub>2</sub> <code>IOIOI</code>  
* P<sub>3</sub> <code>IOIOIOI</code>  
* P<sub>N</sub> <code>IOIOI...OI</code> (<code>O</code>가 N개)

<code>I</code>와 <code>O</code>로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 P<sub>N</sub>이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

### 입력

***

첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.

### 출력

***

S에 P<sub>N</sub>이 몇 군데 포함되어 있는지 출력한다.

### 제한

***

* 1 ≤ N ≤ 1,000,000  
* 2N+1 ≤ M ≤ 1,000,000  
* S는 <code>I</code>와 <code>O</code>로만 이루어져 있다.

### 서브태스크

***

<table class="table table-bordered td-middle subtask-table" style="width: 100%;">
<thead>
<th style="width: 5%;">번호</th>
<th style="width: 5%;">배점</th>
<th style="width: 90%;">제한</th>
</thead>
<tbody>
<tr>
<td>1</td>
<td>50</td>
<td><p>N ≤ 100, M ≤ 10 000.</p>
</td>
</tr>
<tr>
<td>2</td>
<td>50</td>
<td><p>추가적인 제약 조건이 없다.</p>
</td>
</tr>
</tbody>
</table>

### 예제 1

***

```
1
13
OOIOIOIOIIOII
```

```
4
```

* <code>OO<u>IOI</u>OIOIIOII</code>  
* <code>OOIO<u>IOI</u>OIIOII</code>  
* <code>OOIOIO<u>IOI</u>IOII</code>  
* <code>OOIOIOIOI<u>IOI</u>I</code>

### 예제 2

***

```
2
13
OOIOIOIOIIOII
```

```
2
```

* <code>OO<u>IOIOI</u>OIIOII</code>  
* <code>OOIO<u>IOIOI</u>IOII</code>

### 알고리즘 분류

***

* 문자열

