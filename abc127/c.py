n,m=map(int,input().split())
gates=[0]*(n+2)
for _ in range(m):
    l,r=map(int,input().split())
    gates[l]+=1
    gates[r+1]-=1
for i in range(1,n+1):
    gates[i]+=gates[i-1]
print(gates[1:-1].count(m))
