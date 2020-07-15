n,y=map(int,input().split())
for i in range(0,n+1):
    if i*10000>y:
        break
    for j in range(0,n+1-i):
        if i*10000+j*5000>y:
            break
        k=n-i-j
        if i*10000+j*5000+k*1000==y:
            print(i,j,k)
            exit()
print(-1,-1,-1)

"""
1000円札, 5000円札, 10000円札
N枚
Y円
"""
