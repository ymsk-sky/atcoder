h, w, c = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(h)]
INF = float("inf")

def rotate_clockwise(h, w, al):
    """ al:listを時計回りに90度回転 """
    al = list(zip(*al[::-1]))
    al = [list(a) for a in al]
    # 90度回転によりwとhは入れ替わる
    return w, h, al

def solve(h, w, al):
    ml = [[0] * w for _ in range(h)]  # ml[i][j]: (i,j)以下の範囲での最小値
    for i in range(h):
        for j in range(w):
            ml[i][j] = al[i][j] - c*(i + j)
    for i in range(h):
        for j in range(w):
            if i > 0:
                if ml[i - 1][j] < ml[i][j]:
                    ml[i][j] = ml[i - 1][j]
            if j > 0:
                if ml[i][j - 1] < ml[i][j]:
                    ml[i][j] = ml[i][j - 1]
    res = INF
    for i in range(h):
        for j in range(w):
            tmp = INF
            if i > 0:
                if tmp > ml[i - 1][j]:
                    tmp = ml[i - 1][j]
            if j > 0:
                if tmp > ml[i][j - 1]:
                    tmp = ml[i][j - 1]
            res = min(res, al[i][j] + c*(i + j) + tmp)
    return res

ans = INF
for _ in range(2):
    ans = min(ans, solve(h, w, al))
    h, w, al = rotate_clockwise(h, w, al)
print(ans)

"""
2<=h,w<=1000
1<=c<=10**9
1<=a<=10**9

(i,j)->(k,l): c*(|i-k|+|j-l|) + al[i][j] + al[k][l]
i>=k and j>=lと仮定すると
絶対値は (i-k)+(j-l)で考えられるので
c*(i-k+j-l)+al[i][j]+al[k][l]
= al[i][j]+c*(i+j) + al[k][l]-c*(k+l)
よって(i,j)を固定して, i>=k and j>=lを満たす範囲内で最小のal[k][l]-c*(k+l)を見つける
これは累積和のような感じでテーブルをもつことで達成可能

3 4 2
1 7 7 9
9 6 3 7
7 8 6 4
10
"""
