#WA
import math

n = int(input())
p = list(map(int, input().split()))
num = int(0)
temp = 0
ans = ""
z = int("".join(map(str, p)))
q = 0
r = 0
list_a = list(range(1, n+1))

for i in range(n):
    if i == 0:
        temp = 0
    elif p[i-1] < p[i]:
        temp += 1
    if i == n-1:
        num += 1
    else:
        num += (p[i]-1-temp) * math.factorial(n-(i+1))

r = num-2

for j in range(n):
    ans += str(list_a[(r // (math.factorial(n-j-1)))]) + " "
    list_a.pop(r // (math.factorial(n-j-1)))
    r = r % (math.factorial(n-j-1))

print(ans)