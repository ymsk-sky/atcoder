"""
10進数表記のnをb進数のリストで表す

例)
to_base(98, 11) = [8, 10]
11進数を0123456789Aで表すとき, 10はA
"""

def to_base(n, b):
    res = []
    while n >= b:
        res.append(n%b)
        n //= b
    res.append(n)
    return res[::-1]

print(to_base(98, 11))