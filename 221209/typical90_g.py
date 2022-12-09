n = int(input())
a = list(map, int(input().split()))
a.sort()
q = int(input())

for _ in range(q):
    b = int(input())
    l = 0
    h = n-1
    while h >= l:
        m = (h+l) // 2
        if b >= a[m]:
            l = m
        else:
            h = m
    print(a[h], a[l])