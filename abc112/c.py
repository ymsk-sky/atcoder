n=int(input())
f=[list(map(int,input().split())) for _ in range(n)]
def k(H,cx,cy,f):
    for x,y,h in f:
        if h==max(H-abs(x-cx)-abs(y-cy),0):
            continue
        else:
            return
    print(cx,cy,H)
    exit()
for x,y,h in f:
    if h==0:
        continue
    for cx in range(101):
        for cy in range(101):
            H=h+abs(x-cx)+abs(y-cy)
            k(H,cx,cy,f)
