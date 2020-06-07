n=int(input())
c=0
def a(i):
    if int(i)>n:
        return 0
    r=1 if all(i.count(c)>0for c in '753') else 0
    for c in '753':
        r+=a(i+c)
    return r
print(a('0'))
