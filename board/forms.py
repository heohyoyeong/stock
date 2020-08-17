from django import forms
from board.models import Post,Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author','title','contents']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text']






# class SearchStock(forms.Form):
#     search_stock_data = forms.
# 서치폼 구현하기