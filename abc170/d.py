n=int(input())
an=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        if an[i]%an[j]==0:
            j=-1
            break
    if j==n-1:
        c+=1
print(c)
