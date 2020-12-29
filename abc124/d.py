"""
長さnの01で構成された列sに対してk回以下の次の操作が可能
1<=l<=r<=nとなるlからr番目の01を反転させる
連続した1の最大長を求める
"""
n,k=map(int,input().split())
s=input()
s0=[len(x) for x in s.split('1') if not x=='']
s1=[len(x) for x in s.split('0') if not x=='']
k=min(k,len(s0))  # 1を0に反転する必要なし
ans=0
if s[0]!='1':
    s1.insert(0,0)
for i in range(len(s0)-k+1):
    tmp=sum(s0[i:i+k])+sum(s1[i:i+k+1])
    ans=max(ans,tmp)
print(ans)
"""
14 2
11101010110011
s0=['0', '0', '0', '00']
s1=['111', '1', '1', '11', '11']
8

s0=['0', '0', '0', '00']
s1=['111', '1', '11', '1']
011101011001
"""
