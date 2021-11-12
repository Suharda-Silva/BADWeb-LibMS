from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

YEAR = [(y,y) for y in range(datetime.date.today().year+1, 1500, -1)]

class Books (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    picture = models.URLField(max_length=255)
    author = models.CharField(max_length=30)
    year = models.IntegerField(choices=YEAR)
    language = models.CharField(max_length=2,choices=[
                                                ('en', 'English'),
                                                ('lk', 'Sinhala'),
                                                ('tm', 'Tamil'),
                                                ('sp', 'Spanish'),
                                                ('gr', 'German'),
                                                ('fr', 'French'),
                                                ('ru', 'Russian'),
                                                ('lt', 'Latin'),
                                                ('ch', 'Chinese'),
                                                ('jp', 'Japanese'),
                                                ('ot', 'Other')
                                                    ])
    ISBN = models.CharField(max_length=15)
    category = models.CharField(max_length=3, choices=[
                                                ('ad', 'Adventure'),
                                                ('cl', 'Classic'),
                                                ('com', 'Comic'),
                                                ('edu', 'Education'),
                                                ('dit', 'Detective'),
                                                ('fan', 'Fantacy'),
                                                ('hor', 'Horrer'),
                                                ('his', 'Historical'),
                                                ('sh', 'Short Stories'),
                                                ('kid', 'Kids'),
                                                ('cb', 'Cook Books'),
                                                ('nov', 'Novels'),
                                                ('oth', 'Other')
                                                    ])
    description = models.TextField()
    pages = models.IntegerField()
    availability = models.IntegerField()
    issued = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        
        
class UserBook (models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, to_field='id', verbose_name="book", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} - {self.id}"

    class Meta:
        verbose_name = "UserBook"
        verbose_name_plural = "UserBooks"