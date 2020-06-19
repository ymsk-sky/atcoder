a,b,c=map(int,input().split())
a,b,c=abs(a-b),abs(b-c),abs(c-a)
print(a+b+c-max(a,b,c))
