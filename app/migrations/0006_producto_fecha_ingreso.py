# Generated by Django 4.0.4 on 2022-05-03 15:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='fecha_ingreso',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
