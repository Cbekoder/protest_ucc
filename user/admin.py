from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name', 'email', 'birthday', 'city', 'gender', 'image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'birthday', 'city', 'gender', 'image', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    list_display = ('phone', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('phone', 'username', 'email', 'first_name', 'last_name')
    ordering = ('phone',)

admin.site.register(User, UserAdmin)
