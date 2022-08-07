l = list(map(int, input().split()))
for a in l:
    c = l.count(a)
    if c == 2 or c == 3:
        continue
    else:
        print("No")
        exit()
print("Yes")
