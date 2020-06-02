n=int(input())
a=0
for _ in range(n):
    x,u=map(str,input().split())
    x=float(x)
    if u=='JPY':
        a+=x
    else:
        a+=x*380000.0
print(a)
