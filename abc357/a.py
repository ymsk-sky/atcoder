n, m = map(int, input().split())
hl = list(map(int, input().split()))
for i, h in enumerate(hl, start=1):
    if m - h < 0:
        print(i - 1)
        exit()
    m -= h
print(i)
