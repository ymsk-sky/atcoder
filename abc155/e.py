n = "0" + input()
l = len(n)
k = 0  # 繰り上がり
ans = 0
for i in range(l - 1, 0, -1):
    c = n[i]
    c = int(c) + k
    if c == 5:
        d = int(n[i - 1])
        if d + 1 > 5:
            k = 1
            ans += c
        else:
            k = 0
            ans += c
    elif c < 6:
        ans += c
        k = 0
    else:
        ans += 10 - c
        k = 1
print(ans + k)
