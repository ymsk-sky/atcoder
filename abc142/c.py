n=int(input())
as_=list(map(int,input().split()))
l=as_.copy()
for i,a in enumerate(as_):
    l[a-1]=i+1
for v in l:
    print(v, end=' ')
print('')
