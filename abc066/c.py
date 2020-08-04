n=int(input())
l=list(map(int,input().split()))
if n%2==0:
    print(' '.join([str(v) for v in l[1::2][::-1]+l[::2]]))
else:
    print(' '.join([str(v) for v in l[::2][::-1]+l[1::2]]))
