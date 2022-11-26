s = str(input())
ans = 0

for i in range(len(s)):
    if s[i:i+1] == "v":
        ans += 1
    elif s[i:i+1] == "w":
        ans += 2

print(ans)