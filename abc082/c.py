n=int(input())
l=list(map(int,input().split()))
d=dict()
for v in l:
    if v in d:
        d[v]+=1
    else:
        d[v]=1
c=0
for k, v in d.items():
    if k<=v:
        c+=v-k
    else:
        c+=v
print(c)
