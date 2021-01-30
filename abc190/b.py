n,s,d=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
for x,y in l:
    if x<s and y>d:
        print('Yes')
        exit()
print('No')
