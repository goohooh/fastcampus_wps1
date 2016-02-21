"""실습 및 과제"""
# 제목 문제번호 풀이여부

"""DFS와 BFS 1260번 성공"""
n, m, start = map(int, input().split())
table = list()

# a[0]은 신경쓰지 않는다
for _ in range(n+1):
    table.append([])
for _ in range(m):
    u, v = map(int, input().split())
    table[u].append(v)
    table[v].append(u)

# 파악하기 쉽도록 각 정점의 연결 정렬
for i in range(n+1):
    table[i].sort()

#체크 리스트
check = list()
for i in range(n+1):
    check.append(False)

def dfs(table, check, now):
    if not check[now]:
        check[now] = True
    else:
        return
    print(now, end=' ')
    for k in table[now]:
        dfs(table, check, k)

dfs(table, check, start)
print()

# 리셋
check = list()
for i in range(n+1):
    check.append(False)

def bfs(table, check, now):
    queue = list()
    queue.append(now)

    # 반복문에 들어가기 전에 시작 노드를 체크
    check[now] = True
    while queue:
        now = queue[0]
        print(now, end=' ')
        # dequeue
        queue = queue[1:]

        # 현재 노드의 하위 노드들을 다 체크(bfs이므로)
        for i in table[now]:
            if not check[i]:
                queue.append(i)
                check[i] = True

bfs(table, check, start)


"""반복수열 2331번 성공"""
P, A = map(int, input().split())
lis = []
def arr(P, A):
    #브레이크
    if P in lis:
        # 최종 필요한 반환값
        # 인덱스 값이므로 -1 할 필요 없음
        return lis.index(P)
    lis.append(P)
    p = str(P)
    l = len(p)
    num = 0
    for i in range(l):
        n = int(p[i]) ** A
        num += n
    return arr(num, A)

print(arr(A, P))


"""연결 요소의 개수 11724번 성공"""
n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)
for j in a:
    j.sort()

check =[False for _ in range(n+1)]
# 요소 개수
cnt = 0

# bfs 방식으로 탐색
def figure_components(a, check, start):
    if check[start] == True:
        return

    # 큐에 시작점 enqueue
    # 탐색 전 시작점 체크
    queue = [start]
    check[start] = True
    global cnt
    cnt += 1
    while queue:
        now = queue[0]
        queue = queue[1:]
        for i in a[now]:
            if not check[i]:
                queue.append(i)
                check[i] = True

# 끊겨 있을 수 있으므로 모든 정점에서 dfs 실행
# for문이 없다면 하나의 연결 요소만 카운트하기 떄문
for i in range(1, n+1):
    figure_components(a, check, i)

print(cnt)


"""피보나치 수2 2748번 성공"""
n = int(input())
stack = [1, 1]
if n == 1 or n == 2:
    print(1)
else:
    for i in range(3, n+1):
        new = stack[-1] + stack[-2]
        stack.append(new)
    print(stack[-1])


"""2 * N 타일링 11726번 성공"""
n = int(input())

# n만큼 생성 시, 아래 D[1],D[2] 때문에
# n에 1을 넣으면 인덱스 오류 발생(1000 => 최대 입력값)
D = [0]*1001 # 편의를 위해 1000 + 1

D[1] = 1
D[2] = 2
for i in range(3, n+1):
    #점화식
    D[i] = D[i-1] + D[i-2]
ans = D[n] % 10007
print(ans)


"""ROT13 11655번 성공"""
s =list(input())
res = ''
for i in s:
    #소문자
    if 96 < ord(i) and ord(i) < 123:
        # 알파벳 소문자 + 13의 임계점 n
        if ord(i) < 110:
            c = chr(ord(i) + 13)
            res += c
        else:
            c =chr(ord(i) - 13)
            res += c

    # 대문자
    elif 64 < ord(i) and ord(i) < 91:
        if ord(i) < 78:
            c = chr(ord(i) + 13)
            res += c
        else:
            c = chr(ord(i) - 13)
            res += c
    else:
        res += i

print(res)


"""일곱 난쟁이 2309번 성공"""
a = []
fake = []
valid = True
for i in range(9):
    a.append(int(input()))
total = sum(a)
for i in a:
    for j in a:
        # 하나의 난쟁이를 비교할 필요 없음
        if i == j:
            continue
        # 단 하나의 경우
        if total - (i + j) == 100:
            fake.append(i)
            fake.append(j)
            valid = False
            break
    if not valid:
        break

a.remove(fake[0])
a.remove(fake[1])
a.sort()
for k in range(7):
    print(a[k])