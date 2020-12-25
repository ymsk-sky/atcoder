h,w=map(int,input().split())
s=[input() for _ in range(h)]
l=[[[-1,-1,-1,-1] for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j,k in zip(range(w),range(w-1,-1,-1)):
        if s[i][j]=='#':
            l[i][j][0]=0
        elif j==0:
            l[i][j][0]=1
        else:
            l[i][j][0]=l[i][j-1][0]+1

        if s[i][k]=='#':
            l[i][k][1]=0
        elif k==w-1:
            l[i][k][1]=1
        else:
            l[i][k][1]=l[i][k+1][1]+1
for j in range(w):
    for i,k in zip(range(h),range(h-1,-1,-1)):
        if s[i][j]=='#':
            l[i][j][2]=0
        elif i==0:
            l[i][j][2]=1
        else:
            l[i][j][2]=l[i-1][j][2]+1

        if s[k][j]=='#':
            l[k][j][3]=0
        elif k==h-1:
            l[k][j][3]=1
        else:
            l[k][j][3]=l[k+1][j][3]+1
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
