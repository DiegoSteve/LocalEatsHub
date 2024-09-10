from django.db import models
from users.models import CustomUser


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="students"
    )
    name = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "students"

    def __str__(self):
        return str(self.name)
