import numpy as np
n,k=map(int,input().split())
l=np.array([list(map(int,input().split())) for _ in range(n)])
k2=k**2
ans=float('inf')
for i in range(n-k+1):
    for j in range(n-k+1):
        tmp=np.ravel(l[i:i+k,j:j+k])
        if k2%2==0:  # 要素数が偶数の場合中央の2つの値の平均となってしまうため0を追加
            tmp=np.append(0,tmp)
        ans=min(ans,np.median(tmp))
print(int(ans))
