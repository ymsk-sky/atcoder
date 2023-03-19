n = int(input())
al = list(map(int, input().split()))
print(*[a for a in al if a%2 == 0])
