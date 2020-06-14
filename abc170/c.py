x,n=map(int,input().split())
ps=list(map(int,input().split()))
i=0
while 1:
    m=x-i
    if not m in ps:
        print(m)
        exit()
    p=x+i
    if not p in ps:
        print(p)
        exit()
    i+=1
