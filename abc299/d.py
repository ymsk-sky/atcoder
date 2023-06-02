n = int(input())
left = 1
right = n
for _ in range(20):
    mid = (left + right)//2
    print("?", mid)
    v = int(input())
    if v == 1:
        right = mid
    elif v == 0:
        left = mid
print("!", left)

"""
# 0010011
? 4 -> 0
? 5 -> 0
? 6 -> 1
left = 5
right = 6
"""
