from itertools import permutations

al = list(map(int, input().split()))
for pl in permutations(al, 5):
    if len(set(pl)) != 2:
        continue
    for p in pl:
        c = pl.count(p)
        if c == 2 or c == 3:
            continue
        break
    else:
        print("Yes")
        exit()
print("No")
