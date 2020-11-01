from itertools import combinations
n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
for (x1,y1),(x2,y2),(x3,y3) in combinations(l, 3):
    dx2=x3-x1
    dy1=y2-y1
    dx1=x2-x1
    dy2=y3-y1
    if dx2*dy1==dx1*dy2:
        print('Yes')
        exit()
print('No')
