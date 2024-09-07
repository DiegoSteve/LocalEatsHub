# Generated by Django 5.1 on 2024-09-07 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
            options={
                'db_table': 'dishes',
            },
        ),
    ]
