n = int(input())
for i in range(3, 10):
    if n <= 10**i - 1:
        x = i - 3
        print(n if x == 0 else str(n)[:-x] + "0"*x)
        break
