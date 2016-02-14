"""
 문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	609	231	211	37.882%
문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.



입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

예제 입력  복사
2
예제 출력  복사
2
예제 입력 2  복사
9
예제 출력 2  복사
55
"""

import sys
sys.setrecursionlimit(10000)

n = int(input())
li = [0 for _ in range(n+2)]

def fibo(n):
    if(n == 0):
        li[0] = 0
        return 0
    elif(n == 1):
        li[1] = 1
        return 1
    else:
        li[n] = li[n-1] + li[n-2]
        if(li[n]):
            return li[n]
        return fibo(n-1) + fibo(n-2)

result = fibo(n+1)%10007
print(result)