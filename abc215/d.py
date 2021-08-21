def md(n):
    l,u=[],[]
    i=1
    while i*i<=n:
        if n%i==0:
            l.append(i)
            if i!=n//i:
                u.append(n//i)
        i+=1
    return l+u[::-1]
n,m=map(int,input().split())
al=list(map(int,input().split()))
l=[1]*(m+1)  # ans
l[0]=0
dd=[0]*(m+1)  # 計算済
dd[0]=1
for a in al:
    mdl=md(a)  # 約数を計算
    for b in mdl:  # 約数ごとに確認
        if b>m:
            continue
        if b==1:  # 1は例外
            continue
        if dd[b]==1:  # 計算済ならスルー
            continue
        tmp=b
        while tmp<m+1:
            dd[tmp]=1
            l[tmp]=0
            tmp+=b
        #dd[b]=1
print(sum(l))
for i,v in enumerate(l):
    if v==1:
        print(i)

"""
3 12
6 1 5
#6 mdl=[1,2,3,6]
l =[0,1,0,1,0,1,0,1,0,1,0,1,0]
dd=[1,0,1,1,0,0,0,0,0,0,0,0,0]
"""
