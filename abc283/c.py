s = input()
n = int(len(s))
ans = 0
zf = False
for i in range(n - 1):
    if s[i] == "0":
        if zf:
            # 2個めの0
            zf = False
        else:
            if s[i + 1] == "0":
                zf = True
            ans += 1
    else:
        ans += 1
if s[n - 1] == "0":
    if not zf:
        ans += 1
else:
    ans += 1

print(ans)
