n, X, Y = map(int, input().split())
al = list(map(int, input().split()))

x_axis = []
y_axis = []
for i in range(n):
    a = al[i]
    if i % 2 == 0:
        x_axis.append(a)
    else:
        y_axis.append(a)

lx = len(x_axis)
ly = len(y_axis)

M = 10 ** 4

# xdp[i][j]: (i+1)個目まででjに到達できるか * すべて+10**4して考える
xdp = [[0] * (2 * M + 1) for _ in range(lx)]
x = x_axis[0]
xdp[0][x + M] = 1
# xdp[0][-x + M] = 1
for i in range(1, lx):
    x = x_axis[i]
    for j in range(2 * M + 1):
        if xdp[i - 1][j] == 1:
            xdp[i][j + x] = 1
            xdp[i][j - x] = 1

ydp = [[0] * (2 * M + 1) for _ in range(ly)]
y = y_axis[0]
ydp[0][y + M] = 1
ydp[0][-y + M] = 1
for i in range(1, ly):
    y = y_axis[i]
    for j in range(2 * M + 1):
        if ydp[i - 1][j] == 1:
            ydp[i][j + y] = 1
            ydp[i][j - y] = 1

if (xdp[lx - 1][X + M] == 1)and (ydp[ly - 1][Y + M] == 1):
    print("Yes")
else:
    print("No")

"""
2<=n<=10**3
1<=a<=10
|x|,|y|<=10**4
"""
