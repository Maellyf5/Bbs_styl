# Generated by Django 3.0.5 on 2020-09-08 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_myrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='peluqueros',
            name='imagen',
            field=models.ImageField(default=1, upload_to='static/img'),
            preserve_default=False,
        ),
    ]
