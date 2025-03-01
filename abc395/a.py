n = int(input())
al = list(map(int, input().split()))
for a1, a2 in zip(al, al[1:]):
    if a1 >= a2:
        print("No")
        break
else:
    print("Yes")
