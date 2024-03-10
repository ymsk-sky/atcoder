n = int(input())
al = list(map(int, input().split()))
m = int(input())
bl = list(map(int, input().split()))
l = int(input())
cl = list(map(int, input().split()))
q = int(input())
xl = list(map(int, input().split()))

s = set()
for a in al:
    for b in bl:
        for c in cl:
            s.add(a + b + c)
for x in xl:
    print("Yes" if x in s else "No")
