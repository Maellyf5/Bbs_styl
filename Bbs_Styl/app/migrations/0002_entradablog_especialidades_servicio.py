# Generated by Django 2.2.10 on 2020-11-06 17:06

from django.db import migrations, models
import django.db.models.deletion


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
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreServicio', models.CharField(max_length=80, null=True)),
                ('imagen', models.ImageField(upload_to='static/img')),
            ],
        ),
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEspecialidad', models.CharField(max_length=80, null=True)),
                ('servicio', models.ForeignKey(max_length=80, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='especialidad', to='app.Servicio')),
            ],
        ),
    ]