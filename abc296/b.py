s = [input() for _ in range(8)]
x = "87654321"
y = "abcdefgh"
for i in range(8):
    for j in range(8):
        if s[i][j] == "*":
            print(y[j], x[i], sep="")
            exit()
