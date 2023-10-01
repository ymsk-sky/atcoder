n = int(input())
s = input() + "_ABC"
i = s.index("ABC")
print(-1 if i > n else i + 1)
