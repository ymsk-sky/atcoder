import sys
sys.setrecursionlimit(10**5)

n, h, w = map(int, input().split())
tiles = [list(map(int, input().split())) for _ in range(n)]
used = [0] * n
squares = [[0] * w for _ in range(h)]

def confirm():
    for i in range(h):
        for j in range(w):
            if squares[i][j] == 0:
                return
    print("Yes")
    exit()

def get_position():
    for i in range(h):
        for j in range(w):
            if squares[i][j] == 0:
                return (i, j)

def dfs(idx):
    used[idx] = 1
    a, b = tiles[idx]
    y, x = get_position()
    for _ in range(2):
        # 飛び出さないか確認
        if y + a <= h and x + b <= w:
            # 置く予定のマスに何もないか
            can = True
            for i in range(y, y + a):
                for j in range(x, x + b):
                    if squares[i][j] == 1:
                        can = False
                        break
                if not can:
                    break
            if can:
                # 置く
                for i in range(y, y + a):
                    for j in range(x, x + b):
                        squares[i][j] = 1
                confirm()
                for jdx in range(n):
                    if used[jdx]:
                        continue
                    dfs(jdx)
                # どかす
                for i in range(y, y + a):
                    for j in range(x, x + b):
                        squares[i][j] = 0
        a, b = b, a
    used[idx] = 0

for idx in range(n):
    dfs(idx)
print("No")

"""
1<=n<=7
1<=h,w<=10
1<=a,b<=10

7! * h*w * h*w
10**4 * 5040 = 5*10**7
min((i, j))の空いているマスに配置していく
"""