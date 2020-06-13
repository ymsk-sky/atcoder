n,k=map(int,input().split())
s=0
if k%2==0:
    s0=0
    for i in range(1,n+1):
        if i%k==0:
            s0+=1
    s1=0
    for i in range(1,n+1):
        if i%k==k//2:
            s1+=1
    s=s0**3+s1**3
else:
    s0=0
    for i in range(1,n+1):
        if i%k==0:
            s0+=1
    s=s0**3
print(s)
