from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, password=None):
        if not email:
            raise ValueError('You must provide an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

  


# class User(AbstractBaseUser): 
#     email = models.EmailField(max_length=250)
#     # username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='Parent')
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     unique_family_name = models.CharField(max_length=100)
#     is_parent = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_child = models.BooleanField(default=False)
#     objects = CustomUserManager()
#     # REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password1', 'password2' 'is_parent', 'is_child']

#     def __str__(self): 
#         return self.first_name
    
#     def get_absolute_url(self):
#         return reverse('parent_detail',kwargs={'pk':self.pk})


# class Child(AbstractBaseUser):
#     email = models.EmailField('email address', max_length=250, unique=True)
#     user_name = models.CharField(max_length=50, unique=True)
#     first_name = models.CharField(max_length=50, blank=True)
#     last_name = models.CharField(max_length=50, blank=True)
#     unique_family_name = models.CharField(max_length=100)
#     is_child = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

#     REQUIRED_FIELDS = ['user_name', 'first_name']
#     def __str__(self):
#         return self.first_name

class ChildUser(AbstractBaseUser):
    email = models.EmailField(max_length=250, unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField('first_name', max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    family_key = models.CharField(max_length=100)
    is_child = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    identifier = models.CharField(max_length=40, unique=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'first_name'

    REQUIRED_FIELDS = ['email', 'username', 'first_name', 'family_key']
    def __str__(self):
        return self.first_name
# class User(AbstractBaseUser):
#     is_child = models.BooleanField(default=False)
#     is_parent = models.BooleanField(default=False)



class ParentUser(AbstractBaseUser):
    email = models.EmailField(max_length=250)
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='Parent')
    first_name = models.CharField('first_name', max_length=50)
    last_name = models.CharField(max_length=50)
    family_key = models.CharField(max_length=100)
    family_children = models.ManyToManyField(ChildUser, through="ChildrenInFamily")
    is_parent = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    identifier = models.CharField(max_length=40, unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELDS = ['email', 'username', 'first_name', 'family_key']

    def __str__(self):
        return self.first_name
    
    # def get_absolute_url(self):
    #     return reverse('parent_detail',kwargs={'pk':self.pk})
    # def get_success_url(self):
    #     return reverse('login/')


# class Parent(models.Model):
#     email = models.EmailField(max_length=250)
#     username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='Parent')
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     unique_family_name = models.CharField(max_length=100)
#     family_children = models.ManyToManyField(Child, through="ChildrenInFamily")
#     is_parent = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

#     def __str__(self):
#         return self.first_name
    
#     def get_absolute_url(self):
#         return reverse('parent_detail',kwargs={'pk':self.pk})

# class ChildrenInFamily(models.Model):
#     parent = models.ForeignKey(Parent, related_name="family_parent", on_delete=models.CASCADE)
#     child = models.ForeignKey(Child, related_name="user_child_first_name",on_delete=models.CASCADE)

#     def __str__(self):
#         return self.child.first_name

#     class Meta:
#         unique_together = ('parent','child')  

class ChildrenInFamily(models.Model):
    parent = models.ForeignKey(ParentUser, related_name="family_parent", on_delete=models.CASCADE)
    child = models.ForeignKey(ChildUser, related_name="user_child_first_name",on_delete=models.CASCADE)

    def __str__(self):
        return self.parent

    class Meta:
        unique_together = ('parent','child')  



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
    task_approval = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # familygroups = models.ManyToManyField(FamilyGroup) # M:M example
   

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
         return ": $" + str(self.amount)




     









