sx,sy,tx,ty=map(int,input().split())
x=tx-sx
y=ty-sy
print('U'*y+'R'*x+'D'*y+'L'*x+'L'+'U'*(y+1)+'R'*(x+1)+'DR'+'D'*(y+1)+'L'*(x+1)+'U')
