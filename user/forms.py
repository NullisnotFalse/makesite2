from django import forms
from .models import UserModel,CreateUserModel
from django.forms.widgets import PasswordInput
class CreateUserForm(forms.ModelForm):
    class Meta:
        model = CreateUserModel
        fields = ['username','email','password_check1','password_check2']
        labels = {'username':"아이디",'email':"email",'password_check1':"패스워드",'password_check2':"동일한 패스워드"}
        widgets = {"password_check1": PasswordInput(), "password_check2": PasswordInput()}
        help_texts = {'username': None}
class LogInForm(forms.ModelForm):
    class Meta:
        model =UserModel
        fields = ['username','password','email']