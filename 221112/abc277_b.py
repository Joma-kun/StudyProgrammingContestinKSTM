n = int(input())
ans = ("Yes")
temp = []

for i in range(n):
    s = str(input())
    if s[0] != "H" and s[0] != "D" and s[0] != "C" and s[0] != "S":
        ans = "No"
    if s[1] != "A" and s[1] != "2" and s[1] != "3" and s[1] != "4" and s[1] != "5" and s[1] != "6" and s[1] != "7" and s[1] != "8" and s[1] != "9" and s[1] != "T" and s[1] != "J" and s[1] != "Q" and s[1] != "K":
        ans = "No"
    if s in temp:
        ans = "No"
    else:
        temp.append(s)
print(ans)