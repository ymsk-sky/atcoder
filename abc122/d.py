"""
- A,C,G,Tのみで構成されたn長の文字列
- AGC部分文字列を含まない
- 隣接する2文字を入れ替えても上記2つを満たす
を満たす文字列の数をmodで割った数を表示

AGC
ACG, GAC
A*GC, AG*C
を含まない
"""
n=int(input())
mod=10**9+7
memo=[{} for _ in range(n+1)]
def ok(l4):
    """AGC, 隣接した2文字を入れ替えたときにAGCが入ってないかを調べるのを実装
    i=0: そのまま確認
    i=1: 0と1番目を入れ替え
    i=2: 1と2番目を入れ替え
    i=3: 2と3番目を入れ替え
    どこかで条件を満たさないことが判明した時点でFalseを返す, 全部通ればTrue
    """
    for i in range(4):
        t=list(l4)
        if i>=1:
            t[i-1],t[i]=t[i],t[i-1]
        if ''.join(t).count('AGC')>=1:
            return False
    return True
def dfs(cur,l3):
    if l3 in memo[cur]:
        return memo[cur][l3]
    if cur==n:
        return 1
    ret=0
    for c in 'ACGT':
        if ok(l3+c):
            ret=(ret+dfs(cur+1,l3[1:]+c))%mod
    memo[cur][l3]=ret
    return ret
print(dfs(0,'TTT'))
