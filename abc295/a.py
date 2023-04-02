n = int(input())
wl = input().split()
l = ("and", "not", "that", "the", "you")
for w in wl:
    if w in l:
        print("Yes")
        break
else:
    print("No")
