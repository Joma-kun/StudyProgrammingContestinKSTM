#WA
from collections import deque

m = int(input())
temp = []
tem = []
for _ in range(m):
    a, b = map(int, input().split())
    tem.append(a)
    tem.append(b)
    if a not in temp:
        temp.append(a)
    if b not in temp:
        temp.append(b)
    
n = len(temp)
graph = [[] for _ in range(10**9)]

for i in range(len(tem)//2):
    aa = tem[2*i]
    bb = tem[2*i+1]
    graph[aa].append(bb)
    graph[bb].append(aa)
    print(graph)

print(temp)
print(graph)