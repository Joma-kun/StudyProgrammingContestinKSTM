#WA
import itertools
from math import factorial

n, k, d = map(int, input().split())
a = list(map(int, input().split()))
s = set()
b = []

for i in range(100):
    b.append(i)
print(b)
for i in itertools.combinations(b, 50):
    temp = sum(i)
    s.add(temp)
print(s)

print(factorial(100) // (factorial(100-50) * factorial(50)))