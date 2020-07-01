n=int(input())
x=list(map(int,input().split()))
s=sorted(x)
b1=s[n//2-1]
b2=s[n//2]
for v in x:
    print(b2 if v<b2 else b1)
