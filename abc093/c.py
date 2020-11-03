a,b,c=sorted(list(map(int,input().split())),reverse=True)  # 降順
if a==b:
    if (a-c)%2==0:
        print((a-c)//2)
    else:
        print((a-c)//2+2)
elif b==c:
    print(a-b)
else:
    x=a-b
    c+=x
    if (a-c)%2==0:
        print(x+(a-c)//2)
    else:
        print(x+(a-c)//2+2)
