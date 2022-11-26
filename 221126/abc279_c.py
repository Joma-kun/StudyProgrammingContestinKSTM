#TLE
h, w = map(int, input().split())
ss = [""]*w
tt = [""]*w

for i in range(h):
    tem = str(input())
    for j in range(w):
        ss[j] += tem[j]
for i in range(h):
    tem = str(input())
    for j in range(w):
        tt[j] += tem[j]

s = set(ss)
t = set(tt)

if s == t:
    print("Yes")
else:
    print("No")