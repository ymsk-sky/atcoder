n=int(input())
al=list(map(int,input().split()))
l=al[:]
for _ in range(n-1):
    gu=l[1::2]
    ki=l[0::2]
    tmp=[]
    for g,k in zip(gu,ki):
        v=max(g,k)
        tmp.append(v)
    l=tmp[:]
print(al.index(min(l))+1)
