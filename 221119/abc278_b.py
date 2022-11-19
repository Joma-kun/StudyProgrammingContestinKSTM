#WA
#コーナーケース一生分からなかった
h, m = map(int, input().split())

if h < 20:
    if h%10 <= 5:
        print(h, m)
    else:
        h += 1
        m = 0
        print(h, m)
else:
    if m <= 39:
        print(h, m)
    else:
        if h != 23:
            h += 1
        else:
            h = 0
        m = 0
        print(h, m)