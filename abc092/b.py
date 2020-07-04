n=int(input())
d,x=map(int,input().split())
l=[int(input()) for _ in range(n)]
for i in l:
    j=0
    while 1:
        if j*i+1<=d:
            x+=1
        else:
            break
        j+=1
print(x)
