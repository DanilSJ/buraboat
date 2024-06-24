from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # name = models.CharField(verbose_name='Имя', max_length=50)
    # email = models.CharField(verbose_name='Почта', max_length=255)
    phone = models.CharField(verbose_name='Телефон', max_length=255, null=True)
    # password = models.CharField(verbose_name='Пароль', max_length=255)
    balance = models.DecimalField(verbose_name='Баланс', max_digits=20, decimal_places=2, default=0)
    referal_people = models.IntegerField(verbose_name='Число приглашенных пользователей', default=0)

    email_confirmation = models.BooleanField(verbose_name='Подтверждение почты', default=False)
