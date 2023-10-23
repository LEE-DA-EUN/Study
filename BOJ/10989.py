# n = int(input())
# ls = []
# for i in range(n):
#     ls.append(int(input()))
# ls.sort()

# for j in range(n):
#     print(ls[j])
# 메모리 초과로 더 효율적인 메모리 관리 방법을 찾아야함

import sys
n = int(sys.stdin.readline())
ls = [0] * 10001

for _ in range(n):
    ls[int(sys.stdin.readline())] += 1

for i in range(10001):
    if ls[i] != 0:
        for _ in range(ls[i]):
            print(i)
