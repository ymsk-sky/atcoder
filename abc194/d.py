n=int(input())
ans=0
for i in range(1,n+1):
    ans+=1/i
ans*=n
print(ans-1)
