h,w=map(int,input().split())
s=[input() for _ in range(h)]
l=[[-1]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j]=='#':
            l[i][j]=0
        elif j==0:
            l[i][j]=1
        else:
            l[i][j]=l[i][j-1]+1
r=[[-1]*w for _ in range(h)]
for i in range(h):
    for j in range(w-1,-1,-1):
        if s[i][j]=='#':
            r[i][j]=0
        elif j==w-1:
            r[i][j]=1
        else:
            r[i][j]=r[i][j+1]+1
u=[[-1]*w for _ in range(h)]
for j in range(w):
    for i in range(h):
        if s[i][j]=='#':
            u[i][j]=0
        elif i==0:
            u[i][j]=1
        else:
            u[i][j]=u[i-1][j]+1
d=[[-1]*w for _ in range(h)]
for j in range(w):
    for i in range(h-1,-1,-1):
        if s[i][j]=='#':
            d[i][j]=0
        elif i==h-1:
            d[i][j]=1
        else:
            d[i][j]=d[i+1][j]+1
ans=0
for i in range(h):
    for j in range(w):
        ans=max(ans,l[i][j]+r[i][j]+u[i][j]+d[i][j]-3)
print(ans)
"""
4 6
#..#..
.....#
....#.
#.#...
"""
