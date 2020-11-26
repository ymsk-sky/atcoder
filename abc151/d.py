from collections import deque
h,w=map(int,input().split())
m=[input() for _ in range(h)]
ans=0
def bfs(cx,cy,visited):
    tmp=0
    visited[cy][cx]=0
    q=deque([])
    q.append([cy,cx])
    while q:
        y,x=q.popleft()
        for i,j in [[0,1],[1,0],[0,-1],[-1,0]]:
            if y+i<0 or y+i>=h or x+j<0 or x+j>=w:
                continue
            if m[y+i][x+j]=='.' and visited[y+i][x+j]==-1:
                d=visited[y][x]+1
                visited[y+i][x+j]=d
                tmp=max(tmp,d)
                q.append([y+i,x+j])
    return tmp

for y in range(h):
    for x in range(w):
        if m[y][x]=='#':
            continue
        visited=[[-1]*w for _ in range(h)]
        tmp=bfs(x,y,visited)
        ans=max(ans,tmp)
print(ans)
