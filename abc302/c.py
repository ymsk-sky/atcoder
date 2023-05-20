from itertools import permutations

n, m = map(int, input().split())
s = [input() for _ in range(n)]

for per in permutations(s):
    for s1, s2 in zip(per, per[1:]):
        cnt = 0
        for a, b in zip(s1, s2):
            if a != b:
                cnt += 1
        if cnt != 1:
            break
    else:
        print("Yes")
        exit()

print("No")
