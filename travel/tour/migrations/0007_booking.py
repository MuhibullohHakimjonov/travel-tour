# Generated by Django 5.1.5 on 2025-01-16 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0006_alter_tours_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('user_email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('num_people', models.PositiveIntegerField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='tour.tours')),
            ],
        ),
    ]
