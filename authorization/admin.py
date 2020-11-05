from django.contrib import admin
from .models import UserProfile
# Register your models here.

@admin.register(UserProfile)
class AdminProfile(admin.ModelAdmin):
    pass

