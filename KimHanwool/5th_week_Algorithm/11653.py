"""
소인수분해
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	278	170	123	71.098%
문제
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N (2 ≤ N ≤ 10,000,000)이 주어진다.

출력
N의 인수를 한 줄에 하나씩 증가하는 순서대로 출력한다.

예제 입력  복사
72
예제 출력  복사
2
2
2
3
3
예제 입력 2  복사
3
예제 출력 2  복사
3
예제 입력 3  복사
6
예제 출력 3  복사
2
3
예제 입력 4  복사
2
예제 출력 4  복사
2
예제 입력 5  복사
9991
예제 출력 5  복사
97
103
"""


n = int(input())
check =[False for _ in range(n+1)]
prime_list = []

i = 2
for i in range(2,n+1):
    if(check[i]):
        continue
    prime_list.append(i)
    for j in range(i*i, n+1, i):
        check[j] = True

now = n
i = 0

while(now > 1):
    if(now%prime_list[i] == 0):
        now = int(now/prime_list[i])
        print(prime_list[i])
        continue
    i += 1



