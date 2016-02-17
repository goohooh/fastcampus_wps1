#https://www.acmicpc.net/problem/2156
#연속해서 3잔을 마시면 안된, 이 조건을 지키며 최대로 많이 마시는 방법
wine = [0 for _ in range(10001)] #와인잔 수
drink = [0 for _ in range(10001)] #와인잔 갯수에 따른 최대로 마실 양


cnt = int(input()) #몇찬인지
for i in range(1, cnt+1):
    wine[i] = int(input())

drink[1] = wine[1]
drink[2] = wine[1] + wine[2]

for i in range(3, cnt+1):
    drink[i] = max(drink[i-1], drink[i-2]+wine[i], drink[i-3]+wine[i-1]+wine[i])

print(drink[cnt])


