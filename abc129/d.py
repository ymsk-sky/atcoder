h,w=map(int,input().split())
s=[input() for _ in range(h)]
def fu(y,x,n):
    if y<0 or y>=h or s[y][x]=='#':
        return n
    return fu(y+1,x,n+1)
def fd(y,x,n):
    if y<0 or y>=h or s[y][x]=='#':
        return n
    return fd(y-1,x,n+1)
def fr(y,x,n):
    if x<0 or x>=w or s[y][x]=='#':
        return n
    return fr(y,x+1,n+1)
def fl(y,x,n):
    if x<0 or x>=w or s[y][x]=='#':
        return n
    return fl(y,x-1,n+1)
ans=0
for y in range(h):
    for x in range(w):
        cnt=fu(y,x,0)+fd(y,x,0)+fr(y,x,0)+fl(y,x,0)
        if cnt==0:
            continue
        else:
            ans=max(ans,cnt-3)
print(ans)
