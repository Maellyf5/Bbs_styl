# Generated by Django 3.0.5 on 2020-10-15 16:48

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
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.IntegerField(blank=True, null=True)),
                ('horario', models.CharField(max_length=80, null=True)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('aviso', models.TextField(blank=True, max_length=10000, null=True)),
                ('cookies', models.TextField(blank=True, max_length=10000, null=True)),
            ],
        ),
    ]
