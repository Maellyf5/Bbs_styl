# Generated by Django 2.2 on 2020-10-28 17:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_merge_20201028_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesionales',
            name='valoracion',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
