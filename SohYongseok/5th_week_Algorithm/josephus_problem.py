# n, c = map(int, input().split())
#
# table = list(range(1,n+1))
#
# order = ''
# counter = 0
# while(len(table)!=1):
#     cnt = 1
#     while(cnt!=c):
#         table.append(table[0])
#         table.pop(0)
#         cnt += 1
#     order += str(table.pop(0))+", "
#     counter += 1
#
# order += str(table.pop(0))
# counter += 1
#
# print("<{}>".format(order))
# print(counter)


#queue = list(strrange(1, str(q+1)))
queue = ["1","2","3","4","5","6","7","8","9","10"]
print(queue)
print("len",len([10]))

result = list()
for i in range(0,10-1):
   for j in range(0, 3-1):
       queue.append(queue[0])
       del queue[0]
   print(queue[0])
   result += str(queue[0])
   del queue[0]
   if len(queue) == 1:
       result += queue
   else:
       pass
print("<"+', '.join(result)+">")