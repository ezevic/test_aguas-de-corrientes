from atexit import register
from django.contrib import admin

from .models import Palindromo

# Register your models here.


@admin.register(Palindromo)
class AdminPalindromo(admin.ModelAdmin):
    list_display = ('palabra', 'check_palindromo', 'created_at', 'update_at')
