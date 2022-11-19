n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

temp = 0

for i in range(len(a)):
    temp += abs(a[i] - b[i])

if k-temp >= 0 and (k-temp)%2 == 0:
    print("Yes")
else:
    print("No")