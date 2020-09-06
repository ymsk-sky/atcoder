n=int(input())
d={}
for i in range(n):
    a=int(input())
    if a in d:
        d[a].append(i)
    else:
        d[a]=[i]
s=[0]*n
for i,k in enumerate(sorted(d.keys())):
    for a in d[k]:
        s[a]=i
for v in s:
    print(v)
