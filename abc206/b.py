n=int(input())
c=0
for i,p in enumerate(range(1,n+1),start=1):
    c+=p
    if c>=n:
        print(i)
        exit()
