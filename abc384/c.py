pl = list(map(int, input().split()))
l = []
for state in range(1, 1 << 5):
    name = "".join([c for i, c in enumerate("ABCDE") if (state >> i) & 1])
    point = sum([pl[i] if (state >> i) & 1 else 0 for i in range(5)])
    l.append((-point, name))

l.sort()
for _, name in l:
    print(name)
