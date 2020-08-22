n=int(input())
l=list(map(int,input().split()))
s=0
b=l[0]
for a in l[1:]:
    if b>a:
        s+=b-a
    else:
        b=a
print(s)
