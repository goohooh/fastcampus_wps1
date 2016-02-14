"""
조합 0의 개수
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	1570	270	219	24.634%
문제
nCm의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 n, m(0≤m≤n≤2,000,000,000, n!=0)이 들어온다.

출력
첫째 줄에 0의 개수를 출력한다.

예제 입력  복사
25 12
예제 출력  복사
2
"""

n, m = map(int, input().split())
result_list5 = [0,0,0]
result_list2 = [0,0,0]

def check_five(n):
    result = 0
    start = 5

    while(start <= n):
        for i in range(1, n+1):
            if(i%start == 0):
                result += 1
            if(i == n):
                result_list5[0] = result
            if(i == m and start <= m):
                result_list5[1] = result
            if(i == (n-m) and start <= (n-m)):
                result_list5[2] = result

        start *= 5
    return result

def check_two(n):
    result = 0
    start = 2

    while(start <= n):
        for i in range(1, n+1):
            if(i%start == 0):
                result += 1
            if(i == n):
                result_list2[0] = result
            if(i == m and start <= m):
                result_list2[1] = result
            if(i == (n-m) and start <= (n-m)):
                result_list2[2] = result

        start *= 2
    return result

check_five(n)
check_two(n)
final_result = []

final_result.append(min(result_list5[0], result_list2[0]))
final_result.append(min(result_list5[1]+result_list5[2],result_list2[1]+result_list2[2]))

print(final_result[0]-final_result[1])