# Generated by Django 4.1.2 on 2022-11-07 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_tourregistry_bookingid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourregistry',
            name='bookingId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tours', to='bookings.booking'),
        ),
        migrations.AlterField(
            model_name='tourregistry',
            name='tourId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tourdata', to='bookings.tour'),
        ),
    ]
