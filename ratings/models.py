from django.db import models
from dishes.models import Dish
from students.models import Student


# Create your models here.
class Rating(models.Model):
    CHOICES_RATING = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )

    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="ratings")
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="students"
    )
    raiting = models.CharField(max_length=1, choices=CHOICES_RATING, default="5")
    review_text = models.TextField(blank=True, default="Sin descripciones")
