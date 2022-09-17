sl = [input() for _ in range(10)]
a, b, c, d = 0, 0, 0, 0
for i in range(10):
    s = sl[i]
    if "#" in s:
        a = i + 1
        break
for i in range(9, -1, -1):
    s = sl[i]
    if "#" in s:
        b = i + 1
        c = s.find("#") + 1
        d = s.rfind("#") + 1
        break
print(a, b)
print(c, d)
