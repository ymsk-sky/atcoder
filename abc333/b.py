s = input()
t = input()

a = {"AB", "BA", "BC", "CB", "CD", "DC", "DE", "ED", "EA", "AE"}
b = {"AC", "CA", "AD", "DA", "BD", "DB", "BE", "EB", "CE", "EC"}
if (s in a and t in a) or (s in b and t in b):
    print("Yes")
else:
    print("No")
