k, g, m = map(int, input().split())
gw = 0
mw = 0
for _ in range(k):
    if gw == g:
        gw = 0
    elif mw == 0:
        mw = m
    else:
        gw, mw = min(g, mw), max(0, mw - (g - gw))
print(gw, mw)
