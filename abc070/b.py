a,b,c,d=map(int,input().split())
if max(a,c)>min(b,d):
    print(0)
else:
    print(min(b,d)-max(a,c))
