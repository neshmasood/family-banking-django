from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ChildUser
# from .models import ParentUser
from django.contrib.auth.models import User





# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=50)
#     email = forms.EmailField()
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )



# # User Signup Form common for both parent and child login
# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'is_parent', 'is_child', 'password1', 'password2' )
      
# Parent SignUp Form 
class ParentSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=250)
    # username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    family_key = forms.CharField(max_length=100)
    # password1 = forms.CharField(max_length=150)
    # password2 = forms.CharField(max_length=150)
   
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'family_key')
        # widgets = {
        #         'unique_family_name': forms.TextInput(attrs={'unique-family-name':'answer'})
        #         }
# Child SignUp Form
class ChildSignUpForm(UserCreationForm):
    # class Meta():
    #     model = ChildUser
    email = forms.EmailField(max_length=250)
    # username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    family_key = forms.CharField(max_length=100)
    # password1 = forms.CharField(max_length=150)
    # password2 = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'family_key')
        # widgets = {
        #         'unique_family_name': forms.TextInput(attrs={'unique-family-name':'answer'})
        #         }
