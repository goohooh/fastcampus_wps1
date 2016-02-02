def palindrom(str):

    length = len(str)
    mid = int(len(str)/2)
    is_palindrom = True

    for index in range(mid):
        if(str[index] != str[length-index-1]):
            is_palindrom = False

    print (is_palindrom)

palindrom("eye")
