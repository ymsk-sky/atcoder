n,m=map(int,input().split())
def a(n):
    if n<2: return n
    return n+a(n-1)
sum_=0
if n>1:
    sum_+=a(n-1)
if m>1:
    sum_+=a(m-1)
print(sum_)
