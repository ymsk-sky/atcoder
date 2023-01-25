n = int(input())
s = input()
t = [s[0]]
for i in range(1, n):
    if s[i] == "a" and s[i - 1] == "n":
        t.append("ya")
    else:
        t.append(s[i])

print(*t, sep="")