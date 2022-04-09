from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.

class FamilyGroup(models.Model):
    name = models.CharField(max_length=50),
    description = models.CharField(max_length=200)

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
    task_approval = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    familygroups = models.ManyToManyField(FamilyGroup) # M:M example
   
    

    def __str__(self):
        return self.name
        

    class Meta: 
        ordering = ['name']



class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    sending_user = models.ForeignKey(User, related_name='sending_user', on_delete=models.CASCADE)
    receiving_user = models.ForeignKey(User, related_name='receiving_user', on_delete=models.CASCADE)

    def __str__(self):
         return ": $" + str(self.amount)
