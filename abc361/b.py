a, b, c, d, e, f = list(map(int, input().split()))
g, h, i, j, k, l = list(map(int, input().split()))

def is_common(l1, r1, l2, r2):
    """[l1,r1]と[l2,r2]に共通部分が存在するか(長さが正か)"""
    return not (r1 <= l2 or r2 <= l1)

if is_common(a, d, g, j) and is_common(b, e, h, k) and is_common(c, f, i, l):
    print("Yes")
else:
    print("No")
