n, t = map(int, input().split())
a = list(map(int, input().split()))
num = 0
sec = 0

s = sum(a)
k = t // s
t -= s*k

while True:
    num %= n
    if sec < t:
        sec += a[num]
        num += 1
    else:
        num -= 1
        num %= n
        sec -= a[num]
        temp = t - sec
        print(num+1, temp)
        exit()