from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from restaurants.models import Restaurant
from students.models import Student


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        if instance.is_student:
            Student.objects.create(
                user=instance,
                name="Escribe tu nombre",
                phone="0",
                address="Escriba su domicilio",
            )
        elif instance.is_restaurant:
            Restaurant.objects.create(
                user=instance,
                name="Actualice el nombre del restaurant",
                address="Sin informatición",
                phone="0",
            )


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_student:
        instance.students.save()
    elif instance.is_restaurant:
        instance.restaurants.save()
