# Generated by Django 3.2.7 on 2021-11-12 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_alter_userbook_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbook',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.books', verbose_name='book'),
        ),
    ]
