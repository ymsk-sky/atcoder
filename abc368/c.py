n = int(input())
hl = list(map(int, input().split()))
t = 0
for h in hl:
    if t % 3 == 1:
        t += 1
        h -= 1
        if h == 0:
            continue
    elif t % 3 == 0:
        t += 1
        h -= 1
        if h == 0:
            continue
        t += 1
        h -= 1
        if h == 0:
            continue
    t += (h // 5) * 3
    h %= 5
    while h > 0:
        if t % 3 == 2:
            h -= 3
        else:
            h -= 1
        t += 1
print(t)
