from django.contrib import admin
from .models import Task, Transaction,  ChildUser, ParentUser, FamilyGroup

# Register your models here.


admin.site.register(Task)
admin.site.register(Transaction)
admin.site.register(FamilyGroup)
admin.site.register(ChildUser)
admin.site.register(ParentUser)
