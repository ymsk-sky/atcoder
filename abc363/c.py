from itertools import permutations

def encode(l):
    """いい感じに文字を圧縮する
    abc -> abc
    azd -> acb
        a: 0, z:25, d: 3
    """
    d = {c: i for i, c in enumerate(sorted(set(l)))}
    return "".join([chr(d[c] + 97) for c in l])

n, k = map(int, input().split())
s = encode(input())

if len(set(s)) == n:
    import math
    print(math.factorial(n))
    exit()

ans = 0
fin = set()
for per in permutations(s):
    t = "".join(per)
    if t in fin:
        continue
    # 判定
    for i in range(n - k + 1):
        cnt = 0
        for j in range(k // 2):
            if t[i + j] == t[i + k - 1 - j]:
                cnt += 1
        if cnt == k // 2:
            break
    else:
        ans += 1
    fin.add(t)
print(ans)
