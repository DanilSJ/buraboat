from django.db import models

class Excursions(models.Model):
    name = models.CharField(max_length=255)
    time = models.TimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    settings = models.ForeignKey('Settings', on_delete=models.CASCADE, null=True, blank=True)
    image_for_tab = models.ImageField(upload_to='main_excursions', height_field=None, width_field=None, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)

    prive_hour = models.IntegerField(null=True, blank=True)
    prive = models.IntegerField(null=True, blank=True)

    prive_hourr = models.BooleanField(null=True, blank=True)
    privee = models.BooleanField(null=True, blank=True)

    class Meta:
        verbose_name = "Main excursions  Add"
        verbose_name_plural = "Main excursions  Add"

class Calc(models.Model):
    excursions = models.ForeignKey('Excursions', on_delete=models.CASCADE)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    inputs = models.ManyToManyField('Inputs', blank=True)
    checkboxes = models.ManyToManyField('Checkboxes', blank=True)

    class Meta:
        verbose_name = "Calculation"
        verbose_name_plural = "Calculation"

class Checkboxes(models.Model):
    title = models.CharField(max_length=255)
    default_value = models.BooleanField(null=True, blank=True)
    hint  = models.CharField(max_length=255, null=True, blank=True)
    super_hint  = models.TextField(null=True, blank=True)
    hour_coefficient = models.FloatField(null=True, blank=True)
    trip_coefficient = models.FloatField(null=True, blank=True)


    class Meta:
        verbose_name = "Checkboxes"
        verbose_name_plural = "Checkboxes"

class Inputs(models.Model):
    title = models.CharField(max_length=255)
    default_value = models.CharField(max_length=255, null=True, blank=True)
    hint  = models.CharField(max_length=255, null=True, blank=True)
    super_hint  = models.TextField(null=True, blank=True)
    hour_coefficient = models.FloatField(null=True, blank=True)
    trip_coefficient = models.FloatField(null=True, blank=True)


    class Meta:
        verbose_name = "Inputs"
        verbose_name_plural = "Inputs"

class Settings(models.Model):
    name = models.CharField(max_length=255)

    checkboxes = models.ManyToManyField('Checkboxes')
    inputs = models.ManyToManyField('Inputs', blank=True)
    text = models.TextField(null=True, blank=True)

    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"

class Booking(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    excursion_id = models.IntegerField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    day = models.CharField(max_length=255)
    inputs = models.JSONField(null=True, blank=True)
    checkboxes = models.JSONField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    qr = models.URLField(null=True, blank=True)
    ticket = models.URLField(null=True, blank=True)
    qr_text = models.CharField(null=True, blank=True, max_length=255)
    front = models.IntegerField(null=True, blank=True)

    referal = models.IntegerField(null=True, blank=True)

    booking = models.BooleanField(default=False)

    def __str__(self):
        return self.name
