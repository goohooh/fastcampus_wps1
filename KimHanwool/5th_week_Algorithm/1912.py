"""
연속합
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	2340	775	543	35.100%
문제
n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 숫자를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 숫자는 한 개 이상 선택해야 한다.

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.

입력
첫째 줄에 정수 n(1≤n≤100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다.

출력
첫째 줄에 답을 출력한다.

예제 입력  복사
10
10 -4 3 1 5 6 -35 12 21 -1
예제 출력  복사
33
"""


def cal(st):
    if(st[-1] < 0):
        st.pop()
        if(not st):
            print(max(minus_list))
            return
    elif(len(st) == 1 or len(st) == 2):
            print(st.pop())
            return
    else:
        t1 = st.pop()
        t2 = st.pop()
        t3 = st.pop()
        result = max(t1, t1+t2+t3, t3)
        st.append(result)
    cal(st)

#n = int(input())
while(True):
    li = list(map(int, input().split()))
    num_list = []
    prev_icon = True
    minus_list = []
    st = []

    for num in li:
        if(num >=0):
            if(not st):
                st.append(num)
            elif(st[-1] >=0):
                st.append(st.pop() + num)
            elif(st[-1] <0):
                st.append(num)
        elif(num < 0):
            minus_list.append(num)
            if(not st):
                st.append(num)
            elif(st[-1] <0):
                st.append(st.pop() + num)
            elif(st[-1] >0):
                st.append(num)

    reverse_st = st[::-1]
    print(reverse_st)
    cal(reverse_st)
