n=int(input())
l=list(map(int,input().split()))
a=sum(l)/n
if a%1==0:
    c=0
    for i in range(1,n):
        x=l[:i]
        y=l[i:]
        if sum(x)/len(x)!=sum(y)/len(y):
            c+=1
    print(c)
else:
    print(-1)
