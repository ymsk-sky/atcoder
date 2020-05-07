n=int(input())
hs=list(map(int,input().split()))[::-1]
for i in range(n-1):
    d=hs[i]-hs[i+1]
    if d==-1:
        hs[i+1]-=1
    elif d<-1:
        print('No')
        exit()
print('Yes')
