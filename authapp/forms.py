from django import forms
from .models import Register
import django

class SignupForm(forms.ModelForm):
    class Meta:
        model=Register
        widgets={'pwd':forms.PasswordInput(),'cpwd': forms.PasswordInput(),}
        fields=['name', 'mobno', 'email', 'uname', 'pwd', 'cpwd']
class SigninForm(django.forms.Form):
    uname = forms.CharField(max_length=10)
    pwd = forms.CharField(max_length=10)
