from itertools import product
n=int(input())  # 人数
evidences=[]
for _ in range(n):
    a=int(input())  # 証言数
    # xはyである(x:人, y:1のとき正直、０のとき不親切)
    tmp=[-1]*n
    for _ in range(a):
        x,y=map(int,input().split())
        tmp[x-1]=y
    evidences.append(tmp)
ans=0
for p in product((0,1),repeat=n):
    sum_=sum(p)  # 正直者の数
    cnt=0
    for i,q in enumerate(p):
        if q==1:
            evidence=evidences[i]
            for x,y in enumerate(evidence):
                if y!=-1 and p[x]!=y:
                    break
            else:
                cnt+=1
    if sum_==cnt:
        ans=max(ans,sum_)
print(ans)
