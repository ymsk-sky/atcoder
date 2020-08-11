n=int(input())
l=list(map(int,input().split()))
cs1=0
s1=0
for i,a in enumerate(l):
    cs1+=a
    if i%2==0:
        if cs1>=0:
            s1+=abs(cs1)+1
            cs1=-1
    else:
        if cs1<=0:
            s1+=abs(cs1)+1
            cs1=1
cs2=0
s2=0
for i,a in enumerate(l):
    cs2+=a
    if i%2==0:
        if cs2<=0:
            s2+=abs(cs2)+1
            cs2=1
    else:
        if cs2>=0:
            s2+=abs(cs2)+1
            cs2=-1
print(min(s1,s2))
