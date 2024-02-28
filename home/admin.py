from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin

from .models import *


@admin.register(Config)
class ConfigAdmin(ModelAdmin):
    list_display = ('address', 'phone', 'email')


@admin.register(Remark)
class RemarkAdmin(ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'description')


admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin, ModelAdmin):
    pass
