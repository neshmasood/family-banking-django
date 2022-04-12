from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

 

class FamilyGroup(models.Model):
    name = models.CharField(max_length=150)
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
    task_approval = models.BooleanField(null=False)
    users = models.ManyToManyField(User) # M:M example
    familygroup = models.ForeignKey(FamilyGroup, on_delete=models.CASCADE) 
    
   
    def __str__(self):
        return self.name
        
    class Meta: 
        ordering = ['name']


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    sending_user = models.ForeignKey(User, related_name='sending_user', on_delete=models.CASCADE)
    receiving_user = models.ForeignKey(FamilyGroup, related_name='receiving_user', on_delete=models.CASCADE)


    def __str__(self):
         return "$" + str(self.amount)




     









