from django.contrib import admin
from .models import Task, Transaction, FamilyGroup

# Register your models here.




admin.site.register(Task)
admin.site.register(Transaction)
admin.site.register(FamilyGroup)