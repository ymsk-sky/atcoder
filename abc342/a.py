from collections import Counter

s = input()
c = Counter(s)
ch = min(c.keys(), key=lambda k: c[k])
print(s.index(ch) + 1)