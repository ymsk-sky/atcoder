a,b,w=map(int,input().split())
w*=1000
max_=0
min_=float('inf')
for n in range(1,10**6+1):
    if a*n<=w<=b*n:
        min_=min(min_,n)
        max_=max(max_,n)
print('{} {}'.format(min_,max_) if max_!=0 else 'UNSATISFIABLE')
