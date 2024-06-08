s = input()
upper = 0
lower = 0
for c in s:
    if c.islower():
        lower += 1
    else:
        upper += 1
if lower > upper:
    ans = s.lower()
else:
    ans = s.upper()
print(ans)
