from collections import deque

s = input()
n = len(s)
box = [-1] * 26  # box[i]: アルファベットiを何番目で入れたかを管理
que = deque()  # "("が何番目に何個目があるかを管理
for i in range(n):
    c = s[i]
    if c == "(":
        # 何もしない
        que.append(i)
        continue
    elif c == ")":
        # j(<i)であってs[j] ~ s[i]の文字からなる文字列がいい文字列となる最大の整数jを取る
        # j~i番目で箱に入れたボールをすべて取り出す
        j = que.pop()
        for k in range(26):
            if j <= box[k] <= i:
                box[k] = -1
    else:
        # 英小文字: その文字のボールを箱に入れる. ただしすでに入っているならNo
        a = ord(c) - 97
        if box[a] >= 0:
            print("No")
            exit()
        else:
            box[a] = i
print("Yes")

"""
1<=|s|<=3*10**5
"""
