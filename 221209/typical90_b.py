n = int(input())

for i in range(2**n):
    k = "0" + str(n) + "b"
    temp = str(format(i, k))
    if temp.count("0") == temp.count("1"):
        for j in range(n):
            f = 0
            tem = temp[:j+1]
            if tem.count("0") < tem.count("1"):
                f = 1
                break
        if f == 0:
            print(temp.replace("0","(").replace("1",")"))