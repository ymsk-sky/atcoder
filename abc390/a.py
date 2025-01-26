al = list(map(int, input().split()))
for i in range(4):
    al[i], al[i + 1] = al[i + 1], al[i]
    if al == list(range(1, 6)):
        print("Yes")
        break
    al[i], al[i + 1] = al[i + 1], al[i]
else:
    print("No")
