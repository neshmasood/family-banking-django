from django import forms
from django.contrib.auth.forms import UserCreationForm
# from .models import ChildUser, ParentUser
# from .models import ParentUser
from django.contrib.auth.models import User


      
# Parent SignUp Form 
class ParentSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=250)
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    family_key = forms.CharField(max_length=100)
   
   
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'family_key')
        # widgets = {
        #         'family_key': forms.TextInput(attrs={'family_key':'answer'})
        #         }


# Child SignUp Form
class ChildSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=250)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    family_key = forms.CharField(max_length=100)
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'family_key')
        # widgets = {
        #         'family_key': forms.TextInput(attrs={'family_key':'answer'})
        #         }
