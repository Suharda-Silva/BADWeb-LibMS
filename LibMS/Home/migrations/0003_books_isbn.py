# Generated by Django 3.2.8 on 2021-11-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_remove_books_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='ISBN',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
