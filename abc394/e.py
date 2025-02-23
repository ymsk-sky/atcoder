"""01-BFS
頂点を(i,j)で考える.
コード的には頂点を実際に作成するのではなく
長さ0,1の辺を先にキューに追加した後に長さ2の辺を処理していく

like: 超頂点
"""

from collections import deque

n = int(input())
cl = [input() for _ in range(n)]

al = [[-1] * n for _ in range(n)]
que = deque()
for i in range(n):
    al[i][i] = 0
    que.appendleft((i*n + i))
    for j in range(n):
        if i == j:
            continue
        if cl[i][j] == "-":
            continue
        al[i][j] = 1
        que.append(i*n + j)

while que:
    crt = que.popleft()
    i, j = crt // n, crt % n
    for k in range(n):
        for l in range(n):
            if cl[k][i] == "-" or cl[j][l] == "-":
                continue
            if cl[k][i] != cl[j][l]:
                continue
            if al[k][l] >= 0:
                continue
            al[k][l] = al[i][j] + 2
            que.append(k*n + l)

for a in al:
    print(*a)


"""
10
aaaaaaaaaa
bbbbbbbbbb
cccccccccc
dddddddddd
eeeeeeeeee
ffffffffff
gggggggggg
hhhhhhhhhh
iiiiiiiiii
jjjjjjjjjj

"""