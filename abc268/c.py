n = int(input())
pl = list(map(int, input().split()))

# 何回動かしたら喜ばれるかリスト（辞書）を作成する

d = {}
for i, p in enumerate(pl):
    dif = i - p
    for j in [-1, 0, 1]:
        dif2 = (dif + j) % n
        if dif2 in d:
            d[dif2] += 1
        else:
            d[dif2] = 1
print(max(d.values()))

"""
10
3 9 6 1 7 2 8 0 5 4
0 1 2 3 4 5 6 7 8 9
5

4
1 2 0 3
4

1 2 3 4 -> 2 3 4 1 -> 3 4 1 2 -> 4 1 2 3 -> ...
"""
