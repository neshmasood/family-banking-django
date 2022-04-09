from django.contrib import admin
from .models import Task, Transaction
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from .forms import NewUserCreationForm

# Register your models here.



class CustomUserAdmin(UserAdmin):
    model = NewUser
    add_form = NewUserCreationForm

    # fieldsets = (
    #     *UserAdmin.field.sets,
    #     (
    #         'User role',
    #         {
    #             'fields': (
    #                 'is_parent',
    #                 'is_child'
    #             )
    #         }
    #     )
    # )
    # search_fields = ('email', 'user_name', 'first_name',)
    # list_filter = ('email', 'user_name', 'first_name', 'is_parent', 'is_child')
    # ordering = ('start_date',)
    # list_display = ('email', 'user_name', 'first_name', 'is_parent', 'is_child')
    # fieldsets = (
    #     (None, {'fields': ('email', 'user_name', 'first_name',)}),
    #     ('Permissions', {'fields': ('is_child', 'is_parent')}),
    #     ('Personal', {'fields': ('about',)}),
    # )
    # formfield_overrides = {
    #     NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    # }
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_parent', 'is_child')}
    #      ),
    # )

# class CustomUserAdmin(UserAdmin):
#     model = NewUser
#     search_fields = ('email', 'user_name', 'first_name',)
#     list_filter = ('email', 'user_name', 'first_name', 'is_parent', 'is_child')
#     ordering = ('start_date',)
#     list_display = ('email', 'user_name', 'first_name', 'is_parent', 'is_child')
#     fieldsets = (
#         (None, {'fields': ('email', 'user_name', 'first_name',)}),
#         ('Permissions', {'fields': ('is_child', 'is_parent')}),
#         ('Personal', {'fields': ('about',)}),
#     )
#     formfield_overrides = {
#         NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
#     }
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_parent', 'is_child')}
#          ),
#     )


admin.site.register(NewUser, CustomUserAdmin)
admin.site.register(Task)
admin.site.register(Transaction)

