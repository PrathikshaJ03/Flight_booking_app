# Generated by Django 2.2.12 on 2023-05-23 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_booking', '0005_auto_20230523_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]