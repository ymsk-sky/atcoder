import math
a,b,x=map(int,input().split())
x/=a
if a*b/2<x:
    d=math.atan(2*(a*b-x)/a**2)
elif a*b/2>x:
    d=math.atan(b**2/2/x)
else:
    d=math.atan(b/a)
print(math.degrees(d))
