"""
이분 그래프
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	739	152	116	25.951%
문제
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오. 입력으로 주어지는 그래프는 단순 그래프이다.

입력
입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K(2≤K≤5)가 주어진다. 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V(1≤V≤20,000)와 간선의 개수 E(1≤E≤200,000)가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 N까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호가 빈 칸을 사이에 두고 주어진다.

출력
K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

예제 입력  복사
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
예제 출력  복사
YES
NO
"""

test_num = int(input())

for i in range(test_num):
    v, e = map(int, input().split())
    adj = [[] for i in range(v+1)]

    for i in range(e):
        e1, e2 = map(int, input().split())
        adj[e1].append(e2)
        adj[e2].append(e1)

    visited = [0 for _ in range(v+1)]
    black_white = [False for _ in range(v+1)]

    def dfs_sketch(n):
        q = [n]
        visited[n] = 1
        while(q):
            now = q.pop(0)

            for i in adj[now]:
                if(visited[i] == 0):
                    q.append(i)
                    if(black_white[n] == False):
                        black_white[i] = True
                    else:
                        black_white[i] = False

    def bid_graph_check(n):
        for i in range(1,v+1):
            if(i in adj[n]):
                if(black_white[i] == black_white[n]):
                    return False
        return True

    for i in range(1,len(visited)):
        if(visited[i] == 0):
            dfs_sketch(i)

    is_bid = True
    for i in range(1,v+1):
        if(bid_graph_check(i)):
            is_bid = False
            break
        is_bid = True

    if(is_bid):
        print("YES")
    else:
        print("NO")





