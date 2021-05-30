import numpy as np
n,k=map(int,input().split())
l=np.array([list(map(int,input().split())) for _ in range(n)])
ans=float('inf')
for i in range(n-k+1):
    for j in range(n-k+1):
        tmp=l[i:i+k,j:j+k]
        # 要素数が偶数の場合中央の2つの値の平均となってしまう
        ans=min(ans,np.median(tmp))
print(int(ans))
