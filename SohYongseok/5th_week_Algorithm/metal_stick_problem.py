# line = list(input())
# stack = []
# sum = 0
# for i,e in enumerate(line):
#     if e is '(':
#         stack.append(i)
#     elif e is ')':
#         if stack[-1] is i-1: # 연속
#             stack.pop()
#             sum += len(stack)
#         else:
#             stack.pop()
#             sum += 1
# print(sum)


line = list(input())
stack = []
sum = 0
for i,e in enumerate(line):
    if e == '(':
        stack.append(i)
    elif e == ')':
        if i == stack[-1]+1: # 연속
            stack.pop()
            sum += len(stack)
        else:
            stack.pop()
            sum += 1
print(sum)


#(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()(()()))(())()))(()())