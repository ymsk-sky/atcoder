n = int(input())
l = []
for i in range(1, n + 1):
    a, c = map(int, input().split())
    l.append((a, c, i))
l.sort(key=lambda e: e[1])  # コスト順
r = [l.pop()]
while len(l) > 0:
    card_l = l.pop()
    if len(r) == 0:
        r.append(card_l)
        continue
    card_r = r.pop()
    if card_l[0] < card_r[0]:
        r.append(card_r)
        r.append(card_l)
    else:
        l.append(card_l)

print(len(r))
print(*sorted([e[2] for e in r]))
