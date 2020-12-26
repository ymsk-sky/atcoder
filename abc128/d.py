n,k=map(int,input().split())
vs=list(map(int,input().split()))
r=min(n,k)  # 操作(A+B)の最大操作回数
ans=0
for a in range(r+1):  # 右から取り出す回数
    for b in range(r+1-a):  # 左から取り出す回数
        picked=sorted(vs[:b]+vs[n-a:])
        tmp=sum(picked)  # 取り出しただけのときのans
        rn=min(k-(a+b),len(picked))  # 戻す最大操作回数
        for i in range(rn):  # 取り出したマイナスのものをできるだけ戻す
            p=picked[i]
            if p<0:
                tmp-=p
            else:
                break
        ans=max(ans,tmp)
print(ans)
"""
6 4
-10 8 2 1 2 6
"""
