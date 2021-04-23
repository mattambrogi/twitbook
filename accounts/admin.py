from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Following


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'location', 'is_staff', ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age','location', 'bio')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('age', 'location', 'bio')}),)

#Register models here
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Following)