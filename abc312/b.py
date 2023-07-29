n, m = map(int, input().split())
sl = [input() for _ in range(n)]
for i in range(n - 8):
    for j in range(m - 8):
        x = False
        for a in range(3):
            for b in range(3):
                if sl[i + a][j + b] == ".":
                    x = True
                if sl[i + 6 + a][j + 6 + b] == ".":
                    x = True
        for a in range(3):
            if sl[i + a][j + 3] == "#":
                x = True
            if sl[i + 6 + a][j + 5] == "#":
                x = True
        for b in range(4):
            if sl[i + 3][j + b] == "#":
                x = True
            if sl[i + 5][j + 5 + b] == "#":
                x = True
        if not x:
            print(i + 1, j + 1)


"""
9 21
###.#...........#.###
###.#...........#.###
###.#...........#.###
....#...........#....
#########...#########
....#...........#....
....#.###...###.#....
....#.###...###.#....
....#.###...###.#....
"""