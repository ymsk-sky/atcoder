s = input()
al = [len(c) for c in s.split("|") if c]
print(*al)
