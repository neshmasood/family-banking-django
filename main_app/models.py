from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone   


# Create your models here.

class CustomAccountManager(BaseUserManager):
    use_in_migrations = True
    def create_superuser(self, email, user_name, first_name, password):
        return self.create_user(email, user_name, first_name, password)
    def create_user(self, email, user_name, first_name, password):
        if not email:
            raise ValueError(('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractUser, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    is_child = models.BooleanField('child_status',default=False)
    is_parent = models.BooleanField('parent_status', default=False)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']
    def __str__(self):
        return self.user_name

# class Child(models.Model):
#      user = models.OneToOneField('AUTH_USER_MODEL', on_delete=models.CASCADE, primary_key=True)
     

# class Parent(models.Model):
#      user = models.OneToOneField('AUTH_USER_MODEL', on_delete=models.CASCADE, primary_key=True)
     
    



# class FamilyGroup(models.Model):
#     name = models.CharField(max_length=50),
#     description = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name


STATUS_CHOICES = {
    ("Not yet started", "not yet started"), 
    ("Completed", "complete"), 
    ("Incomplete", "incomplete")
}



class Task(models.Model):
    content = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateTimeField()
    description = models.CharField(max_length=200)
    task_status = models.CharField(max_length=20, choices = STATUS_CHOICES)
    task_approval = models.BooleanField()
    # user_parent= models.ForeignKey(Parent, on_delete=models.CASCADE)
    # familygroups = models.ManyToManyField(FamilyGroup) # M:M example
   
    

    def __str__(self):
        return self.content
        

    class Meta: 
        ordering = ['content']



class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    # sending_user = models.ForeignKey(User, related_name='sending_user', on_delete=models.CASCADE)
    # receiving_user = models.ForeignKey(User, related_name='receiving_user', on_delete=models.CASCADE)

    # debit_amount = models.IntegerField()
    # credit_amount = models.IntegerField()
    # account_balance = models.IntegerField()

    def __str__(self):
         return ": $" + str(self.amount)



USER_TYPE_CHOICES = {
    ("chd", "children"), 
    ("pt", "parent")
    
}

# class User(AbstractUser):
#     is_child = models.BooleanField('child status', default=False)
#     is_parent = models.BooleanField('parent status', default=False)
#     user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
#     tasks = models.ManyToManyField(Task)
#     transactions = models.ManyToManyField(Transaction)








