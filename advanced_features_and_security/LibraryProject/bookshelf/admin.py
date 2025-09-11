from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year') 
    list_filter = ('publication_year',)                     
    search_fields = ('title', 'author')          

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields to show when listing users in admin
    list_display = ("email", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "date_of_birth")

    # Fields for editing/adding users
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("bio", "date_of_birth", "profile_picture")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # Fields when creating a new user in admin
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "date_of_birth", "is_staff", "is_active"),
        }),
    )

    search_fields = ("email",)
    ordering = ("email",)

# Register it
admin.site.register(CustomUser, CustomUserAdmin)

# Create a new group
