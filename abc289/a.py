s = input()
print(*[1 if c == "0" else 0 for c in s], sep="")
