"""
별찍기 - 8
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	1386	978	938	71.877%
문제
예제를 보고 별찍는 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N (1<=N<=100)이 주어진다.

출력
첫째 줄부터 2*N-1번째 줄 까지 차례대로 별을 출력한다.

예제 입력  복사
5
예제 출력  복사
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

"""

n = int(input())

total = n*2

for i in range(1, n+1):
    total_space = total - (i*2)
    print("*"*i, end = "")
    print(" "*total_space, end = "")
    print("*"*i)

for i in range(n-1, 0, -1):
    total_space = total - (i*2)
    print("*"*i, end = "")
    print(" "*total_space, end = "")
    print("*"*i)
