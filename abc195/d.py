n,m,q=map(int,input().split())
wvl=[list(map(int,input().split())) for _ in range(n)]
wvl.sort(key=lambda x:x[1],reverse=True)
xl=list(map(int,input().split()))
for _ in range(q):
    l,r=map(int,input().split())
    xs=xl[:l-1]+xl[r:]
    ans=0
    for w,v in wvl:
        tmp_l=[x for x in xs if x>=w]
        if len(tmp_l)==0:
            continue
        xs.remove(min(tmp_l))
        ans+=v
    print(ans)
