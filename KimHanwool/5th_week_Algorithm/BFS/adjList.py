v, e = map(int, input().split())

adj = [[] for i in range(v+1)]
visited = [0 for i in range(v+1)]

for _ in range(e):
    e1, e2 = map(int, input().split())
    adj[e1].append(e2)
    adj[e2].append(e1)

def BFS(start):
    q = [start]
    visited[start] = 1

    while(q):
        now = q.pop(0)
        if(now == start):
            print(now)

        for i in range(1,v+1):
            if(i in adj[now] and visited[i] == 0):
                visited[i] = 1
                print(i)
                q.append(i)

BFS(1)