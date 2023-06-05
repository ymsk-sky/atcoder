n = int(input())
l = []
for i in range(n):
    s, a = input().split()
    l.append((i, s, int(a)))
j = min(l, key=lambda e: e[2])[0]
for k in range(n):
    i = j + k
    print(l[i%n][1])
