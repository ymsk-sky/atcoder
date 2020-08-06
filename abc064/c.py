n=int(input())
l=list(map(int,input().split()))
d={}
f=0
for a in l:
    if a<400:
        if not 0 in d:
            d[0]=1
    elif a<800:
        if not 1 in d:
            d[1]=1
    elif a<1200:
        if not 2 in d:
            d[2]=1
    elif a<1600:
        if not 3 in d:
            d[3]=1
    elif a<2000:
        if not 4 in d:
            d[4]=1
    elif a<2400:
        if not 5 in d:
            d[5]=1
    elif a<2800:
        if not 6 in d:
            d[6]=1
    elif a<3200:
        if not 7 in d:
            d[7]=1
    else:
        f+=1
v=sum(d.values())
min_=1 if v==0 else v
max_=v+f
print(min_,max_)
