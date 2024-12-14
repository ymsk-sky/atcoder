n, s = map(int, input().split())
al = list(map(int, input().split()))

s %= sum(al)
if s == 0:
    print("Yes")
    exit()

right = 0
t = 0
for left in range(2*n):
    while right < 2*n and t + al[right % n] <= s:
        t += al[right % n]
        right += 1
    if t == s:
        print("Yes")
        exit()
    if left == right:
        right += 1
    else:
        t -= al[left % n]
print("No")
