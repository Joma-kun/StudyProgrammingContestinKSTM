h, w = map(int, input().split())
ans = 0

if h == 1 or w == 1:
    ans = h + w - 1
else:
    for i in range(h):
        if i%2 == 0:
            if w%2 == 0:
                ans += w//2
            else:
                ans += w//2 + 1

print(ans)