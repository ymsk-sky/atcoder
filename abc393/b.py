s = input()
n = len(s)

ans = 0
for i in range(n):
    if s[i] == "A":
        for j in range(1, n):
            if i + j > n - 1:
                break
            if s[i + j] == "B":
                if i + 2*j <= n - 1 and s[i + 2*j] == "C":
                    ans += 1
print(ans)
