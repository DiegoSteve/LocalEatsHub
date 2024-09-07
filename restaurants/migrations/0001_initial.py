# Generated by Django 5.1 on 2024-09-07 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('photo', models.ImageField(default='restaurant_avatar.png', upload_to='restaurants/')),
                ('address', models.CharField(max_length=255)),
                ('latitud', models.CharField(blank=True, max_length=50, null=True)),
                ('longitud', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(max_length=13)),
                ('description', models.TextField(blank=True, default='Sin descripción')),
                ('rating', models.FloatField(default=0)),
                ('opening_hours', models.CharField(max_length=100)),
                ('delivery_options', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'restaurants',
            },
        ),
    ]
