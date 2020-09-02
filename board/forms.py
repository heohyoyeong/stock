from django import forms
from board.models import Post,Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author','title','contents','maching_code']
        widgets ={'author': forms.HiddenInput()}
        exclude =['maching_code']



# class PostForm(forms.Forms):
#     title = forms.CharField(error_messages = {'required':'제목을 입력해주세요'}, )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text']
        widgets ={'author': forms.HiddenInput()}







# class SearchStock(forms.Form):
#     search_stock_data = forms.
# 서치폼 구현하기