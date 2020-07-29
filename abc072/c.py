n=int(input())
l=list(map(int,input().split()))
d={}
for a in l:
    for i in [-1,0,1]:
        if a+i in d:
            d[a+i]+=1
        else:
            d[a+i]=1
print(max(d.values()))
