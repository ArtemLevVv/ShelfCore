from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    
    description = models.TextField(
        blank=True
    )
    
    is_active = models.BooleanField(
        default=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(
        max_length=255,
    )
    
    barcode = models.CharField(
        max_length=50,
        unique=True,
    )
    
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products'
    )
    
    description = models.TextField(
        blank=True
    )
    
    age_restricted = models.BooleanField(
        default=False
    )

    class Unit(models.TextChoices):
        PIECE = "PCS", "Piece"
        KILOGRAM = 'KG', "Kilogram"
        LITER = "L", "Liter"
        PACK = "PACK", "Pack"
    
    unit =  models.CharField(
        max_length=10,
        choices=Unit.choices,
        default=Unit.PIECE,
    )    
    
    is_active = models.BooleanField(
        default=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    def __str__(self):
        return self.name