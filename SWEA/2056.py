t = int(input())
for i in range(1, t+1):
    a = str(input())
    y = a[0:4]
    m = a[4:6]
    d = a[6:8]
    if int(m) < 1 or int(m) > 12:
        print(f"#{i} -1")
    else:
        mo = int(m)
        if mo == 1 or mo == 3 or mo == 5 or mo == 7 or mo == 8 or mo == 10 or mo == 12:
            if int(d) <= 31:
                print(f"#{i} {y}/{m}/{d}")
            else:
                print(f"#{i} -1")
        if mo == 2:
            if int(d) <= 28:
                print(f"#{i} {y}/{m}/{d}")
            else:
                print(f"#{i} -1")
        if mo == 4 or mo == 6 or mo == 9 or mo == 11:
            if int(d) <= 30:
                print(f"#{i} {y}/{m}/{d}")
            else:
                print(f"#{i} -1")



# t = int(input())
# for i in range(1, t+1):
#     a = str(input())
#     y = a[0:4]
#     m = a[4:6]
#     d = a[6:8]
#     md = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
#     mo = int(m)
#     if  mo > 0 and mo < 13 and int(d) <= md[mo]:
#         print("#{} {}/{}/{}".format(i,y,m,d))
#     else:
#         print(f"#{i} -1")

# 딕셔너리를 사용하여 간단하게 구현할수도 있다.