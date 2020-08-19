# forms.py == modelform에 대한 class를 정의해주기 위한 파일

from django import forms
from stock.models import stockname

class stocknameForm(forms.ModelForm): #이렇게 반드시해야한다.
    class Meta:
        model = stockname
        fields = ['stock_money'] #실제 입력할 것이 무엇인가.
