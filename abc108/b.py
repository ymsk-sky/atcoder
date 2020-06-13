x1,y1,x2,y2=map(int,input().split())
xd=x2-x1
yd=y2-y1
x3=x2-yd
y3=y2+xd
x4=x1-yd
y4=y1+xd
print(x3,y3,x4,y4)
