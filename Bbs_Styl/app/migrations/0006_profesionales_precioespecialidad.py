# Generated by Django 3.0.5 on 2020-09-28 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200928_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesionales',
            name='precioEspecialidad',
            field=models.ManyToManyField(to='app.Precio'),
        ),
    ]