# Generated by Django 4.1.2 on 2022-11-07 23:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_alter_tourregistry_bookingid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='departDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
