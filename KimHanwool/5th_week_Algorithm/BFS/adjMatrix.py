v, e, start = map(int,input().split())

adj = [[0 for j in range(v+1)] for j in range(v+1)]

for _ in range(e):
    e1, e2 = map(int, input().split())
    adj[e1][e2] = adj[e2][e1] = 1

for li in adj[1:]:
    print(li[1:])

def BFS(start):
    q = [start]
    visited = [[] for i in range(v+1)]

    while(q):
        now = q.pop(0)

        if(now == start):
            print(now)

        for i in range(1, v+1):
            if(adj[now][i] == 1 and visited[i] == 0):
                visited[i] = 1
                print(i)


