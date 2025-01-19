"""AHC041 A - Christmas Tree Cutting
after contest
未完了の頂点の内, 美しさが小さい順にDFSのみ
"""

import sys

sys.setrecursionlimit(10**7)

def input() -> str:
    return sys.stdin.readline().strip()

def solve() -> None:
    # 入力受付
    N, M, H = map(int, input().split())
    al = list(map(int, input().split()))  # al[i]: 頂点iの美しさ
    edges = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    xyl = [list(map(int, input().split())) for _ in range(N)]  # xyl[i]: 頂点iの座標(x, y)

    ul = sorted(range(N), key=lambda i: al[i])

    pl = [-1] * N
    hl = [-1] * N
    def dfs(crt: int) -> None:
        for nxt in edges[crt]:
            if hl[nxt] > -1:
                continue
            hl[nxt] = hl[crt] + 1
            pl[nxt] = crt
            if hl[nxt] < H:
                dfs(nxt)
    for u in ul:
        if hl[u] > -1:
            continue
        hl[u] = 0
        dfs(u)

    print(*pl)


if __name__ == "__main__":
    solve()
