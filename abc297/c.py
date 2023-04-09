h, w = map(int, input().split())
sl = [input() for _ in range(h)]
for s in sl:
    print(s.replace("TT", "PC"))
