n,t=map(int,input().split())
a=float('inf')
for _ in range(n):
    c,u=map(int,input().split())
    if u<=t:
        a=min(a,c)
print('TLE' if a==float('inf') else a)
