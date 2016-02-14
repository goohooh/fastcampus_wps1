"""
소수 구하기
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	1558	473	352	37.487%
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1≤M≤N≤1,000,000)

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

예제 입력  복사
3 16
예제 출력  복사
3
5
7
11
13
"""

m, n = map(int,input().split())

check =[True for _ in range(n+1)]

check[0], check[1] = False, False

i = 2
while(i*i <= n):
    mul = 2
    while(i*mul <= n):
        num = i*mul
        check[num] = False
        mul += 1
    i+= 1

for i, is_prime in enumerate(check):
    if m <= i and is_prime == True:
        print(i)

