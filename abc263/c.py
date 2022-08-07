import itertools
n, m = map(int, input().split())
for c in itertools.combinations(range(1, m + 1), n):
    print(" ".join([str(a) for a in c]))
