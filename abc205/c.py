a,b,c=map(int,input().split())
if c%2==0:  # 偶数回: -は+になる
    A=abs(a)
    B=abs(b)
    if A>B:
        print('>')
    elif A<B:
        print('<')
    else:
        print('=')
else:  # 奇数回: -は-のまま
    if a>=0 and b>=0:
        if a>b:
            print('>')
        elif a<b:
            print('<')
        else:
            print('=')
    elif a>=0 and b<0:
        print('>')
    elif a<0 and b>=0:
        print('<')
    elif a<0 and b<0:
        if a>b:
            print('>')
        elif a<b:
            print('<')
        else:
            print('=')
