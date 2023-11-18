n = int(input())
al = list(map(int, input().split()))
ans = sorted(set(al), reverse=True)[1]
print(ans)
