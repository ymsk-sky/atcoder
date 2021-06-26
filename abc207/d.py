import numpy as np
n=int(input())
s=[list(map(int,input().split())) for _ in range(n)]
t=[list(map(int,input().split())) for _ in range(n)]
# (x,y)を(r,θ)へ変換
s=[(np.sqrt(x**2+y**2),np.rad2deg(np.arctan2(y,x))) for x,y in s]
s.sort()
t=[(np.sqrt(x**2+y**2),np.rad2deg(np.arctan2(y,x))) for x,y in t]
# 1点ごとに合うか確認
for rs,θs in s:
    for rt,θt in t:
        dr=rt-rs
        dθ=θt-θs
        u=[(r-dr,θ-dθ) for r,θ in t]
        u.sort()
        if s==u:
            print('Yes')
            exit()
print('No')
