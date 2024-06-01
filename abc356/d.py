n, m = map(int, input().split())
mod = 998244353

# 0~nの間に各桁のビットが立つ回数
k = n.bit_length()
nums = [0] * k
for i in range(k):
    loop = (1 << i + 1)  # loopにloop//2回ビットが立つ
    half = loop // 2
    tmp = (n + 1) // loop * half  # ループ分
    tmp += max(0, ((n + 1) % loop) - half)  # 端数分
    nums[i] = tmp
ans = 0
for i, num in enumerate(nums):
    if (m >> i) & 1:
        ans += num
        ans %= mod
print(ans)



"""
0<=n<2**60
0<=m<2**60

A B &
0 0 0
0 1 0
1 0 0
1 1 1
"""
