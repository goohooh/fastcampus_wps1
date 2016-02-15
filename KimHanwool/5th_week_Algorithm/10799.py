
li = list(input())
st = []
result = 0

for index in range(len(li)):
    if(li[index] == "("):
        st.append(index)
    else:             #li[index] == ")"
        if (st[-1] == index-1):   #레이저
            st.pop()
            result += len(st)
        else:
            st.pop()
            result += 1
print (result)

