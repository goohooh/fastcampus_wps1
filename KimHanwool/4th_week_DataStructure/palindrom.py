
str = input()

length = len(str)
mid = int(len(str)/2)
is_palindrom = True

for index in range(mid):
    if(str[index] != str[length-index-1]):
        is_palindrom = False

if(is_palindrom == True):
    print("1")
else:
    print("0")

