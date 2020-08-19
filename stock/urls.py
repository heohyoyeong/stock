from django.urls import path
from . import views

app_name = 'stock'

urlpatterns = [

    path('login/', views.s_login, name='login'), # 로그인,
    path('signup/', views.s_signup, name='signup'), # 회원가입
    path('detail/', views.s_detail, name='detail'), # 메인페이지
    path('profile/', views.s_profile, name='profile'), # 프로
    path('logout/', views.s_login, name='logout'), # 로그아웃
    path('calendar/',views.s_calendar, name='calendar'), # 캘린더
    path('profile/',views.s_profile, name='profile'),
    # path('bbs/', views.s_bbs, name='bbs'), # 게시판
    # path('bbs_create',views.s_bbs_create, name='bbs_create'), #게시판 글작성

    path('search/', views.search, name='search'), #select 선택시 계열사 뜸
    path('<str:code_num>/detailpost/', views.detailpost, name='detailpost')
]

