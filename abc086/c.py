n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
ct,cx,cy=0,0,0
for t,x,y in l:
    dt=t-ct
    d=abs(cx-x)+abs(cy-y)
    if dt-d<0 or (dt-d)%2==1:
        print('No')
        exit()
    ct,cx,cy=t,x,y
print('Yes')
