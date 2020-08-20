k,s=map(int,input().split())
c=0
for x in range(k+1):
    for y in range(k+1):
        if x+y<=s and s-x-y<=k:
            c+=1
print(c)
