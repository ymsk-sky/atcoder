n=int(input())
l=list(map(int,input().split()))
if 0 in l:
    print(0)
    exit()
s=1
for a in l:
    s*=a
    if s>10**18:
        print(-1)
        exit()
print(s)
