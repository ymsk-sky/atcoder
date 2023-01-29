n = int(input())
f, a = 0, 0
for _ in range(n):
    s = input()
    if s == "For":
        f += 1
    else:
        a += 1
if 2*f >= n:
    print("Yes")
else:
    print("No")