def is_in_24_hours(h, m):
    return 0 <= h <= 23 and 0 <= m <= 59
def misjudged(h, m):
    A, B = h // 10, h % 10
    C, D = m // 10, m % 10
    AC = A * 10 + C
    BD = B * 10 + D
    return is_in_24_hours(AC, BD)

for i in range(15, 20):
    for j in range(60):
        h = i
        m = j
        H = i
        M = j
        while not misjudged(H, M):
            M += 1
            if M == 60:
                H, M = H + 1, 0
            if H == 24:
                H = 0
        if h < 20:
            if h%10 < 6:
                if h!= H or m != M:
                    print(h, m, H, M)
            else:
                h += 1
                m = 0
                if h!= H or m != M:
                    print(h, m, H, M)
        else:
            if m < 40:
                if h!= H or m != M:
                    print(h, m, H, M)
            else:
                if h != 23:
                    h += 1
                else:
                    h = 0
                m = 0
                if h!= H or m != M:
                    print(h, m, H, M)
