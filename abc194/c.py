n=int(input())
al=list(map(int,input().split()))
sum_=sum(al)
ans=0
for a in al:
    ans+=(n-1)*a**2
    sum_-=a
    ans-=2*a*sum_
print(ans)
