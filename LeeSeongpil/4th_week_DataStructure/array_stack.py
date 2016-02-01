class Empty(Exception):
    pass

class ArrayStack:
    #기본 리스트 선언(스택으로 담을 상자)
    def __init__(self):
        self.data = []
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    def push(self, e):
        self.data.append(e)
    def top(self):
        if self.is_empty() == True:
            return 'empty list'
        else:
            return self.data[-1] #마지막 요소 반환 - 리스트 사용법에 익숙해 지자!!

    def pop(self):
        if self.is_empty() == True:
            print('empty list')
        else:
            returnData = self.data[-1]
            # self.data.pop() #구현하는 의미가 없다
            self.data = self.data[:-1] #슬라이스 활용. 덮어쓰기
            return returnData


aso = ArrayStack()

aso.push(2)
aso.push(5)
aso.push(7)
print(aso.data)
print(aso.pop())
print(aso.data)
