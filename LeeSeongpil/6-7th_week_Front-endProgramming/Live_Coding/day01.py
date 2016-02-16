n, m = map(int, input().split())
trees = list(map(int, input().split()))
""" 발상 1) 0에서 자르면 되지만 자연주의 상근이는 필요한 최소한의 나무만 얻을 수 있는 최대의 절단 높이가 필요 """
""" 발상 2) 답은 모른다. 최소와 최대값의 중간을 잘라서 얻고자하는 m과 비교하여 탐색 범위를 끝까지 좁혀 나간다. """
top = max(trees) # 일단 최대 최소값을 구함
bottom = 0

# 탐색 전 최대 절단 높이(출력해야할 답)
max_cut_height = 0 # 일단 현재 가장 쉽게 나무를 얻을 수 있는 높이 0

# 발상2)를 통해 절단할 중간값을 얻어야할 필요성을 얻음
#cut = (top + bottom)//2    # 발상6)의 이유로 주석처리(밑으로 내려감)
""" 발상 3) 중간값으로 절단했을 때 얻은 나무가 m보다 작은지 큰지 확인할 필요성을 얻음 """
""" 발상 4) m보다 작으면 탐색 범위의 최대값을 낮추고(절단 높이(=중간값)가 낮을 수록 얻을 나무가 많아지므로) """
"""         m보다 크면 탐색 범위의 최소값을 올려 다시 중간 탐색( 유효한 범위므로 다시 최대값을 얻기위한 도전이 가능하다 ) """
# 발상3)으로 인해 확인을 위한 동작이 필요함. 함수를 만든다
def cutter(cut_height):
    #잘랐을 때 얻을 수 있는 나무
    getTree = 0
    for tree in trees:
        # 나무 높이가 절단 높이 보다 커야 얻을 나무가 생긴다
        if tree > cut_height:
            getTree += tree - cut_height
    if getTree >= m:
        return True
    else:
        return False

#발상6) 이후에 while문으로 감싼다
while bottom <= top:
    cut = (top + bottom)//2
    """ 발상 5) 커터함수 값이 참이면 발상4)에 의해 범위의 최소값(= bottom)을 갱신, 반대는 최대값(top)을 갱신 """
    """         최소값 = 절단값 + 1 /  최대값 = 절단값 - 1 // 절단 값은 탐색범위에서 제외하므로 """
    if cutter(cut):
        # getTree가 얻고자 하는 m보다 크거나 같을 때
        # 수근이가 원하는 값은 절단 높이 중에서도 최대값이므로 max 메서드를 통해 비교하여 기록한다
        # 이전 컷과 현재컷 높이의 비교
        max_cut_height = max(max_cut_height, cut)
        bottom = cut + 1
    else:
        top = cut - 1
""" 발상 6) loop의 필요(발상5 윗줄에 while문을 추가함) 인덴트 변경 필요 """
"""         조건문은 탐색의 범위의 극소까지 => bottom과 top 값이 역전되기 전까지 """
"""         cut 값 갱신을 위해 cut 할당문을 while문 안으로 내림 """



print(max_cut_height)
