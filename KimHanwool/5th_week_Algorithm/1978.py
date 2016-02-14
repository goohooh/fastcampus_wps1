"""
소수 찾기
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	1244	768	669	62.002%
문제
주어진 숫자들 중 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력  복사
4
1 3 5 7
예제 출력  복사
3
"""

n = int(input())
li = map(int, input().split())
count = 0

def is_prime(n):

    if (n == 1 or n == 0):
        return False

    i = 2
    while(i*i <= n):
        if(n%i == 0):
            return False
        i += 1
    return True

for num in li:
    if(is_prime(num) == True):
        count += 1

print(count)
