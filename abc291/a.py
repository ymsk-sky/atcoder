s = input()
for i in range(1, len(s) + 1):
    c = s[i - 1]
    if c.isupper():
        print(i)
        exit()
