# Generated by Django 3.0.5 on 2020-10-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_especialidades'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoPostal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(null=True)),
            ],
        ),
    ]
