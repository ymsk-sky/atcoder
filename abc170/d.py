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

n=int(input())
l=sorted(list(map(int,input().split())),reverse=True)
cnt=0
for i,a in enumerate(l[:-1]):
    x=set(l[i+1:])
    y=set(md(a))
    if len(x)+len(y)==len(x|y):
        cnt+=1
if l[-1]!=l[-2]:
    cnt+=1
print(cnt)
