from django.contrib import admin
from .models import Rate
# Register your models here.
@admin.register(Rate)
class UserAdmin(admin.ModelAdmin):
    pass