# def factorial(num):
#     if num == 0:
#         return 1
#
#     total = 1
#
#     for number in range(1,(num+1)):
#         total *= number
#
#     return total
#
# #print(factorial(5))
#
#
#
# def hanoi(n, start=1, end=3):
#     if n:
#         hanoi((n-1),start,6-start-end)
#         print("%d번 디스크를 %d번에서 %d으로 이동" %(n,start,end))
#         hanoi((n-1),6-start-end,end)
#
#
# hanoi(4)
#
#
#

def inorder_to_postorder(exp):
    operator = "+-*/()"                     # 연산자들을 선언
    result = list()                     # 후위 표기법으로 결과가 저장되는 리스트
    stack = list()                      # list를 스택으로 사용함.
    for symbol in exp:
        if symbol not in operator:          # 숫자일 경우 바로 결과리스트에 넣는다.
            result.append(symbol)
        else:
            if symbol in "+-*/":        # 더하기, 빼기, 곱하기, 나누기 연산자일 경우
                stack.append(symbol)    # 후위 표기법으로 변환하기 위하여 우선 별도 스택에 임시로 저장.
            elif symbol == ")":         # 닫는 괄호 ) 일 경우 저장해 연산자 하나를 결과리스트에 추가한다.
                result.append(stack.pop())      # 이 때 pop()을 통해 스택을 하나 비운다.
    while len(stack) != 0:              # 스택에 남아 있는 연산자들을 pop()으로 하나씩 결과리스트에 붙여주면
        result.append(stack.pop())      # 중위 표기법에서 후위 표기법으로 변환 완료!
    return ''.join(result)



def claculate(postorder):
    operator = "+-*/"
    num_stack = list() # 숫자 넣는 스택
    opt_stack = list() # 연산자 스택

    for char in postorder:
        if char not in operator: # 숫자이면
            num_stack.append(int(char)) # 숫자 스택에 정수로 추가
        else: # 숫자가 아닌 연산자이면
            opt_stack.append(char) # 연산자 스택에 추가

        # 숫자 스택에 숫자가 2개 이상이고 연산자 스택에 연산자가 1개 이상 있으면 실행
        if len(num_stack) >= 2 and len(opt_stack) >= 1:
            second = num_stack.pop() # 맨 위의 숫자 빼오기
            first = num_stack.pop() # 그 다음 숫자 빼오기
            opt = opt_stack.pop() # 맨 위의 연산자 빼오기
            new_num = 0

            if opt is '+':
                new_num = first + second
            elif opt is '-':
                new_num = first - second
            elif opt is '*':
                new_num = first * second
            else:
                new_num = first / second

            # 계산한 값을 숫자 스택에 다시 추가
            num_stack.append(new_num)

    # for문이 끝나면 마지막 결과값을 리턴
    else:
        return num_stack[0]


calc = "((((3+1)*3)/((9-5)+2))-((3*(7-4))+6))"
result = inorder_to_postorder(calc)
print(result)
print(claculate(result))