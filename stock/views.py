from django.shortcuts import render, redirect
from .models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
import xml.etree.ElementTree as ET
import requests
from urllib.parse import quote
import pandas as pd
import re
from bs4 import BeautifulSoup

# 로그인
def s_login(request):
    response_data = {}
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        login_username = request.POST.get('login_username', None)
        login_password = request.POST.get('login_password', None)
        print(login_username)
        print(login_password)

        if not (login_username and login_password):
            response_data['error'] = "아이디와 비밀번호를 모두 입력해주세요 ."
        else:
            myuser = User.objects.get(username=login_username)
            print(myuser)

            if (login_password == myuser.password):
                request.session['userss'] = login_username
                context = {'userss': login_username}
                return render(request, 'detail.html', context)  # 나중에 홈피로 연결시켜야함
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."
            return render(request, 'login.html', response_data)
# 회원가입창
def s_signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re_password']
        user=User.objects.create(username=username,
                                 password=request.POST["password"])
        user.save()

        return render(request, 'signup.html')

# 메인페이지
def s_detail(request):
    return render(request,'detail.html')


# select창을 누르고 검색을 누르면 발동
def search(request):

    def plz(company):
        tree = ET.parse('stock/CORPCODE.xml')
        root = tree.getroot()

        def find_corp_num(find_name):
            for country in root.iter("list"):
                if country.findtext("corp_name") == find_name:
                    return country.findtext("corp_code")

        a = find_corp_num(company)

        def load_data(**kwargs):
            crtfc_key = "973b712049bba8d20fc0d58f93531fab399e61c8"
            corp_code = kwargs['corp_code']

            if kwargs['request'] == 'company':
                url = 'http://opendart.fss.or.kr/api/company.json?crtfc_key={}&corp_code={}'.format(crtfc_key,
                                                                                                    corp_code)

                r = requests.get(url)

                company_data = r.json()

                return company_data

        b = load_data(request='company', corp_code=a)
        corp_name = b['corp_name']


        bb = b['stock_code']
        url = f'http://finance.naver.com/item/sise_day.nhn?code={bb}'

        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        allnum = soup.find_all("td", attrs={"class": "num"})
        now = allnum[0].get_text()
        nows = re.sub('[,]', '', now).strip()
        yester = allnum[6].get_text()
        yesters = re.sub('[,]', '', yester).strip()
        differ = int(nows) - int(yesters)
        perdd= float(int(nows)*100/int(yesters)-100)
        per=round(perdd,2)

        context = {'name': corp_name, 'yesterday': yesters, 'now': nows, 'per': per,
                   'real': differ, "code": bb , 'corp_code':a}

        return context

    if request.method == "POST":
        selected_option = request.POST.get('my_options')
        if selected_option=='gs':
            a1 = plz("GS")
            a2 = plz("GS건설")
            a3 = plz("GS리테일")
            a4 = plz("GS글로벌")
            a5 = plz("GS홈쇼핑")
            a6 = plz("자이에스앤디")
            a7 = plz("삼양통상")
            total=[a1,a2,a3,a4,a5,a6,a7]
            context={'posts':total}
        elif selected_option == 'lg':
            a1 = plz("LG전자")
            a2 = plz("LG화학")
            a3 = plz("LG디스플레이")
            a4 = plz("LG유플러스")
            a5 = plz("LG상사")
            a6 = plz("LG이노텍")
            a7 = plz("LG생활건강")
            a8 = plz("LG")
            a9 = plz("LG하우시스")
            a10 = plz("LG헬로비전")
            a11 = plz("실리콘웍스")
            a12 = plz("지투알")
            a13 = plz("로보스타")
            total = [a1, a2, a3, a4, a5, a6, a7,a8,a9,a10,a11,a12,a13]
            context = {'posts': total}
        elif selected_option == 'sk':
            a2 = plz("SK이노베이션")
            a3 = plz("SK하이닉스")
            a4 = plz("SK텔레콤")
            a5 = plz("SK네트웍스")
            a6 = plz("SK디스커버리")
            a7 = plz("SK가스")
            a8 = plz("SKC")
            a9 = plz("SK케미칼")
            a10 = plz("부산도시가스")
            a11 = plz("SK머티리얼즈")
            a12 = plz("SK렌터카")
            a13 = plz("SK디앤디")
            a14 = plz("드림어스컴퍼니")
            a15 = plz("SKC 솔믹스")
            a16 = plz("에스엠코어")
            a17 = plz("에스케이바이오팜")
            a18 = plz("SK바이오랜드")
            a19 = plz("인크로스")
            a20 = plz("나노엔텍")
            total = [a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20]
            context = {'posts': total}
        elif selected_option == 'life':
            a1 = plz("교보증권")
            total = [a1]
            context = {'posts': total}
        elif selected_option == 'asiana':
            a1 = plz("아시아나항공")
            a2 = plz("금호산업")
            a3 = plz("에어부산")
            a4 = plz("아시아나IDT")
            total = [a1, a2, a3, a4]
            context = {'posts': total}
        elif selected_option == 'nog':
            a1 = plz("NH투자증권")
            a2 = plz("남해화학")
            a3 = plz("농우바이오")
            total = [a1, a2, a3]
            context = {'posts': total}
        elif selected_option == 'daerim':
            a1 = plz("대림산업")
            a2 = plz("대림건설")
            a3 = plz("대림씨엔에스")
            total = [a1, a2, a3]
            context = {'posts': total}
        elif selected_option == 'dacons':
            a1 = plz("대우건설")
            total = [a1]
            context = {'posts': total}
        elif selected_option == 'daocean':
            a1 = plz("대우조선해양")
            total = [a1]
            context = {'posts': total}
        elif selected_option == 'du':
            a1 = plz("두산")
            a2 = plz("두산중공업")
            a3 = plz("두산인프라코어")
            a4 = plz("두산밥캣")
            a5 = plz("두산퓨얼셀")
            a6 = plz("오리콤")
            a7 = plz("두산솔루스")
            total = [a1, a2, a3, a4, a5, a6, a7]
            context = {'posts': total}
        elif selected_option == 'lott':
            a1 = plz("롯데쇼핑")
            a2 = plz("롯데케미칼")
            a3 = plz("롯데지주")
            a4 = plz("롯데하이마트")
            a5 = plz("롯데칠성음료")
            a6 = plz("롯데제과")
            a7 = plz("롯데푸드")
            a8 = plz("롯데정밀화학")
            a9 = plz("롯데정보통신")
            a10 = plz("롯데리츠")
            total = [a1, a2, a3, a4, a5, a6, a7,a8,a9,a10]
            context = {'posts': total}
        elif selected_option == 'esse':
            a1 = plz("미래에셋대우")
            a2 = plz("미래에셋생명")
            a3 = plz("미래에셋벤처투자")
            total = [a1, a2, a3]
            context = {'posts': total}
        elif selected_option == 'sam':
            a1 = plz("삼성전자")
            a2 = plz("삼성생명")
            a3 = plz("삼성물산") #이상한거 수정
            a4 = plz("삼성화재해상보험")
            a5 = plz("삼성SDI")
            a6 = plz("삼성에스디에스")
            a7 = plz("삼성전기")
            a8 = plz("삼성중공업")
            a9 = plz("삼성증권")
            a10 = plz("삼성엔지니어링")
            a11 = plz("호텔신라")
            a12 = plz("제일기획")
            a13 = plz("삼성카드")
            a14 = plz("에스원")
            a15 = plz("삼성바이오로직스")
            a16 = plz("멀티캠퍼스")
            total = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10,a11,a12,a13,a14,a15,a16]
            context = {'posts': total}
        elif selected_option == 'neww':
            a1 = plz("이마트")
            a2 = plz("신세계")
            a3 = plz("신세계인터내셔날")
            a4 = plz("신세계푸드")
            a5 = plz("신세계건설")
            a6 = plz("신세계I&C")
            a7 = plz("광주신세계")
            total = [a1, a2, a3, a4, a5, a6, a7]
            context = {'posts': total}
        elif selected_option == 'cj':
            a1 = plz("CJ")
            a2 = plz("CJ제일제당")
            a3 = plz("CJ대한통운")
            a4 = plz("CJ ENM")
            a5 = plz("CJ프레시웨이")
            a6 = plz("CJ CGV")
            a7 = plz("스튜디오드래곤")
            a8 = plz("CJ씨푸드")
            total = [a1, a2, a3, a4, a5, a6, a7,a8]
            context = {'posts': total}
        elif selected_option == 'soil':
            a1 = plz("S-Oil")
            total = [a1]
            context = {'posts': total}
        elif selected_option == 'ls':
            a1 = plz("LS")
            a2 = plz("E1")
            a3 = plz("엘에스일렉트릭")
            a4 = plz("예스코홀딩스")
            a5 = plz("가온전선")
            a6 = plz("LS전선아시아")
            a7 = plz("LS네트웍스")
            total = [a1, a2, a3, a4, a5, a6, a7]
            context = {'posts': total}
        elif selected_option == 'yong':
            a1 = plz("고려아연")
            a2 = plz("영풍") #수정
            a3 = plz("코리아써키트")
            a4 = plz("인터플렉스")
            a5 = plz("시그네틱스")
            a6 = plz("영풍정밀")
            total = [a1, a2, a3, a4, a5, a6]
            context = {'posts': total}
        elif selected_option == 'occ':
            a1 = plz("OCI")
            a2 = plz("이테크건설")
            a3 = plz("유니드")
            a4 = plz("삼광글라스")
            a5 = plz("유니온머티리얼")
            total = [a1, a2, a3, a4, a5]
            context = {'posts': total}
        elif selected_option == 'kcc':
            a1 = plz("케이씨씨")
            a2 = plz("KCC건설")
            a3 = plz("케이씨씨글라스")
            a4 = plz("코리아오토글라스")
            total = [a1, a2, a3, a4]
            context = {'posts': total}
        elif selected_option == 'kt':
            a1 = plz("케이티") #이거 이상한거 있어서 corp수정해줘얗됨
            a2 = plz("KTcs")
            a3 = plz("케이티스카이라이프")
            a4 = plz("KTis")
            a5 = plz("KTH")
            a6 = plz("이니텍")
            a7 = plz("지니뮤직")
            a8 = plz("나스미디어")
            a9 = plz("KT서브마린")
            a10 = plz("플레이디")
            total = [a1, a2, a3, a4, a5, a6, a7,a8,a9,a10]
            context = {'posts': total}
        elif selected_option == 'ktng':
            a1 = plz("케이티앤지")
            a2 = plz("영진약품")
            total = [a1, a2]
            context = {'posts': total}
        elif selected_option == 'kolon':
            a1 = plz("코오롱")
            a2 = plz("코오롱인더")
            a3 = plz("코오롱글로벌")
            a4 = plz("코오롱플라스틱")
            a5 = plz("코오롱생명과학")
            a6 = plz("코오롱머티리얼")
            total = [a1, a2, a3, a4, a5, a6]
            context = {'posts': total}
        elif selected_option == 'posco':
            a1 = plz("포스코")
            a2 = plz("포스코인터내셔널")
            a3 = plz("포스코케미칼")
            a4 = plz("포스코 ICT")
            a5 = plz("포스코강판")
            a6 = plz("포스코엠텍")
            total = [a1, a2, a3, a4, a5, a6]
            context = {'posts': total}
        elif selected_option == 'harim':
            a1 = plz("하림지주")
            a2 = plz("팬오션")
            a3 = plz("팜스코")
            a4 = plz("선진")  #이상한거 있음
            a5 = plz("하림")
            a6 = plz("엔에스쇼핑")
            total = [a1, a2, a3, a4, a5, a6]
            context = {'posts': total}
        elif selected_option == 'invest':
            a1 = plz("한국금융지주")
            total = [a1]
            context = {'posts': total}
        elif selected_option == 'hanjin':
            a1 = plz("대한항공")
            a2 = plz("한진") #이상한거있ㅇ므
            a3 = plz("한진칼")
            a4 = plz("진에어")
            a5 = plz("한국공항")
            total = [a1, a2, a3, a4, a5]
            context = {'posts': total}
        elif selected_option == 'hanha':
            a1 = plz("한화")
            a2 = plz("한화생명")
            a3 = plz("한화솔루션")
            a4 = plz("한화손해보험")
            a5 = plz("한화에어로스페이스")
            a6 = plz("한화투자증권") #이상한거있음
            a7 = plz("한화시스템")
            total = [a1, a2, a3, a4, a5, a6, a7]
            context = {'posts': total}
        elif selected_option == 'hydep':
            a1 = plz("현대그린푸드")
            a2 = plz("현대홈쇼핑")
            a3 = plz("현대백화점")
            a4 = plz("한섬")
            a5 = plz("현대리바트") #이상한거있음
            a6 = plz("현대에이치씨엔")
            a7 = plz("에버다임")
            total = [a1, a2, a3, a4, a5, a6, a7]
            context = {'posts': total}
        elif selected_option == 'hycar':
            a1 = plz("현대자동차")
            a2 = plz("기아자동차")
            a3 = plz("현대모비스")
            a4 = plz("현대제철")
            a5 = plz("현대글로비스")
            a6 = plz("현대건설")
            a7 = plz("현대위아")
            a8 = plz("현대로템")
            a9 = plz("현대오토에버")
            a10 = plz("이노션")
            a11 = plz("현대비앤지스틸")
            a12 = plz("현대차증권")
            total = [a1, a2, a3, a4, a5, a6, a7,a8,a9,a10,a11,a12]
            context = {'posts': total}
        elif selected_option == 'hyjung':
            a1 = plz("현대중공업지주")
            a2 = plz("한국조선해양")
            a3 = plz("현대미포조선")
            a4 = plz("현대건설기계")
            a5 = plz("현대일렉트릭")
            a6 = plz("현대에너지솔루션")
            total = [a1, a2, a3, a4, a5, a6]
            context = {'posts': total}
        elif selected_option == 'hyosung':
            a1 = plz("효성티앤씨")
            a2 = plz("효성중공업")
            a3 = plz("효성")
            a4 = plz("효성첨단소재")
            a5 = plz("효성화학")
            a6 = plz("진흥기업") #이상한거있음
            a7 = plz("효성 ITX")
            a8 = plz("신인터텍")
            a9 = plz("갤럭시아에스엠")
            total = [a1, a2, a3, a4, a5, a6, a7,a8,a9]
            context = {'posts': total}
    a = request.session['userss']
    context['userss'] = a
    return render(request,'detail.html',context)


# 예) 현대모비스 클릭시 나오는 곳
def detailpost(request,code_num):
    def load_data(**kwargs):
        crtfc_key = "973b712049bba8d20fc0d58f93531fab399e61c8"
        corp_code = kwargs['corp_code']
        url = 'http://opendart.fss.or.kr/api/company.json?crtfc_key={}&corp_code={}'.format(crtfc_key, corp_code)
        r = requests.get(url)
        company_data = r.json()
        return company_data

    b = load_data(corp_code=code_num)
    corp_name=b['corp_name']
    hm_url = b['hm_url']
    stock_name = b['stock_name']
    stock_code = b['stock_code']
    adres = b['adres']
    est_dt = b['est_dt']
    context = {'name': corp_name, 'hm_url': hm_url, 'stock_name': stock_name, 'stock_code': stock_code, 'adres': adres,
                   'est_dt': est_dt}

    company =corp_name
    client_id = 'peqszqPNOMxLgNl_IfiQ'
    client_secret = 'vUxug7iDck'
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
    url_base = "https://openapi.naver.com/v1/search/news.json?query="
    keyword = quote(company)
    url_middle = "$&start="
    keyword_number = '1'
    url = url_base + keyword + url_middle + keyword_number
    result = requests.get(url, headers=headers).json()  # 결과값을 변수로 지정
    for z in range(0, 5):
        zz = re.sub('[<b></b>&quot;]', '', result['items'][z]['title'])
        gisa_text="news"+str(z+1)
        gisa_url="urls"+str(z+1)
        context[gisa_text]=zz
        context[gisa_url]=result['items'][z]['link']

    bb = b['stock_code']
    url = f'http://finance.naver.com/item/sise_day.nhn?code={bb}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    allnum = soup.find_all("td", attrs={"class": "num"})
    alldate = soup.find_all("span", attrs={"class": "tah p10 gray03"})


    def detail_stock(z):
        date = alldate[z].get_text()
        date_chart = (str(date)).replace(".","-")+"T00:00:00"
        now = allnum[z*6].get_text()
        nows = re.sub('[,]', '', now).strip()
        yester = allnum[z*6+6].get_text()
        yesters = re.sub('[,]', '', yester).strip()
        differ = int(nows) - int(yesters)
        perdd = float(int(nows) * 100 / int(yesters) - 100)
        per=round(perdd,2)
        siga = allnum[z*6+2].get_text()
        goga = allnum[z * 6 + 3].get_text()
        juga = allnum[z * 6 + 4].get_text()
        gurae = allnum[z * 6 + 5].get_text()
        context = {'date': date, "date_chart" : date_chart, 'nows': nows, 'per': per, 'differ': differ,
                   'siga': siga, "goga": goga, 'juga': juga, 'gurae':gurae}
        return context

    a1 = detail_stock(0)
    a2=  detail_stock(1)
    a3 = detail_stock(2)
    a4 = detail_stock(3)
    a5 = detail_stock(4)
    a6 = detail_stock(5)
    a7 = detail_stock(6)
    a8 = detail_stock(7)

    total = [a1, a2, a3, a4, a5, a6, a7, a8]
    context['stock']=total
    a = request.session['userss']
    context['userss'] = a
    return render(request, 'detailpost.html',context)

# 로그아웃
def s_logout(request):
    request.session.clear()
    return redirect('stock:detail')

# 게시판
def s_bbs(request):


    return render(request,'bbs.html')

# 프로필

def s_profile(request):

    return render(request,'profile.html')

def s_bbs_create(request):

    return render(request,'bbs_create.html')

def s_calendar(request):

    return  render(request,'calendar.html')


