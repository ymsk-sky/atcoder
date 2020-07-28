n=int(input())
d={}
for _ in range(n):
    a=int(input())
    if a in d:
        d[a]+=1
    else:
        d[a]=1
c=0
for a in d.values():
    if a%2==1:
        c+=1
print(c)
