n, q = map(int, input().split())
s = input()
queries = [input().split() for _ in range(q)]
cnt = s.count("ABC")
s = list(s)
for x, c in queries:
    x = int(x) - 1
    for st in range(x - 2, x + 1):
        if st < 0 or st + 2 >= n:
            continue
        t = s[st] + s[st + 1] + s[st + 2]
        if t == "ABC":
            cnt -= 1
    s[x] = c
    for st in range(x - 2, x + 1):
        if st < 0 or st + 2 >= n:
            continue
        t = s[st] + s[st + 1] + s[st + 2]
        if t == "ABC":
            cnt += 1
    print(cnt)
