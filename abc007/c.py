from collections import deque
r,c=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
m=[input() for _ in range(r)]
visited=[[-1]*c for _ in range(r)]
sy-=1
sx-=1
gy-=1
gx-=1
def bfs(sy,sx,gy,gx,m,visited):
    visited[sy][sx]=0
    q=deque([])
    q.append([sy,sx])
    while q:
        y,x=q.popleft()
        if [y,x]==[gy,gx]:
            return visited[y][x]
        for i,j in [[0,1],[1,0],[0,-1],[-1,0]]:
            if m[y+i][x+j]=='.' and visited[y+i][x+j]==-1:
                visited[y+i][x+j]=visited[y][x]+1
                q.append([y+i,x+j])
print(bfs(sy,sx,gy,gx,m,visited))
