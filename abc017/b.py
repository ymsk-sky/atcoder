x=input()
while 1:
    if x[-2:]=='ch':
        x=x[:len(x)-2]
    elif x[-1]=='o' or x[-1]=='k' or x[-1]=='u':
        x=x[:len(x)-1]
    else:
        print('NO')
        exit()
    if len(x)==0:
        break
print('YES')
