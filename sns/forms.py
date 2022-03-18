from socket import fromshare
from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('icon', 'title', 'sound',)
