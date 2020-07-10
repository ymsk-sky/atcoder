from itertools import combinations
n=int(input())
d=dict({'M':0,'A':0,'R':0,'C':0,'H':0})
for _ in range(n):
    s=input()[0]
    if s in d:
        d[s]+=1
a=0
