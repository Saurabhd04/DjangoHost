from django.contrib import admin
from .models import Register

# Register your models here.
admin.site.register(Register)


# from django.contrib import admin

# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import Register

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = Register
#     list_display = ['email', 'username']

# admin.site.register(Register, CustomUserAdmin)