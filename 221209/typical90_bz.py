n, m = map(int, input().split())
l = [[] for _ in range(n)]
ans = 0

for i in range(m):
    a, b = map(int, input().split())
    l[a-1].append(b-1)
    l[b-1].append(a-1)

for j in range(n):
    temp = 0
    for k in l[j]:
        if k < j:
            temp += 1
    if temp == 1:
        ans += 1

print(ans)