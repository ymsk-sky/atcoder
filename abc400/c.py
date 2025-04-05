from math import isqrt

n = int(input())

# ans = int((n // 2)**0.5) + int((n // 4)**0.5)
# print(ans)
ans = isqrt(n // 2) + isqrt(n // 4)
print(ans)
