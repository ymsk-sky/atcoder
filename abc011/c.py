n=int(input())
l=[int(input())for _ in range(3)]
if n in l:
    print('NO')
    exit()
for _ in range(100):
    if n<4:
        print('YES')
        exit()
    if n-3 in l:
        if n-2 in l:
            if n-1 in l:
                print('NO')
                exit()
            else:
                n-=1
        else:
            n-=2
    else:
        n-=3
print('NO')
