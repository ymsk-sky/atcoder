a,b,c=map(int,input().split())
x,y,z=sorted([a,b,c])

if(y-x)%2==0:
    e1=(z-y) + (y-x)
else:
    e1=(z-y) + (y-x+1)

(z-x)
