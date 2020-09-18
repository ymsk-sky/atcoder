n,a,b=map(int,input().split())
p=0
for _ in range(n):
    s,d=map(str,input().split())
    d=int(d)
    k=1 if s=='East' else -1
    d=a if d<a else b if d>b else d
    p+=k*d
print('East {}'.format(p) if p>0 else 'West {}'.format(abs(p)) if p<0 else p)
