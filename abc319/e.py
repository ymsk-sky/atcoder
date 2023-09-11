n, x, y = map(int, input().split())
ptl = [list(map(int, input().split())) for _ in range(n - 1)]

ml = [0] * 9  # ml[i]: バス停1に到着後i分待機した後バス停1~nを乗り継いだ場合の合計時間
for i in range(9):
    s = 0
    bef = i
    for p, t in ptl:
        s += t
    ml[i] = s

ans = []
for _ in range(int(input())):
    q = int(input())
    w = 0
    tmp = x + w + ml[0] + y
    ans.append(tmp)
print(*ans, sep="\n")
