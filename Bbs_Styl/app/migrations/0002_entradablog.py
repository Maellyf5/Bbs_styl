# Generated by Django 2.2.11 on 2020-08-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntradaBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=70)),
                ('descripcion', models.TextField(null=True)),
                ('fecha', models.DateTimeField()),
                ('imagen', models.ImageField(upload_to='static/img')),
                ('destacados', models.BooleanField(default=False)),
            ],
        ),
    ]
