from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chef(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=150, unique=True)
    profile_photo = models.ImageField(upload_to="chefs/", default="chefs/avatar.png")
    phone = models.CharField(max_length=20)  # Usar CharField para el número de teléfono
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "chefs"

    def __str__(self): 
        return str(self.name)
