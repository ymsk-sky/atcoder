from math import sin,cos,pi
n=int(input())
x0,y0=map(int,input().split())
xn,yn=map(int,input().split())
# 中心点座標を求める
xc=(x0+xn)/2
yc=(y0+yn)/2
d=((x0-xc)**2+(y0-yc)**2)**(1/2)  # 中心との距離
deg=360/n  # ずらす角度
#rad=-deg*pi/180
x=cos(deg)*d
y=sin(deg)*d
print(x,y)

"""
4
1 1
2 2
"""
