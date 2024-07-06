from collections import deque

n = int(input())
s = input()
t = input()
if s.count("B") != t.count("B"):
    print(-1)
    exit()

fin = {s + "..": 0}
que = deque([s + ".."])
while que:
    state = que.popleft()
    p = state.find(".")  # p, p + 1 が空き
    i = 0
    while i < n + 1:
        if i == p or i + 1 == p or i == p + 1:
            i += 1
            continue
        new = list(state)
        new[p], new[p + 1] = new[i], new[i + 1]
        new[i], new[i + 1] = ".", "."
        new = "".join(new)
        if new not in fin:
            fin[new] = fin[state] + 1
            que.append(new)
        i += 1

if t + ".." in fin:
    print(fin[t + ".."])
else:
    print(-1)
