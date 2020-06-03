n,m=map(int,input().split())
a=set(list(range(1,m+1)))
for _ in range(n):
    l=set(list(map(int,input().split()))[1:])
    a=a&l
print(len(a))
