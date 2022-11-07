# Generated by Django 4.1.2 on 2022-11-07 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourregistry',
            name='bookingId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tourregs', to='bookings.booking'),
        ),
    ]