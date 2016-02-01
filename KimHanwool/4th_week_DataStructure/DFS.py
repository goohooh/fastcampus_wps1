
class _Graph():

    adj_matrix = []
    visit = []
    number_of_Vertex = 0

    def __init__(self, n):
        self.number_of_Vertex = n
        ad_matrix = [[0 for j in range(n+1)] for i in range(n+1)]
        visit = [[False for j in range(n+1)] for i in range(n+1)]

    def dfs(self, start, end):
        st = [start]
        visit = []

        while (len(st) > 0):
            temp = st.pop()
            visit.append(temp)

            if temp == end:
                return visit

            elif temp not in visit:
                for num in range(self.adj_matrix[temp]):
                    if self.adj_matrix[temp][num] not in visit:
                        st.append(num)

        return visit


# gr = _Graph(5)
# gr.adj_matrix[1][2] = 1
# gr.adj_matrix[2][3] = 1
# gr.adj_matrix[3][4] = 1
# gr.adj_matrix[3][5] = 1
# gr.adj_matrix[4][5] = 1
# gr.dfs(1, 5)

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B','F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited, st = set(), [start]

    while st:
        vertex = st.pop()

        if vertex not in visited:
            visited.add(vertex)
            st.extend(graph[vertex] - visited)
    return visited

dfs(graph,'A')



