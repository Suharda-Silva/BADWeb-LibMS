# Generated by Django 3.2.8 on 2021-11-05 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='ISBN',
        ),
    ]
