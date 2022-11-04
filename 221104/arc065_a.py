s = str(input())
s = s[::-1]
li = ["maerd",  "remaerd", "esare", "resare"]
l = len(s)

while l > 0:
    if s[0:5] == li[0] or s[0:5] == li[2]:
        s = s[5:]
        l -= 5
    elif s[0:6] == li[3]:
        s = s[6:]
        l -= 6
    elif s[0:7] == li[1]:
        s = s[7:]
        l -= 7
    else:
        print("NO")
        exit()
print("YES")