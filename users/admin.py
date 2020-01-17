"""User admin classes."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from users.models import Profile
from django.contrib.auth.models import User


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile admin."""
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    # Create link in field to go to edit panel
    list_display_links = ('pk', 'user')
    # Enable fields to be editable
    list_editable = ('phone_number', 'website', 'picture')
    # Create search field and find by parameters
    search_fields = ('user__email', 'user__username', 'user__first_name', 'user__last_name', 'phone_number')
    # Create filter in right panel of admin
    list_filter = ('created',
                   'modified',
                   'user__is_active',
                   'user__is_staff')

    # field sets to change data in edit panel
    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
                ('phone_number', 'website'),
            ),
        }),
        ('Extra info', {
            'fields': (
                'biography',
            ),
        }
        ),
        ('Metadata', {
            'fields': ('modified', 'created'),
        }),
    )

    readonly_fields = ('created', 'modified', 'user')


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """ Add profile admin to base user admin"""
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
