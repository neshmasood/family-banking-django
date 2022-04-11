from django.contrib import admin
from .models import Task, Transaction,  ChildUser, ParentUser

# Register your models here.




admin.site.register(Task)
admin.site.register(Transaction)

admin.site.register(ChildUser)
admin.site.register(ParentUser)
