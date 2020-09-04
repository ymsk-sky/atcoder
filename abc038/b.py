a,b=map(int,input().split())
c,d=map(int,input().split())
print('YES'if len({a,b}&{c,d})>0else'NO')
