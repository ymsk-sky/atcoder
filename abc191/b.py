n,x=map(int,input().split())
al=list(map(int,input().split()))
l=[str(a) for a in al if a!=x]
print(' '.join(l))
