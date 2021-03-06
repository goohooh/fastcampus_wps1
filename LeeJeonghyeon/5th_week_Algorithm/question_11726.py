# https://www.acmicpc.net/problem/11726

# ====================
# 11726번 :: 2xn 타일링
# ====================
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

# 다이나믹 프로그래밍 문제

# 점화식
# d[n] 타일을 채우는 방법의 수
# d[n] = d[n-1]+d[n-2]

n = int(input())
d = [0 for _ in range(n+1)] #d[1]에서 out of range되는 것을 막기위해 n+1
d[0] = 1
d[1] = 2
for i in range(3,n+1):
    d[i-1] = (d[i-1-1]+d[i-2-1])%10007 #인덱스 0부터 사용하기 위해 -1씩
print(d[n-1])

# 맞았습니다!! 메모리 12172 KB, 시간 116 MS, 코드 길이 321 B



# ---------------------
# 숏코딩보고 상처받을 시간...

# 방법1 : 메모리 121160 KB, 시간 120MS, 코드 길이 76 B
# n=int(input())
# a,b=1,1
# for i in range(n):
#     a,b=b,(a+b)%10007
# print(a)

# 방법2 : 메모리 12168 KB, 시간 108 MS, 코드 길이 88 B
# A=[1,2];N=int(input())
# for i in range(2,N):A.append(A[i-1]+A[i-2])
# print(A[N-1]%10007)
