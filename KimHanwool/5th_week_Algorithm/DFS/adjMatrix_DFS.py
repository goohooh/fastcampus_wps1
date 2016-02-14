v, e = map(int, input().split())
adj = [[0 for _ in range(v+1)] for _ in range(v+1)]

for _ in range(e):
    e1, e2 = map(int, input().split())
    adj[e1][e2] = 1
    adj[e2][e1] = 1

def DFS(start):
    st = [start]
    visited = [0 for _ in range(v+1)]

    while(st):
        now = st.pop()
        if(visited[now] == 0):
            visited[now] = 1
            print(now)


        for i in range(v+1):
            if(adj[now][i] == 1 and visited[i] == 0):
                st.append(i)

DFS(1)
