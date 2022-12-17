n, m = map(int, input().split())
sl = [input() for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for a, b in zip(sl[i], sl[j]):
            if a == "o" or b == "o":
                pass
            else:
                break
        else:
            ans += 1
print(ans)
