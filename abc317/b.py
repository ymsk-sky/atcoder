n = int(input())
al = list(map(int, input().split()))
al.sort()
for a, b in zip(al, al[1:]):
    if a + 1 != b:
        print(a + 1)
        exit()
