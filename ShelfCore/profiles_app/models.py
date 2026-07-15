from django.db import models
from django.conf import settings
# Create your models here.

class CustomerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    
    profile_completed = models.BooleanField(
        default=False
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return self.user.username
    
class EmployeeProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    
    positions = models.CharField(
            max_length=100,
            black=True,
        )
    
    created_at = models.Date1TimeField(
        auto_now_add = True
    )