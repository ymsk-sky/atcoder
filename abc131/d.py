n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
l.sort(key=lambda x:x[1])
sum_=0
for a,b in l:
    sum_+=a
    if sum_>b:
        print('No')
        exit()
print('Yes')
