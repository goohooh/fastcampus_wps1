"""실습 및 과제"""
# 제목 문제번호 풀이여부

"""피보나치 수 2747번 성공"""
k = int(input())
memo = [0]*(k+1)
def fibo(memo, n):
    if n == 0: return 0
    elif n == 1:
        memo[1] = 1
        return 1
    # 메모이제이션을 이용
    # ★ 재귀라도 실행 속도 향상 시킬 수 있음 ★
    else:
        # 메모된 값이라면 리턴
        if memo[n] > 0:
            return memo[n]
        # 메모되지 않았다면 재귀
        else:
            memo[n] = fibo(memo, n-1) + fibo(memo, n-2)
            return memo[n]
print(fibo(memo, k))

"""나무 자르기 2805번 성공(이진 탐색 공부할 것)"""
n, m = map(int, input().split())
trees = list(map(int, input().split()))
# 1) 0에서 자르면 되지만 자연주의 상근이는 필요한 최소한의 나무만 얻을 수 있는 최대의 절단 높이가 필요
# 2) 최소와 최대값의 중간을 잘라서 얻고자하는 m과 비교하여 탐색 범위를 좁혀 나간다.
top = max(trees)
bottom = 0

# 탐색 전 최대 절단 높이(출력해야할 답)
max_cut_height = 0  # 현재 가장 쉽게 나무를 얻을 수 있는 높이 0

# 2)를 통해 절단할 중간값을 얻어야할 필요성을 얻음
#cut = (top + bottom)//2 # 6)의 이유로 주석처리

# 3) 중간값으로 절단했을 때 얻은 나무와 m 비교해야 함
# 4) m보다 작으면 탐색 범위의 최대값을 낮추고( 절단 높이가 높을 수록 얻을 나무가 적어지므로)
#    m보다 크면 탐색 범위의 최소값을 올려 다시 탐색( 유효한 범위므로 다시 최대값을 얻기위한 도전이 가능하다 )
# 발상 3)을 위한 함수 만든다
def cutter(cut_height):
    #잘랐을 때 얻을 수 있는 나무
    getTree = 0
    for tree in trees:
        # 나무 높이가 절단 높이 보다 커야 얻을 나무가 생긴다
        if tree > cut_height:
            getTree += tree - cut_height
    if getTree >= m:
        return True
    else:
        return False

while bottom <= top:
    cut = (top + bottom)//2
    # 5) 커터함수 값이 참이면 4)에 의해 범위의 최소값(= bottom)을 갱신, 반대는 최대값(top)을 갱신
    #    최소값 = 절단값 + 1 /  최대값 = 절단값 - 1 // 절단 값은 탐색범위에서 제외하므로
    if cutter(cut):
        # getTree가 얻고자 하는 m보다 크거나 같을 때
        # 원하는 값은 절단 높이 중 최대값이므로 max 메서드를 통해 비교하여 기록한다
        max_cut_height = cut
        bottom = cut + 1
    else:
        top = cut - 1
# 6) loop의 필요(발상5 윗줄에 while문을 추가함) 인덴트 변경
#    조건문은 탐색의 범위의 극소까지 => bottom과 top 값이 역전되기 전까지
#    cut 값 갱신을 위해 cut 할당문을 while문 밑으로

print(max_cut_height)


"""포도주 시식 2156번 성공"""
n = int(input())
wine = [0]*10001
for i in range(1, n+1):
    wine[i] = int(input())
D = [0]*10001  # 최대로 마실 수 있는 와인의 양

D[1] = wine[1]
D[2] = wine[1] + wine[2]
D[3] = max(wine[1]+wine[2], wine[1]+wine[3], wine[2]+wine[3])
D[4] = max(
    wine[1]+wine[2]+wine[4],  # D[2] + wine[4]           => D[n-2] + wine[n]
    wine[1]+wine[3]+wine[4],  # D[1] + wine[3] + wine[4] => D[n-3] + wine[n-1] + wine[n]
    wine[2]+wine[3]           # D[3]                     => D[n-1]
)

if n >= 5:
    for i in range(5, n+1):
        D[i] = max(
            D[i-2] + wine[i],
            D[i-3] + wine[i-1] + wine[i],
            D[i-1]
        )
print(D[n])



