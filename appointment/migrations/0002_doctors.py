# Generated by Django 3.0.2 on 2020-04-12 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('specialist', models.CharField(max_length=50)),
                ('hospital', models.CharField(max_length=100)),
                ('available_time1', models.TimeField()),
                ('available_time2', models.TimeField()),
            ],
        ),
    ]
