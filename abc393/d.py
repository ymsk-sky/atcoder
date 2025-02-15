n = int(input())
s = input()

pos = []
for i in range(n):
    if s[i] == "1":
        pos.append(i)
m = len(pos)  # 1の個数

r = [0]
cnt = 1
for il, ir in zip(pos, pos[1:]):
    tmp = (ir - il - 1)*cnt
    r.append(r[-1] + tmp)
    cnt += 1

l = [0] * m
cnt = 1
for idx, (ir, il) in enumerate(zip(pos[::-1], pos[::-1][1:])):
    tmp = (ir - il - 1)*cnt
    l[m - idx - 2] = l[m - idx - 1] + tmp
    cnt += 1

ans = float("inf")
for i in range(m):
    ans = min(ans, r[i] + l[i])
print(ans)


print(pos)
print(r)
print(l)

"""

100000000000101
100000000000110 +1

111001101
"""