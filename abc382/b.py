n, d = map(int, input().split())
s = input()
ans = []
for c in s[::-1]:
    if c == ".":
        ans.append(".")
    else:
        if d > 0:
            ans.append(".")
            d -= 1
        else:
            ans.append("@")
print("".join(ans[::-1]))
