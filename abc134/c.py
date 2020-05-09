n=int(input())
as_=[int(input()) for _ in range(n)]
l=sorted(as_)
m1=l[-1]
m2=l[-2]
for a in as_:
    if a==m1:
        print(m2)
    else:
        print(m1)
