r = int(input()) * 2
r2 = r**2
ans = 0
def f(v: float) -> int:
    v = int(v)
    if v % 2 == 0:
        if v > 0:
            return v - 1
        else:
            return v + 1
    else:
        return v

for y in range(r, -r + 2, -2):
    y1, y2 = y - 1, y - 3
    x1 = (r2 - y1**2)**0.5
    x1_l, x1_r = f(-x1), f(x1)
    x2 = (r2 - y2**2)**0.5
    x2_l, x2_r = f(-x2), f(x2)
    ans += min((x1_r - x1_l) // 2, (x2_r - x2_l) // 2)
print(ans)


"""
x**2 + y**2 = r**2
x**2 = r**2 - y**2
x = (r**2 - y**2)**0.5
"""
