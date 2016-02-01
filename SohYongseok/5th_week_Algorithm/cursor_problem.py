s = input()
n = int(input())

left_stack = []
right_stack = []

left_stack = list(s)
while True:
    cmd = input().split(' ')
    print(cmd)
    if cmd[0] == 'P':
        left_stack+=cmd[1]
    elif cmd[0] == 'L':
        if len(left_stack)>0:
            right_stack+= left_stack.pop()
        else:
            pass
    elif cmd[0] == 'D':
        if len(right_stack)>0:
            left_stack+=right_stack.pop()
        else:
            pass
    elif cmd[0] == 'B':
        if len(left_stack)>0:
            left_stack.pop()
        else:
            pass
    n -= 1
    if n == 0:
        break
    print(left_stack,right_stack)

left_stack = ''.join(left_stack)
right_stack = ''.join(right_stack)
print(left_stack+right_stack[::-1])

