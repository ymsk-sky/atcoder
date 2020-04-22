# ans: 二分探索, 10億以下
a,b,x=map(int,input().split()) # 10 7 100
ans=1_000_000_000
k=len(str(ans)) #10
i=0
while i<10:
    sum_=a*ans+b*k
    if sum_==x:
        break
    elif sum_>x:
        ans//=2
        k=len(str(ans))
    else:
        ans+=ans//2
        k=len(str(ans))
    if sum_<=0:
        print(0)
        exit()
    i+=1
print(ans)
