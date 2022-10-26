n, a, b = list(map(int, input().split()))
ans = 0

for i in range(1,n+1):
    temp = 0
    hoge = str(i)
    for j in range(len(hoge)):
        temp += int(hoge[j])
    if temp >=  a and temp <= b:
        ans += i
print(ans)