n,m = map(int,input().split())
tree =  list(map(int,input().split()))

min_t = 0
max_t = max(tree)
height = 0

def check_length(mid):
    length = 0

    for val in tree:
        if val > mid:
            length += (val-mid)

    if length >= m:
        return True
    else:
        return False


while min_t <= max_t:
    mid = (min_t+max_t)//2
    if check_length(mid):
        # 결국 이전 mid와 현재 mid의 값을 비교해 가장 높은 mid를 height 값으로 선정하는 것
        # 이 scope 안에 있다는 것 -> height를 계속 높여나갈 것이라는 것 -> 항상 height 보다 mid가 크지 않나?
        height = mid
        min_t = mid+1
    else:
        max_t = mid-1

print(height)