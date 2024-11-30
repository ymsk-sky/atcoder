n, d = map(int, input().split())
s = input()
ans = n - s.count("@") + d
print(ans)
