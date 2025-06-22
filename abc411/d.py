n, q = map(int, input().split())

l = [(-1, "")]

sv = 0
pc = [0] * n

for _ in range(q):
    query = input().split()
    if query[0] == "1":
        p = int(query[1])
        pc[p - 1] = sv
    elif query[0] == "2":
        tmp, s = query[1:]
        p = int(tmp)
        bef = pc[p - 1]
        pc[p - 1] = len(l)
        l.append((bef, s))
    else:
        p = int(query[1])
        sv = pc[p - 1]

ans = []
while 1:
    bef, s = l[sv]
    ans.append(s)
    if bef == -1:
        break
    sv = bef
print("".join(ans[::-1]))
