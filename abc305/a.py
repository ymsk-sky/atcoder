n = int(input())
ans = min([(abs(i - n), i) for i in range(0, 101, 5)])[1]
print(ans)
