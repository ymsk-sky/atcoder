s=input()
k=int(input())
d=[]
for p in range(len(s)):
    t=s[p:]
    d.append(t)
    for i in range(1,len(t)):
        d.append(t[:-i])
d=sorted(set(d))
print(d[k-1])
