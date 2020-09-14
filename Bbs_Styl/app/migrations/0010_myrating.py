# Generated by Django 2.2.10 on 2020-09-07 12:00

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('app', '0009_auto_20200902_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('total', models.PositiveIntegerField(default=0)),
                ('average', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=6)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('Peluqueros', models.TextField()),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'unique_together': {('content_type', 'object_id')},
            },
        ),
    ]