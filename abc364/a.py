n = int(input())
sl = [input() for _ in range(n)]
sl = sl[:-1]
for s1, s2 in zip(sl, sl[1:]):
    if s1 == s2 == "sweet":
        print("No")
        exit()
print("Yes")
