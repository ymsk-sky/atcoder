n,m=map(int,input().split())
al=list(map(int,input().split()))
bl=list(map(int,input().split()))
s=set(al)^set(bl)
if len(s)==0:
    print('')
else:
    print(' '.join([str(v) for v in sorted(s)]))
