from collections import Counter

n = int(input())
al = list(map(int, input().split()))

cl = Counter(al)
for k in sorted(cl.keys(), reverse=True):
    if cl[k] == 1:
        print(al.index(k) + 1)
        exit()
print(-1)
