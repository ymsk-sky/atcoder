from itertools import combinations_with_replacement
n,m,q=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(q)]
# 長さn, 1<=Ai<=mとなる数列A={A1, A2, ..., An}を生成
ans=0
for al in list(combinations_with_replacement([i for i in range(1,m+1)],n)):
    tmp=0
    for a,b,c,d in l:  # O(q)
        if al[b-1]-al[a-1]==c:
            tmp+=d
    ans=max(ans,tmp)
print(ans)
"""
3 4 3
1 3 3 100
1 2 2 10
2 3 2 10

{1, 1, 1}, {1, 1, 2}, {1, 1, 3}, {1, 1, 4},
{1, 2, 2}, {1, 2, 3}, {1, 2, 4},
{1, 3, 3}, {1, 3, 4},
{1, 4, 4},
{2, 2, 2}, {2, 2, 3}, {2, 2, 4},
{2, 3, 3}, {2, 3, 4},
{2, 4, 4},
{3, 3, 3}, {3, 3, 4},
{3, 4, 4},
{4, 4, 4}

n個の仕切りとm-1個のボールを並び替えた列: (n+m-1)Cn通り
3個仕切り、3個ボールを並び替え: 6C3

"""
