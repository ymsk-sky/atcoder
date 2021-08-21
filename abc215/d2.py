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
n,m=map(int,input().split())
al=list(map(int,input().split()))
bs=set()
for a in al:
    bs=bs|set(md(a))
l=[1]*(m+1)
l[0]=0
dd=[0]*(m+1)
dd[0]=1
for b in list(bs):
    if b==1 or b>m or dd[b]==1:
        continue
    tmp=b
    while tmp<m+1:
        dd[tmp]=1
        l[tmp]=0
        tmp+=b
print(sum(l))
for i,v in enumerate(l):
    if v==1:
        print(i)
