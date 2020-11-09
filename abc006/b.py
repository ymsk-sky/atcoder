n=int(input())
t1,t2,t3=0,0,1
if n==1 or n==2:
    print(0)
elif n==3:
    print(1)
else:
    m=10**4+7
    for _ in range(4,n+1):
        a=(t1+t2+t3)%m
        t1,t2,t3=t2,t3,a
    print(a%m)
