import numpy as np
n=int(input())
tl=list(map(int,input().split()))
s=np.sum(tl)
dp=np.zeros(s//2+1,dtype=np.bool)
dp[-1]=1
for i in range(n):
    if s//2+1-tl[i]<0:
        continue
    dp[:s//2+1-tl[i]]|=dp[tl[i]:]
print(s-s//2+np.argmax(dp))
