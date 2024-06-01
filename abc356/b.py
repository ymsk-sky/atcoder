n, m = map(int, input().split())
al = list(map(int, input().split()))
bl = [0] * m
for _ in range(n):
    xl = list(map(int, input().split()))
    for j, x in enumerate(xl):
        bl[j] += x

for a, b in zip(al, bl):
    if a > b:
        print("No")
        exit()
print("Yes")
