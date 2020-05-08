n=int(input())
as_=list(map(int,input().split()))
bs=list(map(int,input().split()))
bf=sum(as_)
for i in range(n):
    if as_[i]-bs[i]<0:
        bs[i]-=as_[i]
        as_[i]=0
    else:
        as_[i]-=bs[i]
        bs[i]=0
    if as_[i+1]-bs[i]<0:
        as_[i+1]=0
    else:
        as_[i+1]-=bs[i]
print(bf-sum(as_))
