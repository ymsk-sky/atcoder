s = set()
for a in range(33):
    x = int("1" * (a + 1))
    for b in range(33):
        y = int("1" * (b + 1))
        for c in range(33):
            z = int("1" * (c + 1))
            s.add(x + y + z)
l = sorted(s)
n = int(input())
print(l[n - 1])
