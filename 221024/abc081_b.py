n = int(input())
a = list(map(int, input().split()))
ans = 0
flag = True

while flag:
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] /= 2
        else:
            flag = False
            ans -= 1
            break
    ans += 1
print(ans)