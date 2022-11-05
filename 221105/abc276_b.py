n, m = map(int, input().split())
t = [[] for i in range(n)]

for i in range(m):
    li = list(map(int, input().split()))
    t[int(li[0]-1)].append(li[1])
    t[int(li[1]-1)].append(li[0])
    
for k in range(n):
    if len(t[k]) != 0:
        temp = sorted(t[k])
        tem = ' '.join(map(str,temp))
        print(str(len(t[k])) + " " + tem)
    else:
        print(0)