n = int(input())
l = 1 if n % 2 else 2
m = (n - l) // 2

ans = "-" * m + "=" * l + "-" * m
print(ans)
