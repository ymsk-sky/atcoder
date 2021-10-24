n=int(input())
xyl=[list(map(int,input().split())) for _ in range(n)]
ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x1,y1=xyl[i]
            x2,y2=xyl[j]
            x3,y3=xyl[k]
            dx1=x2-x1
            dx2=x3-x1
            dy1=y2-y1
            dy2=y3-y1
            if dx2*dy1==dx1*dy2:
                pass
            else:
                ans+=1
print(ans)
