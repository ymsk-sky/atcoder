n = int(input())
sl = [input() for _ in range(n)]
print(*sl[::-1], sep="\n")