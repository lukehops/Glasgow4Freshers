# Generated by Django 2.2.17 on 2021-04-01 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('G4F_APP', '0002_auto_20210401_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
