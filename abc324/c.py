n, t = input().split()
n = int(n)
ans = []
def a(s):
    return s == t
def b(s):
    if len(s) != len(t) + 1:
        return False
    i = j = 0
    cnt = 0
    while i < len(t):
        x = t[i]
        y = s[j]
        if x == y:
            i += 1
            j += 1
            continue
        cnt += 1
        if cnt > 1:
            return False
        j += 1
    return True
def c(s):
    if len(s) + 1 != len(t):
        return False
    i = j = 0
    cnt = 0
    while j < len(s):
        x = t[i]
        y = s[j]
        if x == y:
            i += 1
            j += 1
            continue
        cnt += 1
        if cnt > 1:
            return False
        i += 1
    return True
def d(s):
    if len(s) != len(t):
        return False
    cnt = 0
    for x, y in zip(s, t):
        if x == y:
            continue
        cnt += 1
        if cnt > 1:
            return False
    return True
for i in range(n):
    s = input()
    if a(s) or b(s) or c(s) or d(s):
        ans.append(i + 1)
print(len(ans))
print(*ans)
