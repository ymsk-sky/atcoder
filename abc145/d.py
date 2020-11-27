"""
(i,j)->(i+1,j+2)
(i,j)->(i+2,j+1)
(X,Y)までの移動方法は何通りか
"""
from collections import deque
mod=10**9+7
X,Y=map(int,input().split())
dp=[[0]*(X+1) for _ in range(Y+1)]
dp[0][0]=1
q=deque([])
q.append([0,0])
while q:
    x,y=q.pop()
    ax,ay=x+1,y+2
    bx,by=x+2,y+1
    v=dp[y][x]%mod
    if ax<=X and ay<=Y:
        init=dp[ay][ax]
        dp[ay][ax]+=v
        if init==0:
            q.append([ax,ay])
    if bx<=X and by<=Y:
        init=dp[by][bx]
        dp[by][bx]+=v
        if init==0:
            q.append([bx,by])
print(dp[Y][X]%mod)
