s, t = input().split()
for w in range(1, len(s)):
    l = []
    i = 0
    while 1:
        tmp = s[i:i + w]
        if len(tmp) == 0:
            break
        l.append(tmp)
        i += w
    for c in range(w):
        word = "".join([tmp[c] for tmp in l if len(tmp) > c])
        if t == word:
            print("Yes")
            exit()
print("No")
