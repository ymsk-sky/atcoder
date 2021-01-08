n,m=map(int,input().split())
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
l=md(m)
l=[v for v in l if v<=m/n]
print(max(l))
