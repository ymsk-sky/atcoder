n,p=map(int,input().split())
al=list(map(int,input().split()))
print(sum([1 for a in al if a<p]))
