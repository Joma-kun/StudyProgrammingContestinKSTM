h, w = map(int, input().split())
s = [input() for i in range(h)]
t = [input() for i in range(h)]
ss = []
tt = []
ans = "Yes"

for i in range(w):
    temp = ""
    for j in range(h):
        tem = s[j]
        temp += tem[i]
    ss.append(temp)
for i in range(w):
    temp = ""
    for j in range(h):
        tem = t[j]
        temp += tem[i]
    tt.append(temp)

for i in range(w):
    if ss[i] not in tt:
        ans = "No"
    else:
        tt.remove(ss[i])
print(ans)