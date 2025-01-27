from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from main.models import Invigilator

class InvigilatorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'email': forms.EmailInput(),
        }


class InvigilatorForm(forms.ModelForm):
    class Meta:
        model = Invigilator
        fields = ['address','middle_name', 'mobile', 'profile_pic']

