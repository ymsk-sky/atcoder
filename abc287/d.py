s = input()
t = input()
n = len(s)
m = len(t)

pre = [0] * (n + 1)
pre[0] = 1
for i in range(m):
    if s[i] == "?" or t[i] == "?" or s[i] == t[i]:
        pre[i + 1] = 1
    else:
        break

s = s[::-1]
t = t[::-1]

suf = [0] * (n + 1)
suf[0] = 1
for i in range(m):
    if s[i] == "?" or t[i] == "?" or s[i] == t[i]:
        suf[i + 1] = 1
    else:
        break

for i in range(m + 1):
    if pre[i] == 1 and suf[m - i] == 1:
        print("Yes")
    else:
        print("No")
