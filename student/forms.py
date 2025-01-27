from django import forms
from django.contrib.auth.models import User
from main import models as QMODEL

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets = {
        'email': forms.EmailInput(),
        'password': forms.PasswordInput()
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model=QMODEL.Student
        fields=['matric_no','middle_name','department', 'level','semester','address','mobile','profile_pic']
