v, e = map(int, input().split())
adj = [[] for i in range(v+1)]

for _ in range(e):
    e1, e2 = map(int, input().split())
    adj[e1].append(e2)
    adj[e2].append(e1)

def DFS(start):
    st = [start]
    visited = [0 for _ in range(v+1)]

    while(st):
        now = st.pop()
        if(visited[now] != 1):
            visited[now] = 1
            print(now)

        for i in range(1, v+1):
            if(i in adj[now] and visited[i] == 0):
                st.append(i)

DFS(1)
