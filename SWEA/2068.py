t = int(input())
for i in range(1, t+1):
    lists = list(map(int, input().split()))
    lists.sort()
    print(f"#{i}", end=" ")
    print(lists[9])

# t = int(input())
# for i in range(1, t+1):
#     lists = list(map(int, input().split()))
#     mx = max(lists)
#     print(f"#{i} {mx}")
#max 함수 사용해서 할 수도 있다