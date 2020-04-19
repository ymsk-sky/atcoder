n=int(input())
s,t=input().split()
for u,v in zip(s,t):
    print('{}{}'.format(u,v),end='')
