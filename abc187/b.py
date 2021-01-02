n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
ans=0
for i in range(n):
    for j in range(i+1,n):
        a,b=l[i]
        c,d=l[j]
        if -1<= (d-b)/(c-a) <=1:
            ans+=1
print(ans)
