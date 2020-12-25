h,w=map(int,input().split())
s=[input() for _ in range(h)]
l=[[[-1,-1,-1,-1] for _ in range(w)] for _ in range(h)]
for i1,i2 in zip(range(h),range(h-1,-1,-1)):
    for j1,j2 in zip(range(w),range(w-1,-1,-1)):
        if s[i1][j1]=='#':
            l[i1][j1][0]=0
        elif j1==0:
            l[i1][j1][0]=1
        else:
            l[i1][j1][0]=l[i1][j1-1][0]+1
        if s[i1][j2]=='#':
            l[i1][j2][1]=0
        elif j2==w-1:
            l[i1][j2][1]=1
        else:
            l[i1][j2][1]=l[i1][j2+1][1]+1
        if s[i1][j1]=='#':
            l[i1][j1][2]=0
        elif i1==0:
            l[i1][j1][2]=1
        else:
            l[i1][j1][2]=l[i1-1][j1][2]+1
        if s[i2][j1]=='#':
            l[i2][j1][3]=0
        elif i2==h-1:
            l[i2][j1][3]=1
        else:
            l[i2][j1][3]=l[i2+1][j1][3]+1
ans=0
for i in range(h):
    for j in range(w):
        ans=max(ans,sum(l[i][j])-3)
print(ans)
"""
4 6
#..#..
.....#
....#.
#.#...
"""
