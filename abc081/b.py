n=int(input())
l=list(map(int,input().split()))
s=float('inf')
for a in l:
    c=0
    while a%2==0:
        c+=1
        a/=2
    s=min(s,c)
print(s)
