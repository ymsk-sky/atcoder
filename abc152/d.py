n=int(input())
dp=[[0]*10 for _ in range(10)]
ans=0
for i in range(1,n+1):
    top=int(str(i)[0])
    end=int(str(i)[-1])
    ans+=2*dp[end][top]
    if top==end:
        ans+=1
    dp[top][end]+=1
print(ans)
