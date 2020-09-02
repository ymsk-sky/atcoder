n=int(input())
l=list(map(int,input().split()))
l=[l[0]]+l
dp=[0,0]
for i in range(2,n+1):
    a=dp[i-2]+abs(l[i-2]-l[i])
    b=dp[i-1]+abs(l[i-1]-l[i])
    dp.append(min(a,b))
print(dp[-1])
