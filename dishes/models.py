from django.db import models
from chefs.models import Chef


# Create your models here.
class Dish(models.Model):
    CATEGORY = (
        ("DULCE", "DULCE"),
        ("SALADO", "SALADO"),
        ("CALIENTE", "CALIENTE"),
        ("FRIO", "FRIO"),
        ("BEBIDA", "BEBIDA"),
    )
    DISH_AVAILABILITY = (
        ("Si", "Si"),
        ("Agotado", "Agotado"),
    )
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=8, choices=CATEGORY, default="CALIENTE")
    photo = models.ImageField(upload_to="dishes/", default="avatar.png")
    availability = models.CharField(
        max_length=7, choices=DISH_AVAILABILITY, default="Si"
    )
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "dishes"

    def __str__(self):
        return str(self.name)
