n=int(input())
x=1
turn=1
while 1:
    if x>n:
        break
    x+=1
    turn*=-1
print('Takahashi'if turn==1 else'Aoki')
