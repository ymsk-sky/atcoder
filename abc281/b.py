s = input()
if len(s) == 8 and s[0].isalpha() and s[1:-1].isdecimal() and s[-1].isalpha():
    if 100000 <= int(s[1:-1]) <= 999999:
        print("Yes")
    else:
        print("No")
else:
    print("No")