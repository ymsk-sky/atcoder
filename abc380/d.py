s = input()
n = len(s)
q = int(input())
kl = list(map(int, input().split()))

def rev(c: str) -> str:
    if c.islower():
        return c.upper()
    return c.lower()

ans = []
for k in kl:
    k -= 1
    x = 0
    while k >= 2**x * n:
        x += 1
    i = k - 2**(x - 1) * n if x > 0 else k
    c = s[i % n]

    cnt = 0
    m = k // n
    for y in range(60, -1, -1):
        if 2**y > m:
            continue
        m -= 2**y
        cnt += 1

    if cnt % 2 == 0:
        ans.append(c)
    else:
        ans.append(rev(c))
print(*ans)
