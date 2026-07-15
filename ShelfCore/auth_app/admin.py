from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info",
            {
                "fields":(
                    "phone",
                    "created_at",
                    "updated_at",
                )
            }
        ),
    )
    
    readonly_fields = (
        "created_at",
        "updated_at",
    )