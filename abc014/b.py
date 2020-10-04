n,x=map(int,input().split())
l=list(map(int,input().split()))
s=0
for i,v in enumerate(bin(x)[2:].zfill(n)[::-1]):
    if int(v)==1:
        s+=l[i]
print(s)

"""
4 5
1 10 100 1000

20 1048575
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
"""
