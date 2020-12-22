"""
ABC038 - C 参考
https://atcoder.jp/contests/abc038/tasks/abc038_c

ABC130 D問題 - 部分数列がK以上となる部分の数え上げ
"""

# 入力受付
n = int(input())
l = list(map(int, input().split())) + [-1]

def sum_return(n):
    return n*(n+1)//2

ans = 0
cnt = 0
pre = -1

for i in range(n+1):
    # 条件外れるまでカウント
    if l[i] > pre:
        cnt += 1
    else:
        # カウントした長さ分の部分数列を追加
        ans += sum_return(cnt)
        # カウントリセット
        cnt = 1
    pre = l[i]

print(ans)
