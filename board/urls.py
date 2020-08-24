"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

app_name='board'

urlpatterns = [
    path('', views.board_main_list, name='bbs_main'),
    path('create', views.board_create, name='bbs_create'),
    path('<int:post_id>/detail', views.board_detail, name='bbs_detail'),
    path('<int:post_id>/detail/send_comment', views.board_send_comment, name='bbs_send_comment'),
    path('<int:post_id>/update', views.board_update, name='bbs_update'),
    path('<int:post_id>/delete', views.board_delete, name='bbs_delete'),


]
