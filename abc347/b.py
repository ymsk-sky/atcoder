s = input()
n = len(s)
l = set()
for i in range(n):
    for j in range(i + 1, n + 1):
        l.add(s[i:j])
print(len(l))
