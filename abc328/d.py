from collections import deque

s = input()
bef = deque()
aft = deque(s)
tmp = ""
while aft:
    a = aft.popleft()
    bef.append(a)
    if len(bef) > 2:
        c = bef.pop()
        b = bef.pop()
        a = bef.pop()
        if not (a == "A" and b == "B" and c == "C"):
            bef.append(a)
            bef.append(b)
            bef.append(c)
print(*bef, sep="")
