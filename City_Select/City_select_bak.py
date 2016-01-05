import CityList
Num=['0','1','2','3']
SelectSuccess=True
while SelectSuccess:
    City_List=list(CityList.info.keys())
    Print_City = ''
    Key = enumerate(CityList.info.keys())
    for i,val in Key:
      i = str(i)
      Print_City += i + '\t' + val + '  |  '
    print ('\033[36;1m欢迎登陆查询系统，请根据提示进行查询\033[0m')
    print ('\033[36;1m%s\033[0m'%(Print_City))
    City=input('\033[36;1m请输入序列号选择你要查询的城市，Q退出:\033[0m').strip()
    if City == "Q":
        SelectSuccess=False
        break
    if len(City) != 0 and int(City) < len(City_List):
        Area_List = list(CityList.info[City_List[int(City)]])
        Print_Area = ''
        Key = enumerate(CityList.info[City_List[int(City)]].keys())
        for i,val in Key:
            i = str(i)
            Print_Area +=i + '\t' + val + ' | '
        while SelectSuccess:
            User_Input=input  ('''\033[36;1m
    ===============================================================================================
                                           欢迎来到 %s:
                                         %s区域分布如下：
     %s
    ===============================================================================================
    请输入您选择的城市编号，按Q退出,B返回上一级:\033[0m
    '''%(City_List[int(City)],City_List[int(City)],Print_Area)).strip()
            if User_Input == 'B':
                break
            if User_Input == 'Q':
                SelectSuccess=False
                break
            if len(User_Input) != 0 and int(User_Input) < len(Area_List):
                if int(User_Input) <= len(Area_List):
                    print ('\033[36;1m')
                    print (CityList.info[City_List[int(City)]][Area_List[int(User_Input)]])
                    print ('\033[0m')
                    Exit=input('\033[36;1m查询结束，Q退出，任意键继续查询\033[0m')
                    if Exit == 'Q':
                        SelectSuccess=False
                        break
                else:
                    print ('\033[1;31;40m请输入正确的序列号\033[')
            else:
                print ('\033[1;31;40m请输入正确的序列号\033[0m')
    else:
        print ('\033[1;31;40m请输入正确的序列号\033[0m')
if SelectSuccess==False:
       print ('\033[36;1m谢谢使用，再见！\033[0m')



