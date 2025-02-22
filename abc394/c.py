s = list(input())
n = len(s)
for i in range(n - 1, 0, -1):
    if s[i - 1] == "W" and s[i] == "A":
        s[i - 1] = "A"
        s[i] = "C"
print(*s, sep="")
