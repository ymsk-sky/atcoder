n=int(input())
a,b=map(int,input().split())
k=int(input())
l=list(map(int,input().split()))
if (a in l) or (b in l) or (len(l)!=len(set(l))):
    print('NO')
else:
    print('YES')
