s = input()
n = len(s)
if s[0] == "<" and s[-1] == ">" and s[1:-1] == "=" * (n - 2):
    print("Yes")
else:
    print("No")
