from collections import Counter

n = int(input())
kl = []
cnts = []
for _ in range(n):
    k, *al = list(map(int, input().split()))
    kl.append(k)
    C = Counter(al)
    cnts.append(C)

ans = [0, 1]  # [分子, 分母]
for i in range(n - 1):
    k_a = kl[i]
    cnt_a = cnts[i]
    for j in range(i + 1, n):
        k_b = kl[j]
        cnt_b = cnts[j]
        tmp = 0
        for a, c in cnt_a.items():
            if a in cnt_b:
                tmp += c*cnt_b[a]
        # ans[0]/ans[1] < tmp/(k_a*k_b): update
        if ans[0]*k_a*k_b < tmp*ans[1]:
            ans = [tmp, k_a*k_b]
print(ans[0] / ans[1])


"""
3
3 1 2 3
4 1 2 2 1
6 1 2 3 4 5 6
"""