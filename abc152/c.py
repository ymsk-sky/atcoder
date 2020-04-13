n=int(input())
ps=list(map(int,input().split()))
cnt=0
min_=ps[0]
for p in ps:
    if min_>=p:
        cnt+=1
        min_=p
print(cnt)
