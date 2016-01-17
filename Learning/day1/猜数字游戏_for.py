Luck_Num = 7
for i in range(3):
    Number = int(input("Please your Number:"))
    if Number > Luck_Num :
        print ("你的数字大了！")
    elif Number < Luck_Num:
        print ("你的数字小了！")
    else:
        print ("Bingo")
        break
else:
    print ("你输入错误的次数超过三次了！！")
