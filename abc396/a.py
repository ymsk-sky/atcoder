n = int(input())
al = list(map(int, input().split()))

for i in range(n - 2):
    if al[i] == al[i + 1] == al[i + 2]:
        print("Yes")
        break
else:
    print("No")
