n=int(input())
pl=list(map(int,input().split()))
ql=[0]*n
for i,p in enumerate(pl,start=1):
    ql[p-1]=str(i)
print(' '.join(ql))
