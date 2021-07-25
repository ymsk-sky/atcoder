from collections import deque
n,m=map(int,input().split())
abl=[list(map(int,input().split())) for _ in range(m)]
mod=10**9+7
graph=[[] for _ in range(n+1)]
for a,b in abl:
    graph[a].append(b)
    graph[b].append(a)
dist=[-1]*(n+1)
dist[0]=0
dist[1]=0
cnt=[0]*(n+1)
cnt[1]=1
dq=deque([1])
while dq:
    v=dq.popleft()
    for i in graph[v]:
        if dist[i]==-1:
            dist[i]=dist[v]+1
            dq.append(i)
            cnt[i]=cnt[v]
        elif dist[i]==dist[v]+1:
            cnt[i]+=cnt[v]
            cnt[i]%=mod
print(cnt[n])
