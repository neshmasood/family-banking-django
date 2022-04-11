from django import forms
from .models import ChildUser
from .models import ParentUser





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
class ParentSignUpForm(forms.Form):
    class Meta():
        model = ParentUser
    class Meta:
        model = ParentUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
                'unique_family_name': forms.TextInput(attrs={'unique-family-name':'answer'})
                }
# Child SignUp Form
class ChildSignUpForm(forms.Form):
    # class Meta():
    #     model = ChildUser
    email = forms.EmailField(max_length=250)
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    family_key = forms.CharField(max_length=100)
    class Meta:
        model = ChildUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' 'family_key')
        # widgets = {
        #         'unique_family_name': forms.TextInput(attrs={'unique-family-name':'answer'})
        #         }
