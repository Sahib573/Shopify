from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    Adhaar_id = forms.IntegerField()
    joindate = forms.DateField()
    address = forms.CharField(max_length=100)
    phone = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'Adhaar_id', 'address', 'joindate', 'phone', 'password1', 'password2']
