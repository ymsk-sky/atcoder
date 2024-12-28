n, m = map(int, input().split())
dd = dict()
for _ in range(m):
    x, y, c = input().split()
    x, y = int(x), int(y)
    if x not in dd:
        dd[x] = [[], []]
    if c == "B":
        dd[x][0].append(y)
    else:
        dd[x][1].append(y)

black_lim = n
white_lim = n + 1
for x in sorted(dd.keys()):
    black = sorted(dd[x][0])
    white = sorted(dd[x][1])
    if len(black) == 0:
        black.append(-1)
    else:
        # 上の行との整合性
        if black[-1] > black_lim:
            print("No")
            exit()
    if len(white) == 0:
        white.append(n + 1)
    else:
        # 行自体の整合性
        if white[0] <= black[-1]:
            print("No")
            exit()
    # limの更新
    white_lim = min(white_lim, white[0])
    black_lim = min(black_lim, white_lim - 1)

print("Yes")
