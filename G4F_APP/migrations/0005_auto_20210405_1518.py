# Generated by Django 2.2.17 on 2021-04-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('G4F_APP', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.CharField(max_length=10000),
        ),
    ]