"""
스택 수열 실패
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	2047	511	382	27.208%
문제
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 먼저 들어간 자료가 제일 나중에 나오는 (FILO, first in last out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이 때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

입력
첫 줄에 n(1≤n≤100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

출력
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

예제 입력  복사
8
4
3
6
8
7
5
2
1
예제 출력  복사
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-
"""

n = int(input())
num_list = [int(input()) for i in range(n)] #숫자 리스트
st = []   #최종 배열 형상
now = 0 #어디까지 입력하였는지 확인
ans = []
is_possible = True

for num in num_list:

    if num > now:
        for i in range(now+1,num+1):
            st.append(i)
            ans += "+"
        now = num
        st.pop()
        ans += "-"

    elif num < now:
        while(st):
            if(st[-1] == num):
                st.pop()
                ans +="-"
                break
            else:
                is_possible = False

if(is_possible):
    for char in ans:
        print(char)
else:
    print("NO")










