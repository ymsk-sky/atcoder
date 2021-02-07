h,w=map(int,input().split())
ss=[input() for _ in range(h)]
ans=0
for y in range(h-1):
    for x in range(w-1):
        a=ss[y][x]
        b=ss[y][x+1]
        c=ss[y+1][x]
        d=ss[y+1][x+1]
        cnt=[a,b,c,d].count('#')
        if cnt==1 or cnt==3:
            ans+=1
print(ans)
