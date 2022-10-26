s = list(input())
ans = int(0)

for i in range(len(s)):
    if s[i] == str(1):
        ans += 1

print(ans)