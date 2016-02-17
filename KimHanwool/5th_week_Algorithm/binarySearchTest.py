li = list(map(int, input().split()))


def bi(li, num):  #파이썬을 활용한 이진탐색
    left = 0        #left 인덱스 값
    right = len(li)-1 #right 인덱스 값

    while(left <= right):
        mid = (left+right)//2

        if(li[mid] == num):
            return True
        elif(num < li[mid]):
            right = mid-1
        else:
            left = mid+1

    return False

print(bi(li, 10))


