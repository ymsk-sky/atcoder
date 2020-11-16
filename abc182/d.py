n=int(input())
al=list(map(int,input().split()))
ps=[0]*n  # 合計変化
qs=[0]*n  # 最大座標
p=0
q=0
for i,a in enumerate(al):
    p+=a
    q=max(q,p)
    ps[i]=p
    qs[i]=q
ans=0
x=0  # 現在位置
for p,q in zip(ps,qs):
    ans=max(ans,x+q)
    x+=p
print(ans)
