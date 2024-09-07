# Generated by Django 5.1 on 2024-09-07 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0003_restaurant_latitud_restaurant_longitud'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.CharField(choices=[('DULCE', 'DULCE'), ('SALADO', 'SALADO'), ('CALIENTE', 'CALIENTE'), ('FRIO', 'FRIO'), ('BEBIDA', 'BEBIDA')], default='CALIENTE', max_length=8)),
                ('photo', models.ImageField(default='avatar.png', upload_to='dishes/')),
                ('availability', models.CharField(choices=[('Si', 'Si'), ('Agotado', 'Agotado')], default='Si', max_length=7)),
                ('crated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
            options={
                'db_table': 'dishes',
            },
        ),
    ]
