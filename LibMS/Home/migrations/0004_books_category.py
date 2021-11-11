# Generated by Django 3.2.9 on 2021-11-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_books_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.CharField(choices=[('ad', 'Adventure'), ('cl', 'Classic'), ('com', 'Comic'), ('edu', 'Education'), ('dit', 'Detective'), ('fan', 'Fantacy'), ('hor', 'Horrer'), ('his', 'Historical'), ('sh', 'Short Stories'), ('kid', 'Kids'), ('cb', 'Cook Books'), ('nov', 'Novels'), ('oth', 'Other')], default='oth', max_length=3),
            preserve_default=False,
        ),
    ]
