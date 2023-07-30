import sys
n = int(input())
ls = []
for i in range(n):
    ls.append(int(sys.stdin.readline()))
ls.sort()
for j in ls:
    print(j)