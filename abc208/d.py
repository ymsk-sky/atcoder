n,m=map(int,input().split())
abcl=[list(map(int,input().split())) for _ in range(m)]

dp=[[[0]*n for _ in range(n)] for _ in range(n)]  # dp[A-1][B-1][C-1]: A->BへのC以下を通っての最短時間

def f(s,t,k):  # s->tへk以下の都市のみを通っての最短時間
    if s==t: return 0
    if dp[s-1][t-1][k-1]>0: return dp[s][t][k]
    return 1

ans=0
for s in range(1,n+1):
    for t in range(1,n+1):
        for k in range(1,n+1):
            ans+=f(s,t,k)
print(ans)
