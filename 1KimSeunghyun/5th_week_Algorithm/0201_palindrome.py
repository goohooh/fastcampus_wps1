str = input()
cnt = 0
for i in range(0, len(str)):
    if str[i] == str[len(str)-(1+i)]:
        cnt += 1
    else:
        pass

if cnt == len(str):
    print (1)
else:
    print (0)