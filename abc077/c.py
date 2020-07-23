from bisect import bisect_left,bisect_right
n=int(input())
al=list(map(int,input().split()))
bl=list(map(int,input().split()))
cl=list(map(int,input().split()))
al.sort()
cl.sort()
s=0
for b in bl:
    a=bisect_left(al,b)
    c=n-bisect_right(cl,b)
    s+=a*c
print(s)
