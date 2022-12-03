k = int(input())

arr = set()

def fa(k):
    tmp = k
    for i in range(2, int(-(-k ** 0.5 // 1)) + 1):
        if tmp % i == 0:
            tmp //= i
            if not i in arr:
                arr.add(i)
            else:
                while 1:
                    i *= 2
                    if not i in arr:
                        break
                arr.add(i)
    if tmp != 1:
        if not tmp in arr:
            fa(tmp)
        else:
            arr.add(tmp)
    if arr == []:
        if not k in arr:
            arr.add(k)

fa(k)

m = max(arr)
print(m)

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr



"""
2<=k<=10**12
"""
