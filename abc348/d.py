import heapq

h, w = map(int, input().split())
al = [input() for _ in range(h)]
n = int(input())
medicines = [[0] * w for _ in range(h)]
for _ in range(n):
    r, c, e = map(int, input().split())
    medicines[r - 1][c - 1] = e
for i in range(h):
    for j in range(w):
        if al[i][j] == "S":
            si, sj = i, j
        if al[i][j] == "T":
            gi, gj = i, j

# (i, j)に到達時のエネルギーの最大値(これ以下なら再度来る必要なし)
power = [[-1] * w for _ in range(h)]

que = [(0, si, sj)]
while que:
    energy, i, j = heapq.heappop(que)
    energy = -energy
    if i == gi and j == gj:
        print("Yes")
        exit()
    energy = max(energy, medicines[i][j])
    if power[i][j] >= energy:
        continue
    power[i][j] = energy
    for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        u, v = i + p, j + q
        if 0 > u or u >= h or 0 > v or v >= w:
            continue
        if al[u][v] == "#":
            continue
        if power[u][v] >= energy - 1:
            continue
        heapq.heappush(que, (-(energy - 1), u, v))
print("No")

"""
1<=h,w<=200
1<=n<=300
"""