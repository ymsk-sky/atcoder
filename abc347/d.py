a, b, c = map(int, input().split())
c_cnt = bin(c).count("1")
share = 0
ok = False
for _ in range(61):
    if c_cnt == a + b:
        ok = True
        break
    a -= 1
    b -= 1
    share += 1
    if a < 0 or b < 0:
        break
if not ok:
    print(-1)
    exit()
x = [0] * 60
y = [0] * 60
x_cnt = 0
y_cnt = 0
for i, k in enumerate(bin(c)[2:].zfill(60)):
    if k == "1":
        if x_cnt < a:
            x[i] = 1
            x_cnt += 1
        else:
            y[i] = 1
            y_cnt += 1
if x_cnt != a or y_cnt != b:
    print(-1)
    exit()
xy_cnt = 0
ok = False
for i in range(59, -1, -1):
    if xy_cnt == share:
        ok = True
        break
    if x[i] == y[i] == 0:
        x[i] = y[i] = 1
        xy_cnt += 1
    if xy_cnt == share:
        ok = True
        break
if not ok:
    print(-1)
    exit()
x = int("".join([str(k) for k in x]), 2)
y = int("".join([str(k) for k in y]), 2)
if x >= 2**60 or y >= 2**60:
    print(-1)
    exit()
print(x, y)
print(bin(x), bin(y))
print((x ^ y))

"""
0 <= a,b <= 60
0 <= c < 2**60
"""