x,y=map(str,input().split('.'))
y=int(y)
if y<3:
    print(x+'-')
elif y<7:
    print(x)
else:
    print(x+'+')
