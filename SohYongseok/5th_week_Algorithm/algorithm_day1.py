
# x,y = map(int, input().split())
#
# ans = x*y
# min = ans
# for i in range(2, ans):
#     if ans%i is 0:
#         pair1 = i
#         pair2 = int(ans/i)
#         if pair1+pair2 < min:
#             min = pair1 + pair2
#             min_pair = (pair1, pair2)
#
# print(min_pair[0], min_pair[1])

# x,y = map(int, input().split())
# days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
# days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# print(days[(sum(days_in_month[0:x])+y) % 7])



# n = int(input())
# i = 0
# while i <= n:
#     buf_star = ''
#     buf_blank = ''
#     for m in range(0,n-i):
#         buf_blank += "*"
#     for l in range(1,i+1):
#         buf_star += " "
#     print(buf_star+buf_blank)
#     i += 1

# n = int(input())
# for i in range(1,n+1):
#     buf_blank = " "* (n-i)
#     buf_star = "*"* (i)
#     print(buf_star+buf_blank*2+buf_star)
# for i in range(n-1,0,-1):
#     buf_blank = " "* (n-i)
#     buf_star = "*"* (i)
#     print(buf_star+buf_blank*2+buf_star)
# for i in range(1,n):
#     buf_blank = " "* i
#     buf_star = "*"* (2*(n-i)-1)
#     print(buf_blank+buf_star)


# n = int(input())
# for i in range(1,n+1):
#     buf_blank = " "* (i-1)
#     buf_star = "*"* (2*(n-i)+1)
#     print(buf_blank+buf_star)
# for i in range(0,n-1):
#     buf_blank = " "* (n-(i+2))
#     buf_star = "*"* (2*(i+1)+1)
#     print(buf_blank+buf_star)

   # ***********
   #   *********
   #    *******
   #     *****
   #      ***
   #       *
   #      ***
   #     *****
   #    *******
   #   *********
   #  ***********


# n = int(input())
# for i in range(1,n+1):
#     buf_blank = " "* (n-i)
#     buf_star = "*"* (i)
#     print(buf_blank+buf_star)
# for i in range(n-1,0,-1):
#     buf_blank = " "* (n-i)
#     buf_star = "*"* (i)
#     print(buf_blank+buf_star)

#   *
#  **
# ***
#  **
#   *
#
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


# n = int(input())
# cnt = 0
# for i in range(1,n):
#     buf_blank = " "* (n-i)
#     buf_space = " " * (2*cnt-1)
#     buf_star = "*"
#     if i is 1:
#         print(buf_blank+buf_star)
#     else:
#         print(buf_blank+buf_star+buf_space+buf_star)
#     cnt += 1
#
# print("*"*(2*n-1))

#          *
#         * *
#        *   *
#       *     *
#      *       *
#     *         *
#    *           *
#   *             *
#  *               *
# *******************



#    *
#   * *
#  * * *
# * * * *

x = 180000000
y = 6000000

x,y = map(int, input().split())
min_val = x*y
ans = int(y/x)
for i in range(1, ans):
    if ans%i == 0:
        pair1 = i
        pair2 = int(ans/i)
        if pair1+pair2 <= min_val:
            min_val = pair1 + pair2
            min_pair = (pair1, pair2)

big_n = max(min_pair)*x
small_n = min(min_pair)*x
print(small_n, big_n)