# Generated by Django 4.0.4 on 2022-06-23 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carritohistorico',
            name='codigoorden',
            field=models.IntegerField(null=True),
        ),
    ]