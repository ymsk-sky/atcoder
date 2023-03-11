import sys
sys.setrecursionlimit(10**8)

n = int(input())

ans = 0
def dfs(crt):
    if crt > n:
        return
    global ans
    ans += 1
    dfs(crt + 1)

dfs(0)
