# Generated by Django 3.2.7 on 2021-11-12 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_userbook'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userbook',
            options={'verbose_name': 'UserBook', 'verbose_name_plural': 'UserBooks'},
        ),
    ]