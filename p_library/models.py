from django.db import models


# Create your models here.
class Author(models.Model):
    full_name = models.TextField(max_length=100)
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)
    face = models.ImageField(upload_to='face_author/%M/%S', blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.birth_year}"


class PublishingHouse(models.Model):
    full_name = models.CharField(default="Empty", max_length=100)
    count_book = models.IntegerField(null=True)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.CharField(max_length=100)
    description = models.TextField()
    year_release = models.SmallIntegerField()
    price = models.FloatField()
    copy_count = models.SmallIntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, verbose_name="Вербос_нэйм")
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE, verbose_name="Издательство",
                                         null=True, related_name="books", blank=True)

    authors = models.ManyToManyField(
        Author,
        through='Inspiration',
        through_fields=('book', 'author'),
        related_name='authors',
    )

    def __str__(self):
        return self.title


class Friend(models.Model):
    full_name = models.CharField(max_length=99, verbose_name="Имя")
    books = models.ManyToManyField(Book, verbose_name="Взяли в долг")

    def __str__(self):
        return self.full_name


class Inspiration(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    inspirer = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='inspired_works',
    )

    def __str__(self):
        return str(self.inspirer)
