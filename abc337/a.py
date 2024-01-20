n = int(input())
a = b = 0
for _ in range(n):
    x, y = map(int, input().split())
    a += x
    b += y
if a > b:
    print("Takahashi")
elif a < b:
    print("Aoki")
else:
    print("Draw")
