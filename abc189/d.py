n = int(input())
sl = [input() for _ in range(n)]
y0 = 1
y1 = 1
for s in sl:
    if s == "OR":
        y0, y1 = y0*1, y0*1 + y1*2
    elif s == "AND":
        y0, y1 = y0*2 + y1*1, y1*1
print(y1)
