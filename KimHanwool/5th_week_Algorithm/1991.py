"""
트리 순회
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	1044	543	413	53.222%
문제
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.



예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.

입력
첫째 줄에는 이진 트리의 노드의 개수 N(1≤N≤26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 영문자 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현된다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

예제 입력  복사
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
예제 출력  복사
ABDCEFG
DBAECFG
DBEGFCA
"""

n = int(input())
tree_array = [0 for i in range(n+1)]
for i in range(n):
    c1, c2, c3 = map(lambda x: x-64, list(map(ord, input().split())))

    if(c2 == -18 and c3 == -18):
        tree_array[c1] = [0,0]
    elif(c2 == -18):
        tree_array[c1] = [0,c3]
    elif(c3 == -18):
        tree_array[c1] = [c2, 0]
    else:
        tree_array[c1] = [c2, c3]


def preorder(start):
    print(chr(start+64), end = "")
    if(tree_array[start][0] != 0):
        preorder(tree_array[start][0])
    if(tree_array[start][1] != 0):
        preorder(tree_array[start][1])

def postorder(start):
    if(tree_array[start][0] != 0):
        postorder(tree_array[start][0])
    if(tree_array[start][1] != 0):
        postorder(tree_array[start][1])
    print(chr(start+64), end = "")

def inorder(start):
    if(tree_array[start][0] != 0):
        inorder(tree_array[start][0])
    print(chr(start+64), end = "")
    if(tree_array[start][1] != 0):
        inorder(tree_array[start][1])

preorder(1)
print()
inorder(1)
print()
postorder(1)
print()


