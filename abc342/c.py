n = int(input())
s = input()
to = {c: c for c in "abcdefghijklmnopqrstuvwxyz"}
q = int(input())
for _ in range(q):
    c, d = input().split()
    for k in to:
        if to[k] == c:
            to[k] = d
t = "".join([to[c] for c in s])
print(t)
