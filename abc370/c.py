s = list(input())
t = list(input())
n = len(s)
x = []
while 1:
    fin = True
    for i in range(n):
        if s[i] == t[i]:
            continue
        if s[i] > t[i]:
            s[i] = t[i]
            fin = False
            x.append("".join(s))
            break
    if fin:
        if s == t:
            break
        else:
            for i in range(n - 1, -1, -1):
                if s[i] != t[i]:
                    s[i] = t[i]
                    x.append("".join(s))
m = len(x)
print(m)
if m > 0:
    print(*x, sep="\n")
