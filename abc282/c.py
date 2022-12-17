n = int(input())
s = input()
t = []
cnt = 0
for c in s:
    if c == "," and cnt%2 == 0:
        t.append(".")
    elif c == '"':
        cnt += 1
        t.append(c)
    else:
        t.append(c)

print(*t, sep="")
