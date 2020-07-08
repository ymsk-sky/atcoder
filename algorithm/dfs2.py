"""
ATC001 - A 参照
https://atcoder.jp/contests/atc001/tasks/dfs_a

(example input)
4 5
s####
....#
#####
#...g
"""
import sys; sys.setrecursionlimit(10**7)  # 再帰呼び出し回数を設定

h, w = map(int,input().split())
m = [list(input()) for _ in range(h)]

def search(x, y):
    if x<0 or h<=x or y<0 or w<=y or m[x][y]=='#':
        return
    if m[x][y] == 'g':
        print('Yes')
        exit()
    m[x][y] = '#'
    search(x+1, y)
    search(x-1, y)
    search(x, y+1)
    search(x, y-1)

# スタート地点を探索
for i in range(h):
    for j in range(w):
        if m[i][j] == 's':
            sx, sy = i, j
            break
search(sx, sy)
print('No')
