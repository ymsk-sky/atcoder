"""X解説
8899AABBCC
 44556677
  112233
   0011
    xx
xxから1つ上下への移動のみで横を兼ねて実現可能なので
この範囲内なら縦だけ考える.
その外の場合のみ追加で考える.

解説
簡単のためスタートとゴールはタイルの左側に移動しておく(枚数は変化しないため)

"""

sx, sy = map(int, input().split())
tx, ty = map(int, input().split())

if (sx + sy) % 2 == 1:
    sx -= 1
if (tx + ty) % 2 == 1:
    tx -= 1

dx = abs(sx - tx)
dy = abs(sy - ty)
ans = (dy + max(dx, dy)) // 2
print(ans)
