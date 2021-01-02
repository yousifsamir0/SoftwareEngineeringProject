from django import forms
from .models import Post


class postform(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('body', 'image')
        labels = {
            'body': '',
            'image': '',
        }
        widgets = {
            'body': forms.Textarea(attrs={'cols':80, 'rows': 2,'class':'form-control my-3','style':'resize:none;','placeholder':"what's in your mind . . .",}),
            'image': forms.FileInput,
        }
