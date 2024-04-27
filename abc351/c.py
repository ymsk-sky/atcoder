n = int(input())
al = list(map(int, input().split()))

l = []
for a in al:
    l.append(a)
    while 1:
        if len(l) <= 1:
            break
        if l[-1] != l[-2]:
            break
        a1 = l.pop()
        a2 = l.pop()
        l.append(a1 + 1)
print(len(l))
