from django import forms
from board.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['author','contents']


# class SearchStock(forms.Form):
#     search_stock_data = forms.
# 서치폼 구현하기