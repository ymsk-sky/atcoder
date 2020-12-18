from itertools import product
d,g=map(int,input().split())
pcs=[list(map(int,input().split())) for _ in range(d)]  # p:問題数, c:全問ボーナス
ans=float('inf')  # min(cnt)
for pt in product((0,1),repeat=d):
    cnt=0  # 個数
    s=0  # 点数
    for i,b in enumerate(pt):
        if b==1:
            p,c=pcs[i]
            cnt+=p
            s+=c+(i+1)*100*p
    if s<g and sum(pt)!=d:  # 目標に達していないとき中途半端に解く
        j=d-pt[::-1].index(0)-1  # 中途半端に解く問題インデックス
        p,_=pcs[j]
        for _ in range(p):
            cnt+=1
            s+=(j+1)*100
            if s>=g:
                break
    if s>=g:
        ans=min(ans,cnt)
print(ans)
