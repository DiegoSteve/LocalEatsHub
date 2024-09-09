from django.db import models
from users.models import User


# Create your models here.
class Restaurant(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="restaurants"
    )
    name = models.CharField(max_length=200, unique=True)
    photo = models.ImageField(upload_to="restaurants/", default="restaurant_avatar.png")
    address = models.CharField(max_length=255)
    latitud = models.CharField(max_length=50, blank=True, null=True)
    longitud = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=13)
    description = models.TextField(blank=True, default="Sin descripción")
    rating = models.FloatField(default=0)
    opening_hours = models.CharField(
        max_length=100, default="Horario corrido: de 9:00am a 5:00pm, de lunes a sábado"
    )
    delivery_options = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "restaurants"
