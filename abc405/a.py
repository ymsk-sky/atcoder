r, x = map(int, input().split())
if x == 1:
    ans = "Yes" if 1600 <= r <= 2999 else "No"
else:
    ans = "Yes" if 1200 <= r <= 2399 else "No"
print(ans)
