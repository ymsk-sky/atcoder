"""ABC030で使用
長さが10**6とかある数字の引き算(繰り下がり対応).
ただしint(a)>=int(b)
"""
a = input()
b = input()
al = [int(v) for v in a]
bl = [int(v) for v in b]
a_n = len(a)
b_n = len(b)
for i in range(b_n):
    if al[a_n - 1 - i] >= bl[b_n - 1 - i]:
        al[a_n - 1 - i] -= bl[b_n - 1 - i]
    else:
        # 繰り下がり
        al[a_n - 1 - i] += 10 - bl[b_n - 1 - i]
        j = a_n - 1 - i - 1
        while 1:
            if al[j] != 0:
                al[j] -= 1
                break
            al[j] = 9
            j -= 1
print("".join(al))  # 桁数は引き算の前のままで先頭に0が残るので注意(そのままintにはできる)


"""ABC030で使用
長さが10**6とかある数字aの int(a)%mod を求める.
"""
a = input()
mod = int(input())
a_n = len(a)
res = 0
for i in range(a_n):
    res += a[i] * pow(10, a_n - i - 1, mod)
    res %= mod
print(res)
