#postfix -> 후위 표기법을 말합니다.
#후위 표기법은 바이너리 트리에서 postorder로 값을 배열시킨 것을 말합니다.


# def inorder_to_postorder(exp):
#     operator = "+-*/()"                     # 연산자들을 선언
#     result = list()                     # 후위 표기법으로 결과가 저장되는 리스트
#     stack = list()                      # list를 스택으로 사용함.
#     for symbol in exp:
#         if symbol not in operator:          # 숫자일 경우 바로 결과리스트에 넣는다.
#             result.append(symbol)
#         else:
#             if symbol in "+-*/":        # 더하기, 빼기, 곱하기, 나누기 연산자일 경우
#                 stack.append(symbol)    # 후위 표기법으로 변환하기 위하여 우선 별도 스택에 임시로 저장.
#             elif symbol == ")":         # 닫는 괄호 ) 일 경우 저장해 연산자 하나를 결과리스트에 추가한다.
#                 result.append(stack.pop())      # 이 때 pop()을 통해 스택을 하나 비운다.
#     while len(stack) != 0:              # 스택에 남아 있는 연산자들을 pop()으로 하나씩 결과리스트에 붙여주면
#         result.append(stack.pop())      # 중위 표기법에서 후위 표기법으로 변환 완료!
#     return ''.join(result)
#
# print(inorder_to_postorder('(((9+9)*4)-((3-1)*2))'))
#get_postfix = inorder_to_postorder('(((9+9)*4)-((3-1)*2))')


##위 함수는 계산기를 만드는 프로그램입니다. 후위표기식을 통해서 괄호에 따른 계산식을 정리하고
##조건에 맞춰서 연산을 해서 출력합니다.
def postfix(num):
    post_list =[]
    post_operator=[]
    operator = {'+':1, '-':1, '*':2, '/':2}


    for i in num:
        if i in operator:
            post_operator.append(i)
        else:
            if i is '(':
                pass

            elif i is not ')':
                post_list.append(i)
            elif i is ')':
                post_list.append(post_operator.pop())

    return "".join(post_list)


a=postfix('((1+4)*3)-((5+1)*2))')
print(a)


def cal(a):
    result_vistion = []
    operator ='+-*/'

    for i in a:
        if i not in operator:
            result_vistion.append(i)
        elif i is '+':
            num1 = int(result_vistion.pop())
            num2 = int(result_vistion.pop())
            result_vistion.append(num1+num2)

        elif i is '-':
            num1 = int(result_vistion.pop())
            num2 = int(result_vistion.pop())
            result_vistion.append(num2-num1)

        elif i is '*':
            num1 =int(result_vistion.pop())
            num2 = int(result_vistion.pop())
            result_vistion.append(num1*num2)

        elif i is '/':
            num1 = int(result_vistion.pop())
            num2 = int(result_vistion.pop())
            result_vistion.append(num2/num1)

    return result_vistion

print(cal(a))