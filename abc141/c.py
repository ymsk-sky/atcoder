n,k,q=map(int,input().split())
as_=[int(input()) for _ in range(q)]
ps=[k-q]*n
for a in as_:
    ps[a-1]+=1
for p in ps:
    print('Yes'if p>0 else 'No')
