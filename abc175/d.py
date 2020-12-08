n,k=map(int,input().split())
ps=list(map(int,input().split()))  # 順列
cs=list(map(int,input().split()))  # マスのスコア
ans=0
scores=[[0]*n]*n
for i in range(n):
    for _ in range(n):
        j=ps[i]
    scores[i][j]
print(scores)
"""
n=3
i: 0 1 2
j: 0 1 2
i+j: 0 1 2, 1 2 0, 2 0 1

5 2
2 4 5 1 3
3 4 -10 -8 8
8

5 5
2 3 4 5 1
-1 2 3 -3 2
1: 2 5 2 4 3 | 5 8 5 7 6 |
2: 3 0 2 1 3
3: -3 -1 -2 0 3
4: 2 1 3 6 3
5: -1 1 4 1 3
"""
