import sys

sys.setrecursionlimit(10**7)

n = int(input())
al = list(map(int, input().split()))

s = set()
gl: list[int] = []

def xor() -> int:
    res = gl[0]
    for g in gl[1:]:
        res ^= g
    return res

def dfs(i: int, k: int) -> None:
    a = al[i]
    for j in range(k + 1):
        if j == k:
            gl.append(a)
            if i < n - 1:
                dfs(i + 1, len(gl))
            else:
                s.add(xor())
            gl.pop()
        else:
            gl[j] += a
            if i < n - 1:
                dfs(i + 1, len(gl))
            else:
                s.add(xor())
            gl[j] -= a

dfs(0, 0)
print(len(s))
