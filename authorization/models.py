from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField()

    RU = "Россия"
    USA = "Америка"
    COUNTRY = [(RU, 'Россия'), (USA, 'Америка')]

    country = models.CharField(max_length=100, choices=COUNTRY, verbose_name="Страна проживания")
    registration_data = models.DateField(auto_now=True, verbose_name='Дата регистрации')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Юзер', related_name='profile')
