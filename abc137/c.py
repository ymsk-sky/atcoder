n=int(input())
d=dict()
a=0
for _ in range(n):
    s=''.join(sorted(input()))
    if s in d:
        a+=d[s]
        d[s]+=1
    else:
        d[s]=1
print(a)
