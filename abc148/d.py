n=int(input())
l=list(map(int,input().split()))
cnt=0
current=1
for a in l:
    if a==current:
        current+=1
    else:
        cnt+=1
print(-1 if cnt==n else cnt)
