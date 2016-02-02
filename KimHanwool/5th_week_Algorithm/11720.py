#-*- coding: utf-8 -*-

"""
숫자의 합
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	820	413	374	53.352%
문제
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

출력
입력으로 주어진 숫자 N개의 합을 출력한다.
"""

# n = input()
# result = 0
# num_list = list(input())
#
# for num in num_list:
#     result += int(num)
# print (result)

_= input()
a = map(int, input())
print(sum(a))
