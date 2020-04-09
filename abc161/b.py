N,M=map(int,input().split())
As=list(map(int,input().split()))
print('Yes' if len([a for a in As if a>=sum(As)/(4*M)])>=M else 'No')
