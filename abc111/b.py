n=int(input())
while 1:
    if len(set(str(n)))==1:
        print(n)
        exit()
    n+=1
