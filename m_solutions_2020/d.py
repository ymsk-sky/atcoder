n=int(input())
al=list(map(int,input().split()))
s=1000
k=0
for i,j in zip(al,al[1:]):
    if i==j:
        continue
    if i<j:
        m=s//i
        k+=m
        s-=m*i
    else:
        s+=k*i
        k=0
s+=k*al[-1]
print(s)
