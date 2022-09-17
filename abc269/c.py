x = int(input())
n = 0
l = []
t = 0
for c in bin(x)[2:]:
    if c == "0":
        t += 1
    else:
        n += 1
        l.append("0" * t)
        t = 0
l.append("0" * t)

for i in range(2 ** n):
    print(int("".join([a + b for a, b in zip(l, list(bin(i)[2:].zfill(n)) + [""])]), 2))
