# Generated by Django 3.0.5 on 2021-01-25 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20210113_1526'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entradablog',
            options={'ordering': ['fecha']},
        ),
    ]