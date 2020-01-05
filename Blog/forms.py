from django import forms
from .models import Comment, Blog
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['blog','pubdate']
class AddPost(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['reporter']