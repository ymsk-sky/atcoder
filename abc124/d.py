"""
長さnの01で構成された列sに対してk回以下の次の操作が可能
1<=l<=r<=nとなるlからr番目の01を反転させる
連続した1の最大長を求める
"""
n,k=map(int,input().split())
s=input()
l=[]
if s[0]!='1':
    l.append(0)
bef=s[0]
cnt=1
for v in s[1:]:
    if v==bef:
        cnt+=1
    else:
        l.append(cnt)
        cnt=1
    bef=v
l.append(cnt)
ans=0
for i in range(0,len(l),2):
    ans=max(ans,sum(l[i:i+2*k+1]))
print(ans)
"""
14 2
11101010110011
3 1 1 1 1 1 2 2 2
3+1+1+1+1 = 7
1+1+1+1+2 = 6
1+1+2+2+2 = 8
"""
