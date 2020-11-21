"""
ΣA,a=1ΣB,b=1ΣC,c=1 a*b*c
を998244353で割った値

1 2 3
18
"""
a,b,c=map(int,input().split())
m=998244353
print((a*(a+1)//2*b*(b+1)//2*c*(c+1)//2)%m)
