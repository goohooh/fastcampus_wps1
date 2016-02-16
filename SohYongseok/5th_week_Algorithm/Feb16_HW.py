n,m = map(int,input().split())
a = list(map(int,input().split()))
l = 0
r = max(a)

ans = 0
def check(mid):
    ans = 0
    for x in a:
        if x >= mid:
            ans += (x-mid)
    if ans >= m:
        return True
    else:
        return False

while l <= r:
    mid = (l+r)//2
    if check(mid):
        ans = max(ans,mid)
        l = mid+1
    else:
        r = mid-1
print(ans)
