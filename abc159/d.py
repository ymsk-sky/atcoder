def a(n):
    if n<2: return n
    return n+a(n-1)
N=int(input())
As=list(map(int,input().split()))
for i in range(len(As)):
    sum_=0
    l=As[:i]+As[i+1:]
    m=list(set(l))
    for f in m:
        c=l.count(f)
        sum_+=a(c-1)
    print(sum_)
