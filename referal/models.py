from django.db import models

class ForgotPass(models.Model):
    email = models.CharField(verbose_name='Почта', max_length=255)
    code = models.IntegerField(verbose_name='Код')
