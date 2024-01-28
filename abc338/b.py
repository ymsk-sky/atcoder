from collections import Counter

s = input()
c = Counter(s)
m = c.most_common()
m.sort(key=lambda e: (-e[1], e[0]))
print(m[0][0])
