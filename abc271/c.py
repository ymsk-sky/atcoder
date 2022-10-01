from collections import deque

n = int(input())
l = list(map(int, input().split()))
l.sort()

al = []
bef = 0
for a in l:
    if bef == a:
        al.append(10 ** 9)
    else:
        al.append(a)
    bef = a
al.sort()

al = deque(al)

ans = 0
crt = 1
while al:
    a = al.popleft()
    if a == crt:
        ans = crt
        crt += 1
    else:
        al.appendleft(a)
        if len(al) >= 2:
            al.pop()
            al.pop()
            ans = crt
            crt += 1
        else:
            break

print(ans)
