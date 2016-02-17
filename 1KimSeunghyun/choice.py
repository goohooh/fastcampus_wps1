import random

lst = ["김예찬", "김한울", "박승권", "서은정", "소용석", "유동현", "이성필", "이정현", "전명훈", "한아름", "한민수"]
random.shuffle(lst)

for i in range(0, 1):
    print (lst.pop())