n=int(input())
vs=list(map(int,input().split()))
cs=list(map(int,input().split()))
a=0
for v,c in zip(vs,cs):
    m=v-c
    if m>0:
        a+=m
print(a)
