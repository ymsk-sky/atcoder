h, w = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(h)]
for a in al:
    print(*["." if c == 0 else chr(c + 64) for c in a], sep="")
