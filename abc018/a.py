a=int(input())
b=int(input())
c=int(input())
x=max(a,b,c)
i=min(a,b,c)
if x==a:
    if i==b:
        print(1)
        print(3)
        print(2)
    else:
        print(1)
        print(2)
        print(3)
elif x==b:
    if i==a:
        print(3)
        print(1)
        print(2)
    else:
        print(2)
        print(1)
        print(3)
else:
    if i==a:
        print(3)
        print(2)
        print(1)
    else:
        print(2)
        print(3)
        print(1)
