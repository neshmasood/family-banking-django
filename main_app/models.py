from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, user_name, first_name, password=None):
#         if not email:
#             raise ValueError('You must provide an email address')
#         email = self.normalize_email(email)
#         user = self.model(email=email, user_name=user_name, first_name=first_name)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user


# class ChildUser(AbstractBaseUser):
#     email = models.EmailField(max_length=250, unique=True)
#     username = models.CharField(max_length=50, unique=True)
#     first_name = models.CharField( max_length=50, blank=True)
#     last_name = models.CharField(max_length=50, blank=True)
#     family_key = models.CharField(max_length=100)
#     is_child = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     identifier = models.CharField(max_length=40, unique=True)

#     objects = CustomUserManager()
#     USERNAME_FIELD = 'identifier'

#     REQUIRED_FIELDS = ['email', 'username', 'first_name', 'family_key']
#     def __str__(self):
#         return self.first_name


# class ParentUser(AbstractBaseUser):
#     id = models.BigIntegerField(primary_key=True)
#     email = models.EmailField(max_length=250)
#     username = models.CharField(max_length=50, unique=True)
#     # username = models.OneToOneField(ChildUser, on_delete=models.CASCADE, primary_key=True, related_name='Parent')
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     family_key = models.CharField(max_length=100)
#     is_parent = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     identifier = models.CharField(max_length=40, unique=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'identifier'
#     REQUIRED_FIELDS = ['email', 'username', 'first_name']

#     def __str__(self):
#         return self.first_name
    
    # def get_absolute_url(self):
    #     return reverse('parent_detail',kwargs={'pk':self.pk})
    # def get_success_url(self):
    #     return reverse('login/')
    
 

class FamilyGroup(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    family_key = models.CharField(max_length=50)

    def __str__(self):
        return self.name

 

STATUS_CHOICES = {
    ("Not yet started", "not yet started"), 
    ("Completed", "complete"), 
    ("Incomplete", "incomplete")
}


class Task(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateTimeField()
    description = models.CharField(max_length=200)
    task_status = models.CharField(max_length=20, choices = STATUS_CHOICES)
    task_approval = models.BooleanField(null=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    familygroup = models.ForeignKey(FamilyGroup, on_delete=models.CASCADE) 
    # childuser =  models.ManyToManyField(ChildUser) # M:M example
   
    def __str__(self):
        return self.name
        
    class Meta: 
        ordering = ['name']


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    sending_user = models.ForeignKey(User, related_name='sending_user', on_delete=models.CASCADE)
    receiving_user = models.ForeignKey(User, related_name='receiving_user', on_delete=models.CASCADE)

    # debit_amount = models.IntegerField()
    # credit_amount = models.IntegerField()
    # account_balance = models.IntegerField()

    def __str__(self):
         return "$" + str(self.amount)




     









