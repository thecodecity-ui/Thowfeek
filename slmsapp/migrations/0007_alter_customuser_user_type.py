# Generated by Django 5.0.7 on 2024-08-08 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slmsapp', '0006_staff_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (2, 'staff')], default=1, max_length=50),
        ),
    ]
