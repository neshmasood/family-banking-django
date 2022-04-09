from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin
from django.utils import timezone   


# Create your models here.





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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # familygroups = models.ManyToManyField(FamilyGroup) # M:M example
   
    

    def __str__(self):
        return self.name
        

    class Meta: 
        ordering = ['name']



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

class User(AbstractUser):
    is_child = models.BooleanField('child status', default=False)
    is_parent = models.BooleanField('parent status', default=False)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    tasks = models.ManyToManyField(Task)
    transactions = models.ManyToManyField(Transaction)



class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_child = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']
    def __str__(self):
        return self.user_name





