k,n=map(int,input().split())
al=list(map(int,input().split()))
d=[a_-a for a,a_ in zip(al, al[1:])]+[k-al[-1]+al[0]]
print(sum(sorted(d)[:-1]))
