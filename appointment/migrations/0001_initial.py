# Generated by Django 3.0.2 on 2020-04-10 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact_no', models.IntegerField()),
                ('type1', models.CharField(choices=[('general', 'general'), ('specialist', 'specialist')], default='general', max_length=50)),
                ('specialist', models.CharField(blank=True, max_length=50)),
                ('date', models.DateField(help_text='appointment_date')),
            ],
        ),
    ]
