n = int(input())

def to_base(n, b):
    res = []
    while n >= b:
        res.append(n%b)
        n //= b
    res.append(n)
    return res[::-1]

d = {i: v for i, v in enumerate("02468")}
res = "".join([d[v] for v in to_base(n - 1, 5)])
print(res)
