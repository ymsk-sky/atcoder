n=int(input())
l=list(map(int,input().split()))
mt=0
ma=0
for i in range(n-1):
    r=l[i:]
    for j in range(2,len(r)+1):
        z=r[:j]
        x=sum(z[0::2]) # takahashi
        y=sum(z[1::2]) # aoki
        print('(t,a)=({},{})'.format(x,y))
        if ma<y:
            ma=y
            mt=x
print(mt)

"""
6
1 -3 3 9 1 6
i=0
j=5
"""
