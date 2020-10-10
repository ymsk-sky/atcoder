n=int(input())
l=list(map(int,input().split()))
m=0
for i,p in enumerate(l):
    if p==m:
        s=set(l[:i+1])
        while 1:
            m+=1
            if m in s:
                pass
            else:
                break
    print(m)
