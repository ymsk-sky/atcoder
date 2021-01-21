from collections import deque
k=int(input())
q=deque([9-i for i in range(9)])
for _ in range(k-1):
    x=q.pop()
    if x%10!=0:
        q.appendleft(10*x+(x%10)-1)
    q.appendleft(10*x+(x%10))
    if x%10!=9:
        q.appendleft(10*x+(x%10)+1)
print(q.pop())
