n,q=map(int,input().split())
d=[0]*(n+1)
for _ in range(q):
    l,r=map(int,input().split())
    d[l-1]+=1
    d[r]-=1
for i,v in zip(range(1,n),d):
    d[i]+=v
for v in d[:-1]:
    print(v%2,end='')
print('')
