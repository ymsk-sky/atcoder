n = int(input())
al = list(map(int, input().split()))
s = input()

M0 = [0] * (n + 1)
M1 = [0] * (n + 1)
M2 = [0] * (n + 1)
X0 = [0] * (n + 1)
X1 = [0] * (n + 1)
X2 = [0] * (n + 1)
for i in range(n):
    a = al[i]
    c = s[i]
    if c == "M":
        if a == 0:
            M0[i + 1] += 1
        elif a == 1:
            M1[i + 1] += 1
        else:
            M2[i + 1] += 1
    elif c == "X":
        if a == 0:
            X0[i + 1] += 1
        elif a == 1:
            X1[i + 1] += 1
        else:
            X2[i + 1] += 1
    M0[i + 1] += M0[i]
    M1[i + 1] += M1[i]
    M2[i + 1] += M2[i]
    X0[i + 1] += X0[i]
    X1[i + 1] += X1[i]
    X2[i + 1] += X2[i]

ans = 0
for j in range(1, n + 1):
    c = s[j - 1]
    if c != "E":
        continue
    # Eなので前後のMとXの個数を調べる
    m0_num = M0[j]
    m1_num = M1[j]
    m2_num = M2[j]
    x0_num = X0[n] - X0[j]
    x1_num = X1[n] - X1[j]
    x2_num = X2[n] - X2[j]
    a = al[j - 1]
    if a == 0:
        ans += 1 * (m0_num*x0_num + m0_num*x2_num + m2_num*x0_num + m2_num*x2_num)
        ans += 2 * (m0_num*x1_num + m1_num*x0_num + m1_num*x1_num)
        ans += 3 * (m1_num*x2_num + m2_num*x1_num)
    elif a == 1:
        ans += 2 * (m0_num*x0_num + m0_num*x1_num + m1_num*x0_num)
        ans += 3 * (m0_num*x2_num + m2_num*x0_num)
    elif a == 2:
        ans += 1 * (m0_num*x0_num + m0_num*x2_num + m2_num*x0_num)
        ans += 3 * (m0_num*x1_num + m1_num*x0_num)
print(ans)

"""
- 1 <= i<j<k <=n
- Si Sj Sk = "MEX"
を満たすmex()
"""
