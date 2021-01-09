from django import forms
from .models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'description', 'avatar')
        labels = {
            'name': 'Group Name',
            'avatar': 'Group picture',
            'description': 'Description'
        }
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'style': 'resize:none;', }),

        }
