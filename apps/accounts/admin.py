from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('phone', 'first_name', 'last_name', 'gender', 'age', 'language', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'gender', 'language')
    search_fields = ('phone', 'first_name', 'last_name')
    ordering = ('phone',)
