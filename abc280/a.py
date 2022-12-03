h, s = map(int, input().split())
ans = 0
for i in range(h):
    s = input()
    ans += s.count("#")
print(ans)