n=int(input())
l=list(map(int,input().split()))
s=0
i=0
for a in l:
    if a!=0:
        s+=a
    else:
        i+=1
n-=i
if s%n==0:
    print(s//n)
else:
    print(s//n+1)
