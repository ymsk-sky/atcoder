from itertools import product
n=int(input())
l=list(map(int,input().split()))
for p in product((0,1),repeat=n-1):
    print(p)
