n, q = map(int, input().split())
al_l = []
for _ in range(n):
    l, *al = list(map(int, input().split()))
    al_l.append(al)

stl = [list(map(int, input().split())) for _ in range(q)]

for s, t in stl:
    print(al_l[s - 1][t - 1])
