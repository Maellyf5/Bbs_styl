# Generated by Django 2.2.11 on 2020-09-22 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20200921_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codigopostal',
            name='profesionalCP',
        ),
        migrations.RemoveField(
            model_name='codigopostal',
            name='servicioCP',
        ),
        migrations.AlterField(
            model_name='codigopostal',
            name='codigo',
            field=models.IntegerField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
