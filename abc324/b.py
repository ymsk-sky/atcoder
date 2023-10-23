n = int(input())
for x in range(60):
    for y in range(38):
        if 2**x * 3**y == n:
            print("Yes")
            exit()
print("No")
