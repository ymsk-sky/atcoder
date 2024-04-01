n, a, b = map(int, input().split())
dl = list(map(int, input().split()))
w = a + b
dl = [d % w for d in dl]
dl = sorted(set(dl))
m = len(dl)

if m == 1:
    print("Yes")
    exit()

for i in range(m):
    # d1を休日の最終日, d2を休日の初日と仮定
    # その間がb(平日)日数より多ければ
    # d2 - d1ではないd1-d2間がすべて休日内
    d1 = dl[i]
    d2 = dl[(i + 1) % m]
    if (d2 - d1) % w > b:
        print("Yes")
        break
else:
    print("No")
