"""
연결 요소의 개수
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	132	78	69	60.000%
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력  복사
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력  복사
2
예제 입력 2  복사
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3

"""

v, e = map(int, input().split())
adj = [[] for _ in range(v+1)]

for _ in range(e):
    e1, e2 = map(int, input().split())
    adj[e1].append(e2)
    adj[e2].append(e1)

visited = [0 for _ in range(v+1)]

def bfs(start):
    q = [start]
    visited[start] = 1
    while(q):
        now = q.pop(0)

        for i in adj[now]:
            if(visited[i] == 0):
                q.append(i)
                visited[i] = 1

result = 0
for i in range(1, len(visited)):
    if(visited[i] == 0):
        bfs(i)
        result += 1
print(result)





