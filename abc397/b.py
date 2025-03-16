s = input()
ans = 0
crt = 0
for c in s:
    if crt == 0:
        if c != "i":
            ans += 1
            crt = 1 - crt
    else:
        if c != "o":
            ans += 1
            crt = 1 - crt
    crt = 1 - crt

if s[-1] == "i":
    ans += 1

print(ans)
