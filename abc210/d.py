h,w,c=map(int,input().split())
awl=[list(map(int,input().split())) for _ in range(h)]  # (i,j)に駅を建てたときの費用
ans=float('inf')
for i1 in range(h-1):  # 10**3
    for i2 in range(i1,h):
        for j1 in range(w-1):  # 10**3
            for j2 in range(j1,w):
                if i1==i2 and j1==j2:
                    continue
                a=awl[i1][j1]
                b=awl[i2][j2]
                d=c*(i2-i1+j2-j1)
                ans=min(ans,a+b+d)
print(ans)
