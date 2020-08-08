h,w=map(int,input().split())
l=[input() for _ in range(h)]
print('#'*(w+2))
for a in l:
    print('#{}#'.format(a))
print('#'*(w+2))
