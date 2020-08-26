n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
x,y=1,1
for t,a in l:
    mt=x//t if x/t==x//t else x//t+1
    ma=y//a if y/a==y//a else y//a+1
    m=max(mt,ma)
    x,y=m*t,m*a
print(x+y)
