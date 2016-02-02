s = str(input())
ss=[]

for i in range(0, len(s)):
    if type(s[i]) == str:
        ss[i] = ord(s[i])
        s[i] = chr(ss[i])
    else:
        pass
print(s)