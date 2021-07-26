from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''Admin View for User'''

    list_display = (
        'id',
        'email',
        'is_staff',
        'is_active'
        )
    list_filter = (
        'is_staff',
        'is_active'
    )
    search_fields = (
        'email',
        )