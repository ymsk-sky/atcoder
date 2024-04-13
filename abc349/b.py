from collections import Counter

s = input()
c = Counter(s)
d = dict()
for k, v in c.items():
    if v in d:
        d[v].append(k)
    else:
        d[v] = [k]
for k in d:
    if len(d[k]) == 0 or len(d[k]) == 2:
        continue
    else:
        print("No")
        exit()
print("Yes")
