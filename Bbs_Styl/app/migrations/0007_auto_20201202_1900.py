# Generated by Django 2.2 on 2020-12-02 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201202_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesionales',
            name='whatsapp',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profesionales',
            name='telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
