n = int(input())
x, y = 0, 0
temp = 0
for _ in range(n):
    a = list(map(int, input().split()))
    a[0] -= temp
    dx = x-a[1]
    dy = y-a[2]
    if a[0] < (dx+dy):
        print("No")
        exit()
    for i in range(a[0]):
        if x == a[1] and y == a[2] and (a[0] - i) % 2 == 0:
            break
        elif x < a[1]:
            x += 1
        elif x > a[1]:
            x -= 1
        elif y < a[2]:
            y += 1
        elif y > a[2]:
            y -= 1
        else:
            print("No")
            exit()
    temp += a[0]
if x == a[1] and y == a[2]:
    print("Yes")
else:
    print("No")