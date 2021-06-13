n=int(input())
al=list(map(int,input().split()))
al.sort()
for i,a in enumerate(al,start=1):
    if i!=a:
        print('No')
        exit()
print('Yes')
