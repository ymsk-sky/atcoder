"""AHC041 A - Christmas Tree Cutting
after contest
未完了の頂点の内, DFSして木を作った際に最も(木のスコア/木の頂点数)が良いものを採用していく
"""

import sys

sys.setrecursionlimit(10**8)

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
    edges = [sorted(e, key=lambda i: al[i]) for e in edges]
    xyl = [list(map(int, input().split())) for _ in range(N)]  # xyl[i]: 頂点iの座標(x, y)

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

    use = []
    def dfs_confirm(crt: int) -> None:
        for nxt in edges[crt]:
            if hl[nxt] > -1:
                continue
            hl[nxt] = hl[crt] + 1
            pl[nxt] = crt
            use.append(nxt)
            if hl[nxt] < H:
                dfs_confirm(nxt)

    def calc_tree_score(ul: list) -> int:
        res = 0
        for u in ul:
            res += (hl[u] + 1) * al[u]
        return res

    while 1:
        ul = []
        scores = []
        for u in range(N):
            if hl[u] > -1:
                continue
            use = [u]
            ul.append(u)
            hl[u] = 0
            dfs_confirm(u)
            score = calc_tree_score(use)
            num = len(use)
            scores.append(score / num)
            for i in use:
                pl[i] = -1
                hl[i] = -1
        if len(ul) == 0:
            break
        U = ul[max(range(len(scores)), key=lambda i: scores[i])]
        hl[U] = 0
        dfs(U)
    print(*pl)


if __name__ == "__main__":
    solve()
