from collections import deque
n,q=map(int,input().split())
abl=[list(map(int,input().split())) for _ in range(n-1)]
cdl=[list(map(int,input().split())) for _ in range(q)]
graph=[[] for _ in range(n+1)]  # graph[i]: iから繋がっている街一覧(graph[0]不使用)
for a,b in abl:
    graph[a].append(b)
    graph[b].append(a)
calced=[[] for _ in range(n+1)]
for c,d in cdl:
    if len(calced[c])!=0:
        if calced[c][d]%2==0:
            print('Town')
        else:
            print('Road')
        continue
    elif len(calced[d])!=0:
        if calced[d][c]%2==0:
            print('Town')
        else:
            print('Road')
        continue
    dist=[-1]*(n+1)
    dist[0]=0  # 不使用
    dist[c]=0
    dq=deque([c])
    while dq:
        v=dq.popleft()
        for i in graph[v]:
            if dist[i]>-1:
                continue
            dist[i]=dist[v]+1
            dq.append(i)
    if dist[d]%2==0:
        print('Town')
    else:
        print('Road')
    calced[c]=dist
