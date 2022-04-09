from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import NewUser





class NewUserCreationForm(UserCreationForm):

    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'first_name', 'is_child', 'is_parent')


#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=50)
#     email = forms.EmailField()

# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=50)
#     email = forms.EmailField()



    