from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Event, User, Location

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'name', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'role', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'name')
    ordering = ('email',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_datetime', 'Category', 'Status', 'Submitted_By')
    list_filter = ('Category', 'Status', 'event_datetime')
    search_fields = ('name', 'description')
    raw_id_fields = ('Submitted_By', 'location')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'country')
    list_filter = ('city', 'country')
    search_fields = ('address', 'city', 'country')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Location, LocationAdmin)