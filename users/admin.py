from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

#admin.site.register(User, UserAdmin)



@admin.register(User)
class UserAdmin2(admin.ModelAdmin):
    pass
