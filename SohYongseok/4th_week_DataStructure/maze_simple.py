input_string = input()  # 정점 개수 입력

a = input_string.split()

num1 = int(a[1])
num2 = int(a[0])
matrix = [[0 for k in range(num1)] for i in range(num2)]  # 빈 2차원 배열 선언

# num1 is width, j
# num2 is height, i

for i in range(num2):
    line = input()
    for j, val in enumerate(line):
        matrix[i][j] = int(val)
    print(matrix[i])


graph = dict()


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]  # list structure,
    while queue:
        (vertex, path) = queue.pop(0)
        # vertex = str(vertex)
        # path = str(path)
        #print(vertex, path)
        for next in graph[vertex]-set(path):
            #next = str(next)
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path+[next]))
         #       print(queue)

for node in range(num1 * num2):
    i = int(node/num1) # i is 수직값
    j = node%num1 # j is 수평값
    l = list()
    if matrix[i][j] is 1: # 내 값이 1이면 주위 값을 보자
#        if i-1 < 0 or i+1 >= num2 or j-1 < 0 or j+1 >= num1:
#            pass
        if i-1 >= 0 :
            if matrix[i-1][j] is 1:
                l.append(str((i-1)*num1+j))
        if i+1 < num2:
            if matrix[i+1][j] is 1:
                l.append(str((i+1)*num1+j))
        if j-1 >= 0:
            if matrix[i][j-1] is 1:
                l.append(str(i*num1+(j-1)))
        if j+1 < num1:
            if matrix[i][j+1] is 1:
                l.append(str(i*num1+(j+1)))

        graph[str(i*num1+j)] = set(l) # 1 인 블록 주위의 다른 1 인 블록들을 찾아서 list에 추가된 것을 dictionary에 추가

#for k in range(num1*num2):
print(graph)

for i in bfs_paths(graph, '0', '23'):
    print(i)