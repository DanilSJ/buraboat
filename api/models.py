from django.db import models
from django.core.exceptions import ValidationError
from calculation.models import Excursions
import json

def default_sequence():
    return [
        {
            "block_name": "boats",
            "num": "1"
        },
        {
            "block_name": "text_block",
            "num": "1"
        },
        {
            "block_name": "tips_today",
            "num": "1"
        },
        {
            "block_name": "past_trips",
            "num": "1"
        },
        {
            "block_name": "module/1",
            "num": "1"
        }
    ]

class MainHead(models.Model):
    slogan = models.CharField(max_length=255)
    mini_slogan = models.TextField(null=True, blank=True)
    background = models.ImageField(upload_to='main_head_background', height_field=None, width_field=None, null=True, blank=True)
    boat = models.ImageField(upload_to='main_head_boat', height_field=None, width_field=None, null=True, blank=True)
    excursions = models.ManyToManyField(Excursions, verbose_name='Экскурсии', blank=True)

    class Meta:
        verbose_name = "Main head  Add"
        verbose_name_plural = "Main head  Add"

class MainTextBlock(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='main_textblock', height_field=None, width_field=None, null=True, blank=True)

    class Meta:
        verbose_name = "Main text block  Add"
        verbose_name_plural = "Main text block  Add"

class MainBoats(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='main_boats', height_field=None, width_field=None, null=True, blank=True)
    slider_number = models.IntegerField(null=True, blank=True)
    draft_all = models.BooleanField(default=False)
    draft_mobile = models.BooleanField(default=False)
    url_button = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    class Meta:
        verbose_name = "Main boats Add"
        verbose_name_plural = "Main boats Add"

class MainPastTrips(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='main_past_trips', height_field=None, width_field=None, null=True, blank=True)
    slider_number = models.IntegerField(null=True, blank=True)
    draft_all = models.BooleanField(default=False)
    draft_mobile = models.BooleanField(default=False)
    url_button = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    page = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Main past trips  Add"
        verbose_name_plural = "Main past trips  Add"

class MainTipsToday(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='main_tips_today', height_field=None, width_field=None, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    hours = models.IntegerField(default=3)
    slider_number = models.IntegerField(null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True)
    raiting = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)        


    class Meta:
        verbose_name = "Main tips today  Add"
        verbose_name_plural = "Main tips today  Add"

class MainSequence(models.Model):
    sequence_json = models.JSONField(default=default_sequence)

    class Meta:
        verbose_name = "Main sequence  Add"
        verbose_name_plural = "Main sequence  Add"

class New_Module(models.Model):
    boat = models.ManyToManyField("MainBoats", verbose_name='boat', blank=True)
    text_block = models.ManyToManyField("MainTextBlock", verbose_name='text_block', blank=True)
    past_trips = models.ManyToManyField("MainPastTrips", verbose_name='past_trips', blank=True)
    trips_today = models.ManyToManyField("MainTipsToday", verbose_name='trips_today', blank=True)
    number = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.id:
            return super(New_Module, self).save(*args, **kwargs)

        if self.boat.exists() != self.text_block.exists() != self.past_trips.exists() != self.trips_today.exists():
            raise ValidationError('Не больше одного выбора в  ManyToManyField')


        if not (self.boat.exists() or self.text_block.exists() or self.past_trips.exists() or self.trips_today.exists()):
            raise ValidationError('Необходимо заполнить хотя бы одно поле ManyToManyField.')

        super().save(*args, **kwargs)
