# Generated by Django 3.0.5 on 2020-10-16 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_conocenos'),
    ]

    operations = [
        migrations.AddField(
            model_name='conocenos',
            name='conocenos',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]