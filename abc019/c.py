n=int(input())
l=list(map(int,input().split()))
s=set()
for a in l:
    while 1:
        if a%2==0:
            a/=2
        else:
            break
    s.add(a)
print(len(s))
