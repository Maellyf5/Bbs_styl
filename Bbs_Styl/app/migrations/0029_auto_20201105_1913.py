# Generated by Django 2.2.10 on 2020-11-05 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20201105_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesionales',
            name='valoraciones',
            field=models.ManyToManyField(to='app.Puntuacion'),
        ),
    ]
