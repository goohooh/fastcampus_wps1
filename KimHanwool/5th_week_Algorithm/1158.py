"""
조세퍼스 문제
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	901	462	364	54.985%
문제
조세퍼스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 M(≤ N)이 주어진다. 이제 순서대로 M번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, M)-조세퍼스 순열이라고 한다. 예를 들어 (7, 3)-조세퍼스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 M이 주어지면 (N,M)-조세퍼스 순열을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ M ≤ N ≤ 5,000)

출력
예제와 같이 조세퍼스 순열을 출력한다.

예제 입력  복사
7 3
예제 출력  복사
<3, 6, 2, 7, 5, 1, 4>
"""

n, m = map(int, input().split())
q = [i for i in range(n+1) if i is not 0]
result = []

while(len(q)):
    for i in range(m-1):
        q.append(q.pop(0))
    result.append(q.pop(0))


print("<", end ="")
for index in range(len(result)):
    if(index == len(result)-1):
        print("%d>" %result[index])
    else:
        print("%d, " %result[index], end = "")