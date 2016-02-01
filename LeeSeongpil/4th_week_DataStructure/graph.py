graph = {
    'a': set(['b', 'c']),
    'b': set(['a', 'd','e']),
    'c': set(['a', 'f']),
    'd': set(['b']),
    'e': set(['b', 'f']),
    'f': set(['c', 'e'])
}



def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

print(dfs(graph, 'a' ))



def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

print(dfs_paths(graph, 'a', 'e'))

# num = int(input())  # 정점 개수 입력
# matrix = [[0 for k in range(num)] for i in range(num)]  # 빈 2차원 배열 선언
#
# for i in range(num):
#     line = input().split()
#     for j, val in enumerate(line):
#         matrix[i][j] = int(val)
# print(matrix)
