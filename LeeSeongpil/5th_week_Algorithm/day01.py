# """실습 및 과제"""
# # 제목 문제번호 풀이여부
#
# """쇠막대기 10799번 성공"""
# bracket = input()
# stick = []
# piece = 0
#
# for idx, c in enumerate(bracket):
#     # 새로운 막대 시작
#     if c == '(':
#         stick.append(idx)
#     else:
#         # '(' 뒤에 바로 ')'나오면 레이저
#         if stick[-1] + 1 == idx:
#             # 1) 마지막 '('는 레이저 임을 나타내므로 pop()으로 빼낸다
#             # 2) 이후 stack에 쌓인 '(' 만큼의 잘린 조각이 나온다
#             stick.pop()
#             piece += len(stick)
#         else:
#             # 1) ')'는 막대가 끝남을 나타냄. stack에서 '(' 제거
#             # 2) 막대가 끝나면서 조각이되므로 +1
#             stick.pop()
#             piece += 1
#
# print(piece)
#
#
# """에디터 1406번 성공"""
# order = []
# string = input()
# stackL = list(string)
# stackR = list()
# n = input()
# for i in range(int(n)):
#     order += input().split()
# for k in order:
#     if k == 'P':
#         continue
#     elif k == 'L':
#         if len(stackL) == 0:
#             continue
#         else:
#             stackR.append(stackL.pop())
#     elif k == 'D':
#         if len(stackR) == 0:
#             continue
#         else:
#             stackL.append(stackR.pop())
#     elif k == 'B':
#         if len(stackL) == 0:
#             continue
#         else:
#             stackL.pop()
#     else:
#         stackL.append(k)
#
#
# print(''.join(stackL + stackR[::-1]))
#
#
# """조세퍼스 문제0 11866번 성공"""
# man, n = input().split()
# table = []
# dead = []
# for i in range(1, int(man)+1):
#     table.append(i)
# die = 1
# while table:
#     if die == int(n):
#         dead.append(table[0])
#         del table[0]
#         die = 1
#     else:
#         table.append(table[0])
#         del table[0]
#         die += 1
#
# print('<' + ', '.join(map(str, dead)) + '>')
#
#
# """스택수열 1874번 성공 (알고리즘 개선 필요)"""
# n = int(input())
# goal = [int(input()) for _ in range(n)]
# arr = [i for i in range(1, n+1)]
# stack = []
# result = ''
# valid = True
# for _ in range(n):
#     stack.append(arr.pop(0))
#     result += '+'
#     while stack[-1] == goal[0]:
#         stack.pop()
#         result += '-'
#         del goal[0]
#         if not goal:
#             break
#         if not stack:
#             break
# if stack or goal:
#     valid = False
#
# if valid:
#     print('\n'.join(result))
# else:
#     print('NO')


"""연속합 1912 실패"""
n = int(input())
sequence = list(map(int, input().split()))
# stack = []
# ans = 0
# maximum = 0
#
# for i in range(n):
#     if sequence[i] > 0:
#         stack.append(sequence[i])
#         if sum(stack) > maximum:
#             maximum = sum(stack)
#             ans = max(maximum, ans)
#     elif sequence[i] < 0:
#         if sum(stack) + sequence[i] > 0:
#             stack.append(sequence[i])
#         elif sum(stack) + sequence[i] <= 0:
#             if maximum > ans:
#                 ans = maximum
#             stack = []
#             # maximum = 0
#     else:
#         continue
#
# print(ans)
#############################
#####모두 음수일 때 틀림#####
#############################


# 충격의 숏코딩 (승권이형 코드)
minimum = 0
ans = max(sequence)

for i in range(n):
   minimum = max(minimum, 0 ) + sequence[i]
   ans = max(ans, minimum)
print(ans)



