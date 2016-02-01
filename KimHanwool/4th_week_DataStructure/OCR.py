
def find(n):
    result = []
    for char in n:
        list = ['h', 'e']
        #print(char)
        if char in list:
            result.append(char)

    return result

n = "heooooooooolllooohhhhhllooollololo"


print(find(n))