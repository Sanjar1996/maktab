from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreatForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreatForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'username', 'age', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'field': ('age',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
