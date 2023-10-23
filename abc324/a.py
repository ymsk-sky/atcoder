n = int(input())
al = list(map(int, input().split()))
print("Yes" if len(set(al)) == 1 else "No")
