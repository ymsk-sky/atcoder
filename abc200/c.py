n=int(input())
al=list(map(int,input().split()))
l=[0]*200
for a in al:
    k=a%200
    l[k]+=1
ans=0
for x in l:
    ans+=x*(x-1)//2
print(ans)
