n=int(input())
al=sorted(list(map(int,input().split())),reverse=True)
l=[]
b=al[0]
for a in al[1:]:
    l.append(abs(b-a))
ans=0
x=0
tmp=0
for i in range(n-1):
    ans+=sum(l[i:])-x*(n-i-1)
    tmp+=l[i]-x
    x=tmp
print(ans)
