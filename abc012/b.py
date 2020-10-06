n=int(input())
h=n//3600
n-=3600*h
m=n//60
n-=60*m
print('{:02}:{:02}:{:02}'.format(h,m,n))
