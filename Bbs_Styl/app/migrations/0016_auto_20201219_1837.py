# Generated by Django 2.2.10 on 2020-12-19 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20201219_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesionales',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]