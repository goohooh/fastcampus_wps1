"""실습 및 과제"""
# 제목 문제번호 풀이여부

"""최대공약수와 최소공배수 2609번 성공"""
x, y = map(int, input().split())

# 최대 공약수 : 재귀
def gcd(a, b):
    if b != 0:
        return gcd(b, a%b)
    else:
        return a

# 최소 공배수
def lcm(a, b):
    return int((a * b)/gcd(a,b))
print(gcd(x, y))
print(lcm(x, y))


"""소수찾기 1978번 성공"""
n = int(input())
a = list(map(int, input().split()))
ans = []

def prime(x):
    if 2 > x:
        return False
    # x/2 => O( logN )
    # 자기 자신과 자신의 반 이상은 탐색할 필요 없음
    # 반부터 자신까지 오려면 2 미만의 실수로 곱해야 하므로 의미가 없다
    for i in range(2, int(x/2+1)):
        if x % i == 0:
            # 1과 x의 반 이상은 제외했으므로
            # 무엇으로든 나누어 떨어지면 소수가 아니다
            return False
    # 위 조건을 모두 통과했다면 소수
    return True

for k in a:
    if prime(k):
        ans.append(k)

print(len(ans))


"""소수 구하기 1929번 성공(prime 함수 확실히 설명할 수 있어야함)"""
n, k = map(int, input().split())

# True : 켜짐(소수) //  False : 꺼짐(소수 아님)
prime = [True for i in range(k+1)] # 일단 모든 수를 True로 켜둔 상태
prime[1] = False # 소수의 정의

for i in range(2, k+1):
    # i*i > k // 탐색할 필요 없음
    # i의 제곱은 i의 배수이기 때문에 False로 불이 꺼짐
    if i*i > k:
        break

    if prime[i] == True:
        m = 2
        while i*m <= k:
            # 배수들은 다 False로 꺼버린다
            prime[i*m] = False
            m += 1


for i in range(n, k+1):
    if prime[i] == True:
        print(i)


"""골드바흐의 추측 6588번 성공(prime 함수 확실히 설명할 수 있어야함) """
def prime(x):
    if 2 > x:
        return False
    # 1929번 prime 함수와 같은 이유
    # i * i > k == i > k**0.5 ↓
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

n = 1
while n:
    n = int(input())
    if n == 0:
        break
    for i in range(2,n+1):
        if prime(i) ==True and prime(n-i) == True:
            print("{} = {} + {}".format(n, i, n-i))
            break


"""1로 만들기 1463번"""
n = int(input())
D = [0]*((10**6)+1)
D[1] = 0
# 1 = 1 (연산 0회 => 0 )
D[2] = 1
# 2 /2 = 1 (/2연산 1회 => D[2] = 1) D[2] = 1
# 2 -1 = 1 (-1연산 1회 => D[2] = 1) D[2] = 1
D[3] = 1
# 3 /3 = 1 (/3연산 1회   => D[3] = 1) [3] = 1
# 3 -1 -1 = 1(-1연산 2회 => D[3] = D[2] + 1)   // 관계식 : D[n] = D[n-1] +1
D[4] = 2
# 4 /2 /2 (/2연산 2회    => D[4] => D[2] + 1)  // 관계식 : D[n] = D[n/2] + 1
# 4 -1 -1 -1 (-1연산 3회 => D[4] = D[3] + 1)   // 관계식 : D[n] = D[n-1] + 1
D[5] = 3
# 5 -1 /2 /2 (-1연산 1회 /2연산 2회 => D[5] = [4] + 1 ) // 관계식 : D[n] = D[n-1] + 1
D[6] = 2
# 6 /3 /2 (/3연산 1회 /2연산 1회    => D[6] = D[2] + 1) // 관계식 : D[n] = D[n/3] + 1

## 공통 관계식 : D[n] = D[n-1] + 1
## 조건 관계식 : n % 3 = 0 일때 D[n] = D[n/3] + 1
## 조건 관계식 : n % 2 = 0 일때 D[n] = D[n/2] + 1
if n >= 7:
    for i in range(7, n+1):
        D[i] = D[i-1] + 1
        if i % 3 == 0 and D[i] > D[i//3] + 1:
            D[i] = D[i//3] + 1
        if i % 2 == 0 and D[i] > D[i//2] + 1:
            D[i] = D[i//2] + 1
print(D[n])

