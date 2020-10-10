n=int(input())
l=list(map(int,input().split()))
s=list(range(2*10**5+1))
for p in l:
    try:
        s.remove(p)
    except:
        pass
    print(s[0])
