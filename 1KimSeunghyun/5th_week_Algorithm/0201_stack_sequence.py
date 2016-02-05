class stack_method():
    def push(self, x):      #push 함수 구현
        stack.append(x)

    def pop(self):          #pop 함수 구현
        print (stack[len(stack)-1])
        del stack[len(stack)-1]

    def sol(self, s):
        stack_method.push(s)

n = int(input())
stack=[]
for i in range(1, n+1): #입력받은 n까지 stack 생성
    stack.append(i)


print(stack)