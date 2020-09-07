n,q=map(int,input().split())
d={k:0 for k in range(n)}
for _ in range(q):
    l,r=map(int,input().split())
    for i in range(l,r+1):
        d[i-1]+=1
for v in d.values():
    print(v%2,end='')
print('')
