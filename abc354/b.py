n = int(input())
t = 0
l = []
for i in range(n):
    s, c = input().split()
    c = int(c)
    t += c
    l.append((s, i))
l.sort()
print(l[t % n][0])
