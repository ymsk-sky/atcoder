import math
a,b,h,m=map(int,input().split())
pm=6*m
ph=30*h+m/2
d=min(abs(pm-ph),abs(ph-pm))
print((a**2+b**2-2*a*b*math.cos(math.radians(d)))**(1/2))
