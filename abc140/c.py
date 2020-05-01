n=int(input())
bs=list(map(int,input().split()))
a=[10**5]*n
for i,b in enumerate(bs):
    a[i+1]=b
    if a[i]>b:
        a[i]=b
print(sum(a))
