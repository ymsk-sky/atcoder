n=int(input())
l=list(map(int,input().split()))
c=0
for e,v in enumerate(l,start=1):
    if e%2==1 and v%2==1:
        c+=1
print(c)
