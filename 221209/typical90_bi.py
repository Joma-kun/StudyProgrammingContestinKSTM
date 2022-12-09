q = int(input())
d = []
for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        d.insert(0, x)
    elif t == 2:
        d.append(x)
    else:
        print(d[x-1])