a,b,c,k=map(int,input().split())
s,t=map(int,input().split())
p=0 if s+t<k else (s+t)*c
print(a*s+b*t-p)
