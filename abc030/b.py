n,m=map(int,input().split())
a=6*m
b=n%12*30+m/2
d=max(a,b)-min(a,b)
print(d if d<180 else 360-d)
