n,m,q=map(int,input().split())
wvl=[list(map(int,input().split())) for _ in range(n)]
xl=list(map(int,input().split()))
for _ in range(q):
    l,r=map(int,input().split())
    xs=xl[:l-1]+xl[r:]
    #ans=0
    #print(ans)
