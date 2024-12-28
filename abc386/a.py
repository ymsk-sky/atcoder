l = list(map(int, input().split()))

cards = {}
for x in l:
    if x in cards:
        cards[x] += 1
    else:
        cards[x] = 1

if len(cards) != 2:
    print("No")
    exit()

v1, v2 = list(sorted(cards.values()))
if (v1 == 2 and v2 == 2) or (v1 == 1 and v2 == 3):
    print("Yes")
else:
    print("No")
