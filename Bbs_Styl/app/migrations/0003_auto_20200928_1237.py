# Generated by Django 3.0.5 on 2020-09-28 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200928_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='precio',
        ),
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField(null=True)),
                ('nombreEspecialidad', models.CharField(max_length=80, null=True)),
                ('servicio', models.ForeignKey(max_length=80, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='especialidad', to='app.Servicio')),
            ],
        ),
    ]