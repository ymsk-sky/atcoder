n=int(input())
ds=list(map(int,input().split()))
sum_=0
for i,d in enumerate(ds[:-1]):
    sum_+=sum([d*e for e in ds[i+1:]])
print(sum_)
