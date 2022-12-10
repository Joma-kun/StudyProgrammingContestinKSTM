s = str(input())
ans = "No"
if len(s) != 8:
    print(ans)
    exit()
else:
    s1 = s[:1]
    s2 = s[1:7]
    s3 = s[7:]
    if s2.isdecimal():
        s2 = int(s2)
    else:
        print("No")
        exit()
    if s1.isupper() and s3.isupper() and 100000 <= s2 and s2 <= 999999:
        print("Yes")
    else:
        print("No")