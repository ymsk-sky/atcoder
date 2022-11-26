h, w = map(int, input().split())
s = [[] for _ in range(w)]
for _ in range(h):
    l = input()
    for j in range(w):
        s[j].append(l[j])
t = [[] for _ in range(w)]
for _ in range(h):
    l = input()
    for j in range(w):
        t[j].append(l[j])

s.sort()
t.sort()
for i in range(w):
    if s[i] != t[i]:
        print("No")
        exit()
print("Yes")