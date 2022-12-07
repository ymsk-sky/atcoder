from math import sin, cos, radians

n = int(input())
x0, y0 = map(int, input().split())
xh, yh = map(int, input().split())

xc, yc = (x0 + xh)/2, (y0 + yh)/2  # 中心
# 中心点分ずらす
x0 -= xc
y0 -= yc
deg = 360 / n
rad = radians(deg)  # 度->ラジアン

x = x0*cos(rad) - y0*sin(rad)
y = x0*sin(rad) + y0*cos(rad)
# 中心点分戻す
x += xc
y += yc
print(x, y)