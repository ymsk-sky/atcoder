n=int(input())
l=[int(input()) for _ in range(n)]
c=0
i=1
while 1:
    if i==2:
        print(c)
        break
    if c>=n:
        print(-1)
        break
    c+=1
    i=l[i-1]
