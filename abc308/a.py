sl = list(map(int, input().split()))

for a, b in zip(sl, sl[1:]):
    if a > b:
        print("No")
        exit()

if max(sl) > 675 or min(sl) < 100:
    print("No")
    exit()

for s in sl:
    if s%25 != 0:
        print("No")
        exit()

print("Yes")
