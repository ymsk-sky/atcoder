l = []
x = 1
x3 = x**3
while x3 <= 10**18:
    s = str(x3)
    if s == s[::-1]:
        l.append(x3)
    x += 1
    x3 = x**3

n = int(input())
for v in l[::-1]:
    if v <= n:
        print(v)
        break
