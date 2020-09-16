from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)
    copy_count =  models.SmallIntegerField(default=1)

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    price = models.FloatField()
    copy_count =  models.SmallIntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)



