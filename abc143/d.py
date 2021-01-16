from bisect import bisect_left
n=int(input())
l=sorted(list(map(int,input().split())))
cnt=0
for i in range(n):
    for j in range(i+1,n):
        a=l[i]
        b=l[j]
        k=bisect_left(l,a+b)
        tmp=k-(j+1)
        cnt+=tmp
print(cnt)
