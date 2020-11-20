from collections import deque
h,w=map(int,input().split())
ch,cw=map(int,input().split())
dh,dw=map(int,input().split())
m=[[c for c in input()] for _ in range(h)]
visited=[[-1]*w for _ in range(h)]
ch,cw,dh,dw=ch-1,cw-1,dh-1,dw-1

def bfs(ch,cw,cost):
    visited[ch][cw]=cost
    q=deque([])
    q.append([ch,cw])
    while q:
        y,x=q.popleft()
        for i,j in [[0,1],[1,0],[0,-1],[-1,0]]:
            if m[y+i][x+j]=='.' and visited[y+i][x+j]==-1:
                visited[y+i][x+j]=cost
                q.append([y+i,x+j])
            elif True:
                pass
