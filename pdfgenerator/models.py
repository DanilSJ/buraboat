from django.db import models
from calculation.models import Excursions,Checkboxes,Inputs

# Create your models here.
#
# class Checkbox(models.Model):
#     id2= models.IntegerField(default=1)
#     name= models.CharField(verbose_name='имя', max_length=255)
#     on= models.BooleanField()
#
# class Input(models.Model):
#     id2= models.IntegerField(default=1)
#     name= models.CharField(verbose_name='имя', max_length=255)
#     value= models.CharField(verbose_name='значение', max_length=255)
#
#
# class Excursion(models.Model):
#     name= models.CharField(verbose_name='имя', max_length=255)


class FastBooking(models.Model):
    book_id = models.IntegerField(default=1)
    name= models.CharField(verbose_name='имя', max_length=255)
    phone= models.CharField(verbose_name='телефон', max_length=25)
    description=models.CharField(verbose_name='wishes', max_length=255)
    excursion_id  = models.ForeignKey(Excursions, on_delete=models.CASCADE)
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    inputs= models.ManyToManyField(Inputs)
    checkboxes= models.ManyToManyField(Checkboxes)
    price = models.IntegerField(default=1)
    text = models.CharField(verbose_name='booking result', default='Thanks for booking', max_length=25)
    qr_code_url = models.CharField(verbose_name='qr code url', default='https://qrcg-media.s3.eu-central-1.amazonaws.com/wp-content/uploads/2020/02/03165309/07-blog-qr-code-information-1024x365.png', max_length=25)
    qr_code_text = models.CharField(verbose_name=' qr code text', default='your QR - dont lose it', max_length=25)
    link_download_ticket = models.CharField(verbose_name='ticket', default='https://149471370.v2.pressablecdn.com/wp-content/uploads/2019/02/TICKET-2-Success-FULL-MIX-6-20-12-mp3-image.jpg', max_length=25)
