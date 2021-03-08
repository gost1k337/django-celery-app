from django.contrib import admin

from .forms import LoginForm, RegisterForm
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'verified')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    list_display = ('email', 'username', 'created_at')
