a, b = map(int, input().split())
ans = set()
for x in range(-1000, 1001):
    l = [(a, b, x), (a, x, b), (x, a, b), (b, a, x), (b, x, a), (x, b, a)]
    for p, q, r in l:
        if q - p == r - q:
            ans.add(x)
print(len(ans))


"""
A B x
A x B
x A B

B A x
B x A
x B A

A, B, C
B - A == C - B
"""