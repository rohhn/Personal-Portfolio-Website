# Generated by Django 4.1.7 on 2023-05-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0002_panorama'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveldiary',
            name='publish',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Panorama',
        ),
    ]
