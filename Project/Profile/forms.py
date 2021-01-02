from django import forms
from .models import Profile


class editProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('fName', 'lName', 'eMail', 'about', 'avatar',)
        labels = {
            'fName': 'First Name',
            'lName': 'Last Name',
            'avatar': 'Profile picture',
            'eMail': 'E-mail',
        }
