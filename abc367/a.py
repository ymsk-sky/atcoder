a, b, c = map(int, input().split())
if b < c:
    print("No" if b < a < c else "Yes")
else:
    print("Yes" if c < a < b else "No")
