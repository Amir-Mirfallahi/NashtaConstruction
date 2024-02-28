from django import forms
from tinymce.widgets import TinyMCE

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {'content': TinyMCE(attrs={'cols': 80, 'rows': 30})}
        fields = "__all__"
