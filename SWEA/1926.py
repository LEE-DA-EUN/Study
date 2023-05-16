t = int(input())
for i in range(1, t+1):
    s = str(i)
    ls = list(s)
    l = ls[len(ls)-1]
    if i//100 == 3 or i//100 == 6 or i//100 == 9:
        print("-", end="")
    elif i//10 == 3 or i//10 == 6 or i//10 == 9:
        if int(l) == 3 or int(l) == 6 or int(l) == 9:
            print("-", end="")
        print("-", end=" ")
    elif int(l) == 3 or int(l) == 6 or int(l) == 9:
        print("-", end=" ")
    else:
        print(i, end=" ")

# 백의자리 3,6,9일 때 ---인 경우 예외처리 추가해야할듯 테스트케이스는 통과함