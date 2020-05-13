n,x=map(int,input().split())
ls=list(map(int,input().split()))
a=1
d=0
for l in ls:
    d+=l
    if d<=x:
        a+=1
    else:
        break
print(a)
