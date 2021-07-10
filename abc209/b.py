n,x=map(int,input().split())
al=list(map(int,input().split()))
s=0
for i,a in enumerate(al):
    if i%2==0:
        s+=a
    else:
        s+=a-1
print('Yes' if s<=x else 'No')
