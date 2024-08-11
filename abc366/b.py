n = int(input())
m = 0
sl = []
for _ in range(n):
    s = input()
    m = max(m, len(s))
    sl.append(s)
ans = []
for j in range(m):
    w = []
    for s in sl:
        if len(s) > j:
            w.append(s[j])
        else:
            w.append("*")
    ans.append("".join(w[::-1]).rstrip("*"))
for an in ans:
    print(an)
