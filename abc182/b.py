n=int(input())
l=list(map(int,input().split()))
d={}
def md(n):
    l,u=[],[]
    i=1
    while i*i<=n:
        if n%i==0:
            l.append(i)
            if i!=n//i:
                u.append(n//i)
        i+=1
    return l+u[::-1]
for v in l:
    ks=md(v)
    for k in ks:
        if k==1:
            continue
        if k in d:
            d[k]+=1
        else:
            d[k]=1
print(max(d,key=d.get))
