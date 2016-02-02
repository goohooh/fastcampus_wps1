n = int(input())
cs = []
cs.append(n)

for i in range(1, n):
    s = int(input())
    cs.append(s)

max1 = 0
max2 = 0

for i in range(0, n):
    if (cs[i] > max1):
        max1 = cs[i]
    else:
        pass
for i in range(0, n):
    if (cs[i] > max2):
        if max2 < max1:
            max2 = cs[i]
    else:
        pass

print(cs)
print (max1)
print (max2)