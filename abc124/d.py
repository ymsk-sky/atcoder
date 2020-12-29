"""
長さnの01で構成された列sに対してk回以下の次の操作が可能
1<=l<=r<=nとなるlからr番目の01を反転させる
連続した1の最大長を求める
"""
n,k=map(int,input().split())
s=input()
ans=0
cnt=0  # 反転した連続した0の部分列
tmp=0
r=0
for l in range(n):
    bef='-1'
    while cnt<k:
        if r==n:
            break
        tmp+=int(s[r])
        if s[r]=='':
            r+=1
