# Generated by Django 3.0.5 on 2020-09-10 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_servicio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicio',
            old_name='nombre',
            new_name='nombreServicio',
        ),
    ]
