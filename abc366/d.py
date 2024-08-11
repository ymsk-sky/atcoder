n = int(input())
al = [[[0] * (n + 1) for _ in range(n + 1)]]
for _ in range(n):
    l = [[0] * (n + 1)]
    for _ in range(n):
        tmp = [0] + list(map(int, input().split()))
        l.append(tmp)
    al.append(l)
q = int(input())
ql = [list(map(int, input().split())) for _ in range(q)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            al[i][j][k] += al[i - 1][j][k]
for j in range(1, n + 1):
    for i in range(1, n + 1):
        for k in range(1, n + 1):
            al[i][j][k] += al[i][j - 1][k]
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            al[i][j][k] += al[i][j][k - 1]

for lx, rx, ly, ry, lz, rz in ql:
    ans = (al[rx][ry][rz]
           - al[rx][ry][lz - 1]
           - al[rx][ly - 1][rz] + al[rx][ly - 1][lz - 1]
           - al[lx - 1][ry][rz] + al[lx - 1][ly - 1][rz] + al[lx - 1][ry][lz - 1] - al[lx - 1][ly - 1][lz - 1])
    print(ans)
