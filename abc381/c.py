n = int(input())
s = input()
ans = 0

def check(i: int) -> int:
    j = i - 1
    left = 0
    while j >= 0:
        if s[j] == "1":
            left += 1
        else:
            break
        j -= 1
    k = i + 1
    right = 0
    while k < n:
        if s[k] == "2":
            right += 1
        else:
            break
        k += 1
    return 1 + 2*min(left, right)

for i in range(n):
    if s[i] == "/":
        tmp = check(i)
        if tmp > ans:
            ans = tmp
print(ans)
