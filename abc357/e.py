"""Functional Graph
- 各連結成分には閉路が1つだけ
"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())
al = list(map(int, input().split()))

vis = [False] * n
nums = [-1] * n
loop = []
def dfs(u):
    """ループを作る. ループの起点を返す"""
    global loop
    v = al[u] - 1
    if vis[v]:
        if nums[v] == -1:
            # 訪問済みだが確定していない = ループ開始
            loop = [v]
            return v
        else:
            # 既に存在するループ
            nums[u] = nums[v] + 1
            return -1
    else:
        vis[v] = True
        st = dfs(v)
        if st == -1:
            # ループに入る箇所
            if nums[v] != -1 and nums[u] == -1:
                nums[u] = nums[v] + 1
            return -1
        elif st == v:
            # ループ一巡
            l = len(loop)
            for x in loop:
                nums[x] = l
            if nums[u] == -1:
                nums[u] = nums[v] + 1
            loop = []
            return -1
        else:
            # vはループの途中なので引き続き探索
            loop.append(v)
            return st

for i in range(n):
    if vis[i]:
        continue
    dfs(i)

ans = sum(nums)
print(ans)


"""
1<=n<=2*10**5
1<=a<=n
"""