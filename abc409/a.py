n = int(input())
t = input()
a = input()

for i in range(n):
    if t[i] == a[i] == "o":
        print("Yes")
        break
else:
    print("No")
