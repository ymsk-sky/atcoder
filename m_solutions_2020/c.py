n,k=map(int,input().split())
al=list(map(int,input().split()))
for b,c in zip(al,al[k:]):
    print('Yes'if b<c else'No')
