# Generated by Django 3.0.2 on 2020-04-12 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_doctors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors',
            name='available_time2',
        ),
        migrations.AlterField(
            model_name='doctors',
            name='available_time1',
            field=models.CharField(max_length=50),
        ),
    ]
