import CityList
SelectSuccess=True
City_List=list(CityList.info.keys())      #获取省份列表
while SelectSuccess:
    Print_City = ''
    for i,val in enumerate(City_List):  #通过enumerate将省份按照阿序号排列，通过for循环取值
      i = str(i)
      Print_City += i + '\t' + val + '  |  '
    print ('\033[36;1m欢迎登陆查询系统，请根据提示进行查询\033[0m')
    print ('\033[36;1m%s\033[0m'%(Print_City))
    City=input('\033[36;1m请输入序列号选择你要查询的城市，Q退出:\033[0m').strip()
    if City == 'Q':
        SelectSuccess=False
        break
    if City.isdigit() is False:                                #判断用户输入的是不是数字 不是继续输入
        print ('\033[1;31;40m请输入正确的指令\033[0m')
        continue
    if len(City) != 0 and int(City) < len(City_List):         #判断用户输入是不是为空（可取消） and 用户输入的数字是否超过省份列表的索引值
        Print_Area = ''
        Area_List = list(CityList.info[City_List[int(City)]])   #将用户选择的省份取出其区域的keys转换为列表
        for i,val in enumerate(Area_List):  #取出用户输入的省份的keys添加序列号 for循环取出
            i = str(i)
            Print_Area += i + '\t' + val + ' | '
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
            if User_Input.isdigit() is False:
                print ('\033[1;31;40m请输入正确的指令\033[0m')
                continue
            if len(User_Input) != 0 and int(User_Input) < len(Area_List):  #判断用户输入是不是为空（可取消） and 用户输入的数字是否超过区域列表的索引值
                if int(User_Input) <= len(Area_List):
                    print ('\033[36;1m')
                    print (CityList.info[City_List[int(City)]][Area_List[int(User_Input)]])  #打印用户选择的区域的信息
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