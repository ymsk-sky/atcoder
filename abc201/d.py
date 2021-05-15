"""
+: 青マス(乗ると+1)
-: 赤マス(乗ると-1)
"""
from collections import deque
H,W=map(int,input().split())
A=[input() for _ in range(H)]
q=deque()
q.append([0,0])
while q:
    x,y=q.pop()
    x1,y1=x+1,y
    x2,y2=x,y+1
    if x1<=W:
        q.append([x1,y1])
    if y2<=H:
        q.append([x2,y2])
