n=int(input())
tl=list(map(int,input().split()))
tl.sort(reverse=True)
a=0
b=0
for t in tl:
    if a>=b:
        b+=t
    else:
        a+=t
print(max(a,b))
