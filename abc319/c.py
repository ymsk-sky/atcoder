from itertools import permutations

cl = [list(map(int, input().split())) for _ in range(3)]
cnt = 0
for p in permutations(range(9)):
    l = [[0] * 3 for _ in range(3)]
    for i, x in enumerate(p):
        l[x//3][x%3] = i
    # check 8 pattern
    for y in ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)):
        tmp = [(l[x//3][x%3], cl[x//3][x%3]) for x in y]
        tmp.sort()
        if tmp[0][1] == tmp[1][1]:
            cnt += 1
            break
print(1 - cnt/362880)
