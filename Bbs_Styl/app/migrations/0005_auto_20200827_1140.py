# Generated by Django 2.2.10 on 2020-08-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200826_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inicio',
            old_name='dscrServicio',
            new_name='textServicio',
        ),
        migrations.AddField(
            model_name='inicio',
            name='proInicio',
            field=models.ImageField(default=1, upload_to='static/img'),
            preserve_default=False,
        ),
    ]
