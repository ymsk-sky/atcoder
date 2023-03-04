def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return len(lower_divisors + upper_divisors[::-1])

n = int(input())
ans = 0
l = [make_divisors(x) for x in range(n + 1)]

for x in range(1, n):
    y = n - x
    ans += l[x]*l[y]
print(ans)

"""
x 1 2 3
y 3 2 1
"""
