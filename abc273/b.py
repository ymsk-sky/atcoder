from decimal import Decimal, ROUND_HALF_UP
x, k = map(int, input().split())
x = Decimal(str(x))
for i in range(k):
    x = x / Decimal(str(10 ** (i + 1)))
    x = x.quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    x = x * Decimal(str(10 ** (i + 1)))
print(x)