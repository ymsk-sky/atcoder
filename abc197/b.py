h,w,x,y=map(int,input().split())
sl=[input() for _ in range(h)]
x-=1
y-=1
cnt=1 if sl[x][y]=='.' else 0
for i in range(y+1,w):
    if sl[x][i]=='#':
        break
    cnt+=1
if y>0:
    for i in range(y-1,-1,-1):
        if sl[x][i]=='#':
            break
        cnt+=1
for i in range(x+1,h):
    if sl[i][y]=='#':
        break
    cnt+=1
if x>0:
    for i in range(x-1,-1,-1):
        if sl[i][y]=='#':
            break
        cnt+=1
print(cnt)
