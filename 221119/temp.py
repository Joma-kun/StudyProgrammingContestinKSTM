for i in range(5, 10):
    for j in range(60):
        h = i
        m = j
        if h < 20:
            if h%10 < 6:
                print(h)
                print(m)
                print("-----")
            else:
                h += 1
                m = 0
                print(h)
                print(m)
                print("-----")
        else:
            if m < 40:
                print(h)
                print(m)
                print("-----")
            else:
                if h != 23:
                    h += 1
                else:
                    h = 0
                m = 0
                print(h)
                print(m)
                print("-----")