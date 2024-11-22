"""しゃくとり法
"""

n = int(input())
al = list(map(int, input().split()))

ll = []
i = 0
while i < n - 1:
    tmp = []
    while i < n - 1:
        if al[i] == al[i + 1]:
            tmp.append(al[i])
        else:
            break
        i += 2
    if tmp:
        ll.append(tmp)
        i -= 1
    else:
        i += 1
print(ll)
ans = 0
for l in ll:
    used = set()
    m = len(l)
    right = 0
    for left in range(m):
        while right < m:
            a = l[right]
            if a in used:
                break
            used.add(a)
            right += 1
        ans = max(ans, len(used))
        a = l[left]
        used.discard(a)
print(ans*2)
