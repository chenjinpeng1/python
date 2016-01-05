import CityList
Num=['0','1','2','3']
SelectSuccess=True
while SelectSuccess:
    if SelectSuccess==False:
        break
    City_List=list(CityList.info.keys())
    b = ''
    Key = enumerate(CityList.info.keys())
    for i,val in Key:
        i = str(i)
        b += i + '\t' + val + '  |  '
    print (b)
    # print ('''
    # 北京
    # 上海
    # 广州
    # 深圳
    # ''')
    City = input('请输入序列号选择你要查询的城市，Q退出:').strip()
    if City == "Q":
        SelectSuccess=False
        break
    if City == '0':
        Area_List = list(CityList.info[City_List[0]])
        b = ''
        Key = enumerate(CityList.info[City_List[0]].keys())
        for i,val in Key:
            i = str(i)
            b += i + '\t' + val + '  |  '
        while SelectSuccess:
            A=input  ('''
    ===============================================================================================
                                           欢迎来到 %s:
                                         %s区域分布如下：
     %s
    ===============================================================================================
    请输入您选择的城市编号，按Q退出,B返回上一级:
    '''%(City,City,b))
            if A == 'B':
                break
            if A == 'Q':
                SelectSuccess=False
                break
            if A == "0":
                print (CityList.info['北京'][Area_List[0]])
            if A == "1":
                print (CityList.info['北京'][Area_List[1]])
            if A == "2":
                print (CityList.info['北京'][Area_List[2]])
            if A == "3":
                print (CityList.info['北京'][Area_List[3]])
            if A == "4":
                print (CityList.info['北京'][Area_List[4]])
    # if City == '上海':
    #     List = list(CityList.info['上海'])
    #     b = ''
    #     bj_key = enumerate(CityList.info['上海'].keys())
    #     for i,val in bj_key:
    #         i = str(i)
    #         b += i + '\t' + val + '  |  '
    #     while SelectSuccess:
    #         A=input  ('''
    # ===============================================================================================
    #                                        欢迎来到 %s:
    #                                      %s区域分布如下：
    #  %s
    # ===============================================================================================
    # 请输入您选择的城市编号，按Q退出,B返回上一级:
    # '''%(City,City,b))
    #         if A == 'B':
    #             break
    #         if A == 'Q':
    #             SelectSuccess=False
    #             break
    #         if A == "0":
    #             print (CityList.info['上海'][List[0]])
    #         if A == "1":
    #             print (CityList.info['上海'][List[1]])
    #         if A == "2":
    #             print (CityList.info['上海'][List[2]])
    #         if A == "3":
    #             print (CityList.info['上海'][List[3]])
    #         if A == "4":
    #             print (CityList.info['上海'][List[4]])





