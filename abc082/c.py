n=int(input())
l=list(map(int,input().split()))
s=set(l)
a=0
for v in s:
    c=l.count(v)
    if v<=c:
        a+=c-v
    else:
        a+=c
print(a)
