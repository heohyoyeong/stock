import xml.etree.ElementTree as et


didMakeStockList=False
didMakeDictionary=False
group_list = list()
company_list = list()
csv_maching_dict = dict()

def Get_Stock_list():
    global didMakeStockList  # 전역변수라고 알려줌

    # 해당 파일을 만든 적이 없다면 아래 과정 실시
    if didMakeStockList is False:
        print("csv 파일에서 가져오기")
        with open('board/group-company2.csv','r',encoding='utf-8') as file:

            # 한줄로 데이터 읽어서 넣음 : 문자열(str)
            txtStr = file.read()

            # 줄바꿈을 기준으로 txtStr을 잘라서 lines에 넣음 : 리스트(list)
            lines = txtStr.split("\n")

            # 표의 첫번째 부분 잘라냄
            del lines [0]

            for line in lines:
                row =line.split(',')
                if len (row) == 2 :
                    group_list.append(row[0])
                    company_list.append(row[1])


            # 아래 파일을 만든적이 있다면 과정을 생략하고 리스트를 리턴
            didMakeStockList=True

    return group_list, company_list



# 키가 중복으로 있기 때문에
# 리스트를 생성하여 dict에 추가해주는 것이 key-point

def Get_CSV_Maching_dict():

    glist, clist = Get_Stock_list()
    global didMakeDictionary

    if didMakeDictionary == False:
        print("dictionary 파일에서 가져오기")
        for n in range(len(glist)):

            # 그룹명이 csv_maching_dict의 키에 있으면 회사명을 value로 append해라
            if glist[n] in csv_maching_dict:
                csv_maching_dict[glist[n]].append(clist[n])

            # 그룹명이 csv_maching_dict의 키에 없으면
            # 그룹명을 키로 빈 리스트를 생성해 dict에 추가하고
            # 회사명을 value로 append 해라
            else:
                csv_maching_dict[glist[n] ] =list()
                csv_maching_dict[glist[n]].append(clist[n])
        didMakeDictionary = True

    return csv_maching_dict



didMakeXmlMachingDict=False

corp_code = list()
corp_name = list()
xml_maching_dict = dict()



def Get_XML_maching_dict():

    global didMakeXmlMachingDict

    if didMakeXmlMachingDict is False:
        print('xml 파일에서 가져오기')

        tree = et.parse('stock/CORPCODE.xml')

        root = tree.getroot()


        for child in root.iter('list'):
            c_code = (child.findtext('corp_code'))
            c_name = (child.findtext('corp_name'))

            xml_maching_dict[c_name] = c_code

        didMakeXmlMachingDict = True

    return xml_maching_dict

