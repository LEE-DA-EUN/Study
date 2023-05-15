t = int(input())
for i in range(1, t+1):
    ls = list(map(int, input().split()))
    a = 0
    for j in range(0, len(ls)):
        if ls[j]>= 0 and ls[j]<= 10000:
            a = a + ls[j]
    av = round(a/len(ls))
    print(f"#{i} {av}")
    
# t = int(input())
# for i in range(1, t+1):
#     ls = list(map(int, input().split()))
#     a = sum(ls)
#     av = round(a/len(ls))
#     print(f"#{i} {av}")
# 숫자 조건 없으면 sum함수 사용해서 풀자!