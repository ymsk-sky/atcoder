n = int(input())
s = input()
a = b = c = 0
for i in range(n):
    if s[i] == "A":
        a = 1
    if s[i] == "B":
        b = 1
    if s[i] == "C":
        c = 1
    if a and b and c:
        print(i + 1)
        break
