# Generated by Django 4.0.4 on 2022-05-02 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_seguimiento_alter_producto_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='carritodecompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
    ]