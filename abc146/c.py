a,b,x=map(int,input().split())
l=0  # 下限
r=10**9+1  # 上限
m=0
while r-l>1:
    m=(l+r)//2
    d=len(str(m))
    v=a*m+b*d
    if v>x:
        r=m
    else:
        l=m
print(l)
