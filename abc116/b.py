s=int(input())
l=[s]
i=1
while 1:
    i+=1
    s=s/2 if s%2==0 else 3*s+1
    if s in l:
        print(i)
        exit()
    else:
        l.append(s)
