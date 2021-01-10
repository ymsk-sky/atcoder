n=int(input())
al=list(map(int,input().split()))
bl=list(map(int,input().split()))
ans=0
for a,b in zip(al,bl):
    ans+=a*b
print('Yes' if ans==0 else 'No')
