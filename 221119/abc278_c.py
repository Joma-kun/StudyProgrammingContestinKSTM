from collections import defaultdict

n, q = map(int, input().split())
d = defaultdict(set)

for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if b not in d[str(a)]:
            d[str(a)].add(b)
    elif t == 2:
        if b in d[str(a)]:
            d[str(a)].discard(b)
    else:
        if a in d[str(b)] and b in d[str(a)]:
            print("Yes")
        else:
            print("No")