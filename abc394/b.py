n = int(input())
sl = [input() for _ in range(n)]
sl.sort(key=lambda s: len(s))
print("".join(sl))
