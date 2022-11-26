#TLE
import math
a, b = map(int, input().split())
pre = a
g = 1
cnt = 0
f = 1
while f == 1:
    g += 1
    cnt += 1
    next = (a / math.sqrt(g)) + b*cnt
    print(next)
    if pre > next:
        pre = next
    else:
        print(pre)
        f = 0