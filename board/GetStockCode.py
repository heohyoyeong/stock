import xml.etree.ElementTree as et


didMakeStockList=False
didMakeDictionary=False
group_list = list()
company_list = list()
csv_maching_dict = dict()

def Get_Stock_list():
    global didMakeStockList  # 전역변수라고 알려줌

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



            didMakeStockList=True

    return group_list, company_list




def Get_CSV_Maching_dict():

    glist, clist = Get_Stock_list()
    global didMakeDictionary

    if didMakeDictionary == False:
        print("dictionary 파일에서 가져오기")
        for n in range(len(glist)):

            if glist[n] in csv_maching_dict:
                csv_maching_dict[glist[n]].append(clist[n])

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

        tree = et.parse('stock/CORPCODE.xml')

        root = tree.getroot()


        for child in root.iter('list'):
            c_code = (child.findtext('corp_code'))
            c_name = (child.findtext('corp_name'))

            xml_maching_dict[c_name] = c_code

        didMakeXmlMachingDict = True

    return xml_maching_dict

