n = int(input())

def level(k):
    if k == 0:
        return ["#"]
    ml = []
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                # 中央
                m = ["." * 3**(k - 1)] * 3**(k - 1)
            else:
                m = level(k - 1)
            ml.append(m)
    res = []
    for a, b, c in zip(ml[0], ml[1], ml[2]):
        res.append(a + b + c)
    for a, b, c in zip(ml[3], ml[4], ml[5]):
        res.append(a + b + c)
    for a, b, c in zip(ml[6], ml[7], ml[8]):
        res.append(a + b + c)
    return res

ans = level(n)
for an in ans:
    print(*an, sep="")
